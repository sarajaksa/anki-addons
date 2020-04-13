from anki.hooks import addHook
import re

clozeField = "Meaning"
finalField = "Expression"


def sentenceFromCloze(sentence):
    all_cloze = re.findall(r"{{c\d+::.+?}}", sentence)
    for cloze in all_cloze:
        replace_with = re.findall(r"{{c\d+::.+?::(.+?)}}", cloze)
        if replace_with:
            replace_with = replace_with[0]
        else:
            replace_with = re.findall(r"{{c\d+::(.+?)}}", cloze)[0]
        sentence = sentence.replace(cloze, replace_with)
    return sentence


def onSentenceFromCloze(editor):
    fieldText = editor.note[clozeField]
    sentenceWithoutCloze = sentenceFromCloze(fieldText)
    editor.note.__setitem__(finalField, sentenceWithoutCloze)
    editor.mw.reset()


def addSentenceFromClozeButton(buttons, editor):
    editor._links["sentencefromcloze"] = onSentenceFromCloze
    return buttons + [
        editor._addButton(
            "", "sentencefromcloze", "Creates sentence from cloze sentence", "[X]"
        )
    ]


addHook("setupEditorButtons", addSentenceFromClozeButton)
