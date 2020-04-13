from aqt import mw
from aqt.qt import QAction
from anki.hooks import addHook


def addLeechButton(browser):
    leechButton = QAction("Reset Leech", browser)
    leechButton.triggered.connect(lambda: onResetLeech(browser))
    browser.form.menuEdit.addAction(leechButton)


def onResetLeech(browser):
    resetLeech(browser.selectedCards())


def resetLeech(cids):
    for cid in cids:
        card = mw.col.getCard(cid)
        card.lapses = 0
        card.flush()
    mw.progress.finish()
    mw.reset()


addHook("browser.setupMenus", addLeechButton)
