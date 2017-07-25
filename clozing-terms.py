#!/usr/bin/python
# -*- coding: utf-8 -*-
#Anki add-on
#Written by Sara Jakša sarajaksa@gmail.com

from aqt import mw
from anki.hooks import addHook
from aqt.editor import _html
from aqt.qt import *

import re
import unicodedata
import string

def addMenu(browser):
    button = QAction("Clozing specifics terms", browser)
    button.triggered.connect(lambda: ClozingWords(browser))
    browser.form.menuEdit.addAction(button)

class ClozingWords(QWidget):

    def __init__(self, browser):
        super(ClozingWords, self).__init__()
        self.mw = mw
        self.models = self.mw.col.models.all()
        
        self.term = ""
        self.noteIds = self.getNoteIds(browser)

        self.window = QDialog(mw)
        self.window.setWindowTitle('Write the terms to cloze')
        self.window.layout = QVBoxLayout(self.window)
        
        self.label_tags = QLabel("Which thing do you want to cloze in all the notes?")
        self.window.layout.addWidget(self.label_tags)
        
        self.terms = QLineEdit()
        self.terms.editingFinished.connect(self.whichTerm)
        self.window.layout.addWidget(self.terms)
        
        self.saveButton = QPushButton("Cloze")
        self.saveButton.pressed.connect(self.clozeEverything)
        self.window.layout.addWidget(self.saveButton)
        
        self.stopButton = QPushButton("I am finished")
        self.stopButton.pressed.connect(self.stop)
        self.window.layout.addWidget(self.stopButton)
        
        self.window.show()
        self.window.exec_()
        
    def whichTerm(self):
        self.term = self.terms.text()
        
    def getNoteIds(self, browser):
        return browser.selectedNotes()
        
    def clozeEverything(self):
        for noteId in self.noteIds:
            note = mw.col.getNote(noteId)
            if self.isCloze(noteId):
                for name, text in note.items():
                    newText = self.clozeTermsInNote(name, text, note)
                    note[name] = newText
                    note.flush()
                    mw.reset()
                    break
        
    def clozeTermsInNote(self, name, noteText, note):
        newText = noteText
        if not self.term in noteText:
            return newText
        allWords = re.finditer(r"\b" + re.escape(self.term) + r"\b", noteText)
        allWords = [m.start() for m in allWords][::-1]
        clozeNumber = self.findNextClozeNumber(noteText)
        for word in allWords:
            if not noteText[word - 1].isalnum() or noteText[word + len(self.term)].isalnum():
                if not "{{" in noteText[word:word + len(self.term)] or "}}" in noteText[word:word + len(self.term)]:
                    newText = newText[:word + len(self.term)] + "}}" + newText[word + len(self.term):]
                    newText = newText[:word] + "{{c" + str(clozeNumber) + "::" + newText[word:]
                    clozeNumber = clozeNumber + 1
        return newText
        
    def findNextClozeNumber(self, noteText):
        allClozeNumbers = re.findall(r"{{c(\d*?)::", noteText)
        allClozeNumbers.sort()
        clozeNumber = int(allClozeNumbers[-1]) + 1
        return clozeNumber
        
    def isCloze(self, noteId):
        note = mw.col.getNote(noteId)
        return re.search('{{(.*:)*cloze:', note.model()['tmpls'][0]['qfmt'])
        
    def stop(self):
        self.window.close()
        
    
    
addHook("browser.setupMenus", addMenu)

