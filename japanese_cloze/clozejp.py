from anki.hooks import addHook
import re


def findNextClozeNumber(note):
    all_fields_text = ""
    for (name, value) in note.items():
        all_fields_text += value
    cloze_numbers = re.findall(r"{{c(\d+)::.+?}}", all_fields_text)
    if len(cloze_numbers) > 0:
        return max([int(n) for n in cloze_numbers]) + 1
    return 1


def onJapaneseCloze(editor):
    nextClozeValue = findNextClozeNumber(editor.note)
    start = "{{c" + str(nextClozeValue) + "::"
    hintText = re.sub(r"\[.+?\]", "", editor.web.selectedText())
    end = "::" + hintText + "}}"
    editor.web.eval(f"wrap('{start}', '{end}');")


def addClozeJPButton(buttons, editor):
    editor._links["clozejp"] = onJapaneseCloze
    return buttons + [
        editor._addButton(
            "",
            "clozejp",
            "Helps with creating my Japanese cloze deletion cards",
            "[JP]",
        )
    ]


addHook("setupEditorButtons", addClozeJPButton)
