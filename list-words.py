#!/usr/bin/python
# -*- coding: utf-8 -*-
#Anki add-on
#Written by Sara Jakša sarajaksa@gmail.com

from aqt import mw
from aqt.qt import *
import string
from aqt.webview import AnkiWebView
import codecs

class ListOfWords():
    
    def __init__(self):
        self.mw = mw
        self.models = self.mw.col.models.all()
        
        self.model = ""
        self.field = 0
        self.tag = ""
        self.isNew = 1
        self.isOld = 1
        
        self.words = ""
        
        self.window = QDialog(mw)
        self.window.setWindowTitle('List of Words - Choose')
        self.createWindow()
        
        self.window.show()
        self.window.exec_()
        
    def startReport(self): 
        self.report = QDialog(mw)
        self.report.setWindowTitle('List of Words - Report')
        self.report.layout = QVBoxLayout(self.report)
        self.webView = AnkiWebView()
        self.report.layout.addWidget(self.webView)
        
        self.printButton = self.saveButton = QPushButton("Print List")
        self.printButton.pressed.connect(self.printWordList)
        
    def printWordList(self):
        filename = QFileDialog.getSaveFileName()
        with codecs.open(filename, "wt", encoding="utf-8") as file:
            file.write(self.words)
        return filename   
        
    def createWindow(self):
    
        self.window.layout = QVBoxLayout(self.window)
        
        self.choose_model = QComboBox()
        self.choose_model.addItem("Choose a Model")
        for model in self.models:
            self.choose_model.addItem(model["name"])
        self.choose_model.activated.connect(self.populateFields)
        self.window.layout.addWidget(self.choose_model)
        
        self.choose_field = QComboBox()
        self.choose_field.activated.connect(self.whichField)
        self.window.layout.addWidget(self.choose_field)
        
        self.label_tags = QLabel("(Not required) Type and other tags you want to filter by:")
        self.window.layout.addWidget(self.label_tags)
        self.tags = QLineEdit()
        self.tags.editingFinished.connect(self.whichTags)
        self.window.layout.addWidget(self.tags)
        
        self.is_new = QCheckBox("Include new cards")
        self.is_new.setChecked(True)
        self.is_new.stateChanged.connect(self.whichNew)
        self.window.layout.addWidget(self.is_new)
        
        self.is_old = QCheckBox("Include already seen cards")
        self.is_old.setChecked(True)
        self.is_old.stateChanged.connect(self.whichOld)
        self.window.layout.addWidget(self.is_old)
        
        self.saveButton = QPushButton("Show")
        self.saveButton.pressed.connect(self.showWords)
        self.window.layout.addWidget(self.saveButton)
        
    def showWords(self):
        self.window.close()
        self.startReport()
        search_term = self.createSearchTerm()
        ids = mw.col.findNotes(search_term)
        words = self.get_all_notes(ids, self.field)
        report = self.createWordsList(words)
        self.words = self.createWordListsPrint(words)
        self.webView.stdHtml(report)
        self.report.layout.addWidget(self.printButton)
        self.report.show()
        self.report.exec_()
        
    def createWordsList(self, words):
        wordList = ""
        for word in words:
            if word:
                wordList = wordList + word + "<br>"
        return wordList
        
    def createWordListsPrint(self, words):
        wordList = ""
        for word in words:
            if word:
                wordList = wordList + word.strip() + "\n"
        return wordList
        
    def get_all_notes(self, ids, field):
        words = set()
        for id in ids:
            note_id = mw.col.getNote(id)
            note_text = note_id.fields[field]
            note_text = note_text.lower()
            note_words = note_text.split(" ")
            note_text = "".join(l for l in note_text if l not in string.punctuation.replace("'", ""))
            for word in note_words:
                word_first = word
                while 1:
                    word_second = word_first.strip().rstrip(string.punctuation).lstrip(string.punctuation)
                    if word_first == word_second:
                        words.add(word_second)
                        break
                    else:
                        word_first = word_second
        words = list(words)
        words.sort()
        return words
        
    def createSearchTerm(self):
        search_term = ""
        if self.model:
            search_term = search_term + "mid:" + str(self.model) + " "
        if self.tag:
            search_term = search_term + self.tag + " "
        if self.isNew and self.isOld:
            return search_term
        if self.isNew:
            return search_term + "is:new"  
        if self.isOld:
            return search_term + "-is:new"
    
    def populateFields(self):
        self.choose_field.clear()
        self.choose_field.addItem("Choose Field")
        currentField = self.choose_model.currentIndex() - 1
        self.model = self.models[currentField]["id"]
        fields = self.models[currentField]["flds"]
        for field in fields:
            self.choose_field.addItem(field["name"])
            
    def whichField(self):
        self.field = self.choose_field.currentIndex() - 1
        
    def whichTags(self):
        self.tag = self.tags.text()
        
    def whichNew(self):
        self.isNew = self.is_new.isChecked()
    
    def whichOld(self):
        self.isOld = self.is_old.isChecked()
        
#Menu item
#################################
action = QAction("Test", mw)
mw.connect(action, SIGNAL("triggered()"), ListOfWords)
mw.form.menuTools.addAction(action)
