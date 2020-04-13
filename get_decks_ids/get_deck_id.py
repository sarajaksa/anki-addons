from aqt import mw
from aqt.qt import QAction
from anki.hooks import addHook


def addFindDeckIdsButton(browser):
    leechButton = QAction("Print deck ids in terminal", browser)
    leechButton.triggered.connect(lambda: onFindDeckIds(browser))
    browser.form.menuEdit.addAction(leechButton)


def onFindDeckIds(browser):
    findDeckIds(browser.selectedCards())


def findDeckIds(cids):
    for cid in cids:
        card = mw.col.getCard(cid)
        print(card.did)


addHook("browser.setupMenus", addFindDeckIdsButton)
