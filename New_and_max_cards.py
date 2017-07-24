#!/usr/bin/python
# -*- coding: utf-8 -*-
#Anki add-on
#Written by Sara Jakša sarajaksa@gmail.com

from aqt import mw
from aqt.qt import *
from aqt.deckbrowser import DeckBrowser
from aqt.deckconf import DeckConf

class ScrollArea(QScrollArea):

    def __init__(self):
        super(ScrollArea, self).__init__()

class ConfigurationWindow(QWidget):

    def __init__(self):
        super(ConfigurationWindow, self).__init__()
        #Things connected to Anki
        self.mw = mw
        self.allDecks = self.mw.col.decks.all()
        self.allConf = self.mw.col.decks.allConf()
        #Things connected to GUI
        self.layout = QGridLayout(self)
        self.grid = []
        self.labels = {}
        self.decksOrder = self.deckLevel()
        self.showContent()
        self.setWindowTitle('New Cards / Max Reviews per Day')
        self.show()

    #Finds all decks and sort them in the right order (only the names)
    def deckLevel(self):
        deckSort = []
        for deck in self.allDecks:
            if deck[u'dyn'] is 0:
                deckSort.append(deck[u'name'])
        deckSort.sort()
        return deckSort

    #Helping function for creating a grid
    def appendGrid(self, j):
        for i in range(5):
            self.grid.append((j,i))

    #Helps with creating the elements in the window
    def showContent(self):
        self.showLabels()
        decks = self.decksOrder
        i = 1
        for deck in decks:
            self.appendGrid(i)
            self.showElements(deck, i)
            i += 1
        self.showSaveButton(i)

    #Show save button
    def showSaveButton(self, i):
        self.appendGrid(i)
        self.labels[(i, 4)] = QPushButton("Save")
        self.layout.addWidget(self.labels[(i,4)], self.grid[i*5+4][0], self.grid[i*5+4][1])
        self.labels[(i,4)].pressed.connect(self.saveConfiguration)

    #get configuration from known id
    def getConfigurationFromId(self, id):
        for conf in self.allConf:
            if conf[u'id'] == id:
                return conf

    #Saves the configurations (only new and max cards)
    def saveConfiguration(self):
        decks = self.deckLevel()
        i = 1
        for deck in decks:
            self.deck = self.findDeck(deck)
            self.conf = self.findConfigurationFromDeck(self.deck)
            if not self.onlyDeckConfiguration(self.conf):
                name = self.conf[u'name'] + "_" + str("Copy")
                id = self.mw.col.decks.confId(name, cloneFrom=self.conf)
                self.deck['conf'] = id
                self.allConf = self.mw.col.decks.allConf()
                self.conf = self.getConfigurationFromId(id)
            self.conf['new']['perDay'] = self.labels[(i,1)].value()
            self.conf['rev']['perDay'] = self.labels[(i,3)].value()
            self.mw.col.decks.save(self.deck)
            self.mw.col.decks.save(self.conf)
            i += 1
        self.mw.onRefreshTimer()
        self.close()
        mw.myWidget.close()

    #It checks, if this is the only deck, using this configuration
    def onlyDeckConfiguration(self, conf):
        conf = conf[u'id']
        i = 0
        for deck in self.allDecks:
            if deck[u'dyn'] is 0:
                if deck[u'conf'] == conf:
                    i += 1
            if i > 1:
                return False
        return True

    #Shows elements for every deck
    def showElements(self, deck, i):
        deck = self.findDeck(deck)
        conf = self.findConfigurationFromDeck(deck)
        self.labels[(i, 0)] = QLabel(self.deckNameForShow(deck[u'name']))
        self.layout.addWidget(self.labels[(i, 0)], self.grid[i*5][0], self.grid[i*5][1])
        self.labels[(i, 1)] = QSpinBox()
        self.labels[(i, 1)].setMaximum(500000)
        self.labels[(i, 1)].setValue(conf[u'new'][u'perDay'])
        self.layout.addWidget(self.labels[(i, 1)], self.grid[i*5+1][0], self.grid[i*5+1][1])
        self.labels[(i,2)] = QLabel(self.findParentNew(deck))
        self.layout.addWidget(self.labels[(i, 2)], self.grid[i*5+2][0], self.grid[i*5+2][1])
        self.labels[(i, 3)] = QSpinBox()
        self.labels[(i, 3)].setMaximum(500000)
        self.labels[(i, 3)].setValue(conf[u'rev'][u'perDay'])
        self.layout.addWidget(self.labels[(i, 3)], self.grid[i*5+3][0], self.grid[i*5+3][1])
        self.labels[(i,4)] = QLabel(self.findParentMax(deck))
        self.layout.addWidget(self.labels[(i, 4)], self.grid[i*5+4][0], self.grid[i*5+4][1])

    #Helping function for finding parent's new cards
    def findParentNew(self, deck):
        new = self.findParent(deck)
        if not new:
            return ""
        new = new[0]
        return str(new)

    #Helping function for findinf parent's max cards
    def findParentMax(self, deck):
        rev = self.findParent(deck)
        if not rev:
            return ""
        rev = rev[1]
        return str(rev)

    #Finds the minimal number of new and max cards among all the parents deck
    def findParent(self, deck):
        name = deck[u'name']
        conf = self.findConfigurationFromDeck(deck)
        decks = []
        if "::" in name:
            decks = self.findParentName(name, decks)
        if decks:
            numberNew = []
            numberMax = []
            for deck in decks:
                configuration = self.findConfigurationFromDeck(self.findDeck(deck))
                numberNew.append(configuration[u'new'][u'perDay'])
                numberMax.append(configuration[u'rev'][u'perDay'])
                new = min(numberNew)
                Max = min(numberMax)
            return [new, Max]
        return None

    #Changes int into string
    def intToStr(self, number):
        return str(number)

    #Find every deck, that is a parent to this deck
    def findParentName(self, name, decks):
        if "::" in name:
            name = name.split("::")
            name = name[:-1]
            name = "::".join(name)
            decks = self.findParentName(name, decks)
        decks.append(name)
        return decks

    #Makes a string, that gets show in the window from full deck name
    def deckNameForShow(self, fullName):
        if '::' in fullName:
            nameList = fullName.split('::')
            name = '\r'*2*(len(nameList)-1) + nameList[-1]
            return name
        return fullName

    #Find deck from knowing the name
    def findDeck(self, name):
        for deck in self.allDecks:
            if deck[u'name'] == name:
                return deck

    #Find configuration, if you know the deck
    def findConfigurationFromDeck(self, deck):
        configuration = deck[u'conf']
        for conf in self.allConf:
            if conf[u'id'] == configuration:
                return conf

    #Shows labels up in the window
    def showLabels(self):
        labels = [u"Deck Name", u"New Cards/day", u"Parent's New", u"Reviews/day", u"Parent's Reviews"]
        i = 0
        self.appendGrid(i)
        for label in labels:
            self.labels[(0,i)] = QLabel(labels[i])
            self.layout.addWidget(self.labels[(0, i)], self.grid[i][0], self.grid[i][1])
            i += 1

def confStart():
    mw.myWidget = widget = ScrollArea()
    conf = ConfigurationWindow()
    widget.setWidget(conf)
    widget.show()

mw.action = QAction("New/Max Cards Configuration", mw)
mw.action.triggered.connect(confStart)
mw.form.menuTools.addAction(mw.action)
