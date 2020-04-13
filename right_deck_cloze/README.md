# Put cards in the right deck (for cloze cards with multiple cloze fields)

This add-on checks the selected cards, and then puts them in decks, based on which field the cloze appears in.

I personally use it for my Japanese sentence cards, as I have a note with different clozes for reading, kanji and meaning.

The add-on expects the field and deck id pairings in the consts.py file. It is a list of dictionaries. The field 'field' expects the name of the field, as it appears in the card editing. The field 'deck' expects the deck id. The example is shows in the added consts.py file.

The add-on was tested with Anki version: 2.1.15
