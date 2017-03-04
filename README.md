# README

The program in this files are different add-ons for ANKI, which is a SRS software ( http://ankisrs.net/ ).

## INSTALLING

Put the file in questions in the anki add-on folder (Anki/addons).
DELETING DECKS CONFIGURATIONS

This one provides a quick way to delete all the deck configurations that are currently not in use.

## ENGLISH WORD LOOKUP (file words-lookup.py)

This one is for looking up definitions of the English words. It looks up the word in one field and puts the definition in another field. Work with words only.

The words-lookup.py file tell the program which field to check for word (line 12) and where to put the definition (line 14). 

When in Anki, open the Browse window. Highlight the cards that you want to check. Under menu Edit, there is a button generate meaning. Click it. If the word was in the dictionary, the definition is posted in appropriate field.

In order for it to work, there needs to be a dictionary.json file somewhere on the disk. In the file, on line 16, write in the location of the dictionary.json file.

The program is using the json version of Webster's Unabridged English Dictionary. The project dealing with this can be found on https://github.com/adambom/dictionary

## WORDS HIGHLIGHTER (file Words_Highlighter.py)

This one is for highlighting the words. It checks the words in the external file, and changes their color.

In the Anki card browser, under the menu, there is a highlight words button (Edit > Highlight words). Pick the cards, that you want to change, and click on the button.

In the addon file, you can change which field get checked, by changing the onlyFields variable. If you want only the Front field to get checked, and the rest of them to be left alone, then change the line to onlyFields = ["Front"]. The default (empty) means that all the fields get changed.

For it to work, you need an additional csv file named words-highlighting.csv. This is the list of all the words that will change color. It format is word (lowercase) + tab + color (word or HEX).

Example:
anki	red
knowledge	blue
SRS	red

## NEW MAX CARDS (file New_and_max_cards.py)

This one provides a more convenient way to change the number of new cards to learn and how many cards to review for multiple decks. 

The program adds the button New/Max Cards Configuration to Tools menu.

## REWARD SOUND (file reward_sound.py)

This is an Anki add, This one plays a sound as a reward after answering a specific number of cards.

If you want to change the values:

To change the number of cards to be shown, before the file is played (default 5):
+ change the number in the line 13 (number = 5)

To point to the folders with the files to be played:
+ Add them to the list on the line 15 (audioPath = [])
Examples:
+ If the files are in folder /home/guest/audio -> audioPath = ["/home/guest/audio"] (Linux)
+ If files are in the folder E:\Dropbox\Music -> audioPath = ["E:\Dropbox\Music"] (Windows)
+ If the files are in folder /home/guest/audio, /home/shared/audio and /home/mother/video -> audioPath = ["/home/guest/audio", "/home/shared/audio", "/home/mother/video"]

## WORD LIST (file Word_Lists_Generator.py)

This one lists the words in the deck.

## HEISING STATS (heising_stats.py)

This one provides the statistics of how many kanji were added and studied.

## TEXT BUTTONS (edit-buttons.py)

This one adds additional buttons to the editing menu.

## DELETE REDUNDANT CONFIGURATIONS (file Deleting_Reduant_Configurations.py)

This one goes over all the deck configurations and deletes all that are not in use but the original one.

## CLOZING TERMS (file clozing-terms.py)

Finds all the instances of the phrase and make an additional cloze question out of it.

## LICENSE

This scripts are unlicensed (the license found on http://unlicense.org/ ), except the dictionary.json file, which is licensed under the MIT license (originally found on: https://github.com/adambom/dictionary ).

CONTACT

For any questions, complains or comments, you can reach me on sarajaksa@gmail.com .
