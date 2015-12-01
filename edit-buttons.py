#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from aqt.editor import Editor
from anki.hooks import wrap

from aqt.qt import *

def addButtonSize(editor):
    addSizes(editor)
    
def addButtonFont(editor):
    addFonts(editor)

def addButtonCase(editor):
    editor._addButton("changeUpper", lambda: containerCase(editor), key=_("Shift+F3"), tip=_(u"Changes case of the text (Shift+F3)"), text=_(u"Cc"))
    
def addSizes(self):
        sizeOptions = QComboBox()
        sizes = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 28, 32, 36, 40, 44, 48, 54, 60, 66, 72, 80, 88, 96]
        for size in sizes:
            sizeOptions.addItem(str(size))
        sizeOptions.activated.connect(lambda: containerSize(self, sizeOptions.currentText()))
        self.iconsBox.addWidget(sizeOptions)
    
def addFonts(self):
    fontOptions = QComboBox()
    allfonts = QFontDatabase()
    fonts = allfonts.families()
    fonts = [re.sub(r'\[.*?\]', '', font).strip() for font in fonts]
    for font in fonts:
        fontOptions.addItem(str(font))
    fontOptions.activated.connect(lambda: containerFont(self, fontOptions.currentText()))
    self.iconsBox.addWidget(fontOptions)

def changeTextCase(text):
    if text.isupper():
        return text.lower()
    return text.upper()
    
def changeFont(text, font):
    return "<span style='font-family: " + font + ";'>" + text + "</span>"
    
def changeSize(text, size):
    return "<span style='font-size: " + str(size) + "px;'>" + text + "</span>"
    
def findSelectedText(html, selection):
    if selection in html:
        return selection
    text = selection
    foundMatch = False
    while not foundMatch:
        if text in html:
            foundMatch = True
        else:
            text = text[:-1]
    start = html.find(text)
    foundMatch = False
    text = selection
    while not foundMatch:
        if text in html:
            foundMatch = True
        else:
            text = text[1:]
    end = html.find(text) + len(text)
    html = html[start:end]
    return html
    
def containerSize(editor, size):
    html = editor.note.fields[editor.currentField]
    selection = editor.web.selectedText()
    selection = findSelectedText(html, selection)
    replace = changeSize(selection, size)
    text = html.replace(selection, replace)
    saveChanges(editor, text)

def containerCase(editor):
    html = editor.note.fields[editor.currentField]
    selection = editor.web.selectedText()
    selection = findSelectedText(html, selection)
    replace = changeTextCase(selection)
    text = html.replace(selection, replace)
    saveChanges(editor, text)
    
def containerFont(editor, font):
    html = editor.note.fields[editor.currentField]
    selection = editor.web.selectedText()
    selection = findSelectedText(html, selection)
    replace = changeFont(selection, font)
    text = html.replace(selection, replace)
    saveChanges(editor, text)
    
def saveChanges(editor, text):
    editor.note.fields[editor.currentField] = text
    editor.loadNote()
    editor.web.setFocus()
    editor.saveNow()
    editor.web.setFocus()
    editor.web.eval("focusField(%d);" % editor.currentField)
    
Editor.setupButtons = wrap(Editor.setupButtons, addButtonFont)
Editor.setupButtons = wrap(Editor.setupButtons, addButtonSize)
Editor.setupButtons = wrap(Editor.setupButtons, addButtonCase)
