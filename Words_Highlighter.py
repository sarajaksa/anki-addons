#!/usr/bin/python
# -*- coding: utf-8 -*-
#Anki add-on
#Written by Sara Jakša sarajaksa@gmail.com

from aqt import mw
from anki.hooks import addHook
from aqt.qt import *
import re
import string
import unicodedata
import csv
import codecs

#Here you you can define, which fields should the script work on. If empty, it works on every one
onlyFields = []

def csvName(fileName="words-highlighting.csv"):
    path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(path, fileName)

def getWordList(wordList):
    wordsColor = dict()
    with codecs.open(wordList, "r") as coloredWordList:
        coloredWordList = csv.reader(coloredWordList, delimiter='\t', quotechar='|')
        for row in coloredWordList:
            wordsColor[row[0]] = row[1]
    return wordsColor

def removeAllHighlights(note, name, value):
    if 'class="highlight-words"' in value:
        value = re.sub('<font class="highlight-words"[^<]+?>', "", value)
        value = re.sub('</font>', "", value)
        note[name] = value
    return None

def addColor(note, name, text, wordsColor):
    lang = ""
    text = re.sub("<[^<]+?>", "", text)
    if text:
        if not unicodedata.category(text[0]) == "Lo":
            text = text.split(" ")
        else:
            text = list(text)
            lang = "jp"
        for i, word in enumerate(text):
            wordOnly = word.strip().rstrip(string.punctuation).lstrip(string.punctuation).lower()
            if wordOnly in wordsColor:
                text[i] = "<font class='highlight-words' color='" + wordsColor[wordOnly] + "'>" + word + '</font>'
        if not lang == "jp":
            note[name] = " " .join(text).strip()
        else:
            note[name] = "" .join(text).strip()
    return None

def highlightWords(browser):
    wordsColor = getWordList(wordList)
    noteIds = browser.selectedNotes()
    for noteId in noteIds:
        note = mw.col.getNote(noteId)
        for (name, value) in note.items():
            if not onlyFields:
                removeAllHighlights(note, name, value)
                addColor(note, name, value, wordsColor)
            if name in onlyFields:
                removeAllHighlights(note, name, value)
                addColor(note, name, value, wordsColor)
        note.flush()
    mw.reset()
    
def addMenu(browser):
    browser.button = QAction("Highlight words", browser)
    browser.button.triggered.connect(lambda: highlightWords(browser))
    browser.form.menuEdit.addAction(browser.button)

addHook("browser.setupMenus", addMenu)
#The word list with colors (csv file, first row=word, second row=color - name or HEX, seperator is tab). If file is named differently, then put the name of the file as the function argument (if name="lalala.csv", then csvName("lalala.csv")). It assumes that file is in the same folder than addons. If on different place, put the absolute path there instead
wordList = csvName()
