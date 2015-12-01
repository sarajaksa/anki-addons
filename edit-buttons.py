#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from aqt.editor import Editor, _html
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
   
def containerSize(editor, size):
    selection = editor.web.selectedText()
    if not selection:
        return
    editor.web.eval("wrap('[spreminjanjevelikosti1]', '[spreminjanjevelikosti2]');")
    html = editor.note.fields[editor.currentField]
    text = html.replace("[spreminjanjevelikosti1]", "<span style='font-size: " + str(size) + "px;'>")
    text = text.replace("[spreminjanjevelikosti2]", "</span>")
    saveChanges(editor, text)
    
def containerFont(editor, font):
    html = editor.note.fields[editor.currentField]
    selection = editor.web.selectedText()
    if not selection:
        return
    editor.web.eval("wrap('[spreminjanjepisave1]', '[spreminjanjepisave2]');")
    html = editor.note.fields[editor.currentField]
    text = html.replace("[spreminjanjepisave1]", "<span style='font-family: " + font + ";'>")
    text = text.replace("[spreminjanjepisave2]", "</span>")
    saveChanges(editor, text)

def containerCase(editor):
    selection = editor.web.selectedText()
    if not selection:
        return
    editor.web.eval("wrap('[spreminjanjecrk1]', '[spreminjanjecrk2]');")
    html = editor.note.fields[editor.currentField]
    matching = r"\[spreminjanjecrk1\](.*?)\[spreminjanjecrk2\]"
    selection = re.findall(matching, html)[0]
    replace = changeTextCase(selection)
    start = html.find("[spreminjanjecrk1]") + len("[spreminjanjecrk1]")
    text = html[:start] + replace + html[start + len(replace):]
    text = text.replace("[spreminjanjecrk1]", "")
    text = text.replace("[spreminjanjecrk2]", "")
    saveChanges(editor, text)
    
def changeTextCase(text):
    if text.isupper():
        return text.lower()
    return text.upper()
    
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
