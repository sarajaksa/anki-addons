from anki.sched import Scheduler
from anki.hooks import wrap
from anki.sound import play
import os

# Add here the path to the folder with the addon
path = ""
# Here you can define the files to play with each ease (1=again, 4=best)
soundEase = {
              1: "1.mp3",
              2: "2.mp3",
              3: "3.mp3",
              4: "4.mp3",
             }

def playSoundEaseAnswer(self, card, ease):
    play(os.path.join(path, soundEase[ease]))

Scheduler.answerCard = wrap(Scheduler.answerCard, playSoundEaseAnswer, "before")
