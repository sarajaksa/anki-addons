#!/usr/bin/python
# -*- coding: utf-8 -*-
#Anki add-on
#Written by Sara Jakša sarajaksa@gmail.com

from anki.hooks import addHook
from aqt import mw
from anki.sound import play
import os
import random

#lenght of a cycle (after how many answers does the audio play)
number = 5
#Folder with Audios (add the path to the folder)
audioPath = ""

current_number = -1

def plusAnswers():
    global current_number
    current_number = current_number + 1
    if current_number == number:
        current_number = 0
        playTheReward(audioPath)
    return None

def minusAnswers(self, ids):
    global current_number
    current_number = current_number - 1
    return None

def playTheReward(path):
    try:
        for (path, dirs, files) in os.walk(path):
            audioFiles = files
            break
        audioFile = random.choice(audioFiles)
        filePath = os.path.join(path, audioFile)
        playMusic(filePath)
    except:
        print "The folder is not specificed"
    return None

def playMusic(filePath):
    play(filePath)

addHook("showQuestion", plusAnswers)
addHook("remNotes", minusAnswers)
