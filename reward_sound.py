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
number = 3
#Folder with Audios (add the path to the folder)
audioPath = []

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
    
def findMusicFilesFromPath(path):
    musicFiles = []
    for (path, dirs, files) in os.walk(path):
        if files:
            for f in files:
                musicFiles.append(os.path.join(path, f))
    return musicFiles

def findMusicFiles(paths):
    musicFiles = []
    for path in paths:
        musicFiles = musicFiles + findMusicFilesFromPath(path)
    return musicFiles

def playTheReward(path):
    try:
        audioFile = random.choice(audioFiles)
        playMusic(audioFile)
    except:
        print("Is file " + audioFile + " an audio or a video? (it might not be)")
    return None

def playMusic(filePath):
    play(filePath)

addHook("showQuestion", plusAnswers)
addHook("remNotes", minusAnswers)

audioFiles = findMusicFiles(audioPath)
