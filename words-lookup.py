#!/usr/bin/python
# -*- coding: utf-8 -*-
#Anki add-on
#Written by Sara Jakša sarajaksa@gmail.com

from aqt import mw
from aqt.qt import *
from anki.hooks import addHook
import json

#The name of the field with the word
fromFieldName = "Front"
#The name of the field where you want definition
toFieldName = "Back"
#Place of the dictionary file
dictinaryFile = "../../addons21/dictionary.json"

def testFunction(editor):
    englishDictionary = getDictionary(dictinaryFile)
    noteIds = editor.selectedNotes()
    for noteId in noteIds:
        note = mw.col.getNote(noteId)
        word = note[fromFieldName]
        definition = getDefenition(word, englishDictionary)
        if definition:
            note[toFieldName] = definition
        note.flush()
    mw.reset()
    return None
    
def getDictionary(dictFile):
    with open(dictFile) as englishDictionaryFile:
        return json.load(englishDictionaryFile)
            
def getDefenition(word, dictionary):
    try:
        return dictionary[word.upper().strip()]
    except KeyError:
        return None

def addMenu(editor):
    editor.a = QAction("Generate Meaning", editor)
    editor.a.triggered.connect(lambda: testFunction(editor))
    editor.form.menuEdit.addAction(editor.a)

addHook("browser.setupMenus", addMenu)
