import re
from aqt import mw
from aqt.qt import QAction
from anki.hooks import addHook
from .consts import field_to_deck_map


def addDeckButton(browser):
    deckButton = QAction("Put in right deck (JAP)", browser)
    deckButton.triggered.connect(lambda: onDeckChange(browser))
    browser.form.menuEdit.addAction(deckButton)


def onDeckChange(browser):
    changeDeckBasedOnClozeField(browser.selectedCards())


def getClozeNumbers(sentence):
    cloze_numbers = re.findall(r"{{c(\d+)::.+?}}", sentence)
    return [int(number) for number in cloze_numbers]


def changeDeckBasedOnClozeField(cids):
    for cid in cids:
        card = mw.col.getCard(cid)
        for field_deck_pairing in field_to_deck_map:
            current_field = field_deck_pairing["field"]
            current_deck = field_deck_pairing["deck"]
            card_number = card.ord + 1
            cloze_numbers = getClozeNumbers(card.note()[current_field])
            if card_number in cloze_numbers:
                card.did = current_deck
        card.flush()
    mw.progress.finish()
    mw.reset()


addHook("browser.setupMenus", addDeckButton)
