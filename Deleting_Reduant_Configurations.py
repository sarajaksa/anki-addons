#!/usr/bin/python
# -*- coding: utf-8 -*-
#Anki add-on
#Written by Sara Jakša sarajaksa@gmail.com

from aqt import mw
from aqt.qt import *
from aqt.deckconf import DeckConf

class ConfigurationDeletions():

	def __init__(self):
		self.mw = mw
		self.allDecks = mw.col.decks.all()
		self.allConf = mw.col.decks.allConf()

	#Odstrani configuracije
	def remGroup(self, conf4Del):
		#deck = self.findDeckFromConfiguration(self.findConfigurationFromId(1))
		#configuration = DeckConf(mw, deck)
		for conf in conf4Del:
			conf = self.findConfigurationFromId(conf)
			if not conf['id'] == 1:
				mw.col.decks.remConf(conf['id'])
				#configuration.loadConfs()

	def findDeckFromConfiguration(self, conf):
		for deck in self.allDecks:
			if deck[u'conf'] == conf:
				return deck

	#Finds the ID of all configurations
	def findIdConfigurations(self):
		confId = set()
		for conf in self.allConf:
			confId.add(conf[u'id'])
		return confId

	#Find if it is a filter deck
	def filterDeck(self, deck):
		if deck[u'dyn']:
			return True
		return False
			
	#Finds all the decks and their's configurations
	def findDeckIdConfiguration(self):
		deckConfId = set()
		for deck in self.allDecks:
			if self.filterDeck(deck):
				return None
			deckConfId.add(deck['conf'])
		return deckConfId

	#finds all configuration, with no deck
	def ophranConfigurations(self, confId, deckId):
		conf4Del = []
		for ID in confId:
			if ID not in deckId:
				conf4Del.append(ID)
		return conf4Del

	#From confId find configuration
	def findConfigurationFromId(self, Id):
		for conf in self.allConf:
			if conf['id'] == Id:
				return conf

	def start(self):
		self.remGroup(self.ophranConfigurations(self.findIdConfigurations(), self.findDeckIdConfiguration()))
		return None

def confStart():
	deletion = ConfigurationDeletions()
	deletion.start()

mw.action = QAction("Delete Reduant Configurations", mw)
mw.action.triggered.connect(confStart)
mw.form.menuTools.addAction(mw.action)
