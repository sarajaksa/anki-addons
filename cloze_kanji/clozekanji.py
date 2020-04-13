from anki.hooks import addHook
import re

kanjiField = "Kanji"
sentenceField = "Reading"

hiragana = (
    "あえいおうかけきこくがげぎごくられりろるやよゆまめみもむばべびぼぶはへひほふぱぺぴぽぷなねにのぬわをたてちとつだでぢどづさせしそすざぜじぞずんっょゃぉぃぁぇ"
)
katakana = (
    "アエイオウカケキコクガゲギゴクラレリロルヤヨユマメミモムハヘヒホフバベビボブパペピポプナネニノヌワヲタテチトツダデヂドヅサセシソスザゼジゾズンーッャェュグ"
)
others = "、『』。＞・ィ＜「」…？！~＆<>ｘ"
latin = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRQSTUVWXYZčšžćđČŠŽĆ"
numbers = "０１２３４５６７８９1234567890"


def sentenceFromCloze(sentence):
    all_cloze = re.findall(r"{{c\d+::.+?::.+?}}", sentence)
    all_replace_with = re.findall(r"{{c\d+::(.+?)::.+?}}", sentence)
    for cloze, replace_with in zip(all_cloze, all_replace_with):
        sentence = sentence.replace(cloze, replace_with)
    return sentence


def findNextClozeNumber(note):
    all_fields_text = ""
    for (name, value) in note.items():
        all_fields_text += value
    cloze_numbers = re.findall(r"{{c(\d+)::.+?}}", all_fields_text)
    if len(cloze_numbers) > 0:
        return max([int(n) for n in cloze_numbers]) + 1
    return 1


def kanjiCloze(fieldText, currentCloze=1):
    nonKanji = set(hiragana + katakana + others + latin + numbers)
    finalText = ""
    currentReading = False
    for char in fieldText:
        if char == "[":
            currentReading = True
        if not currentReading and char not in nonKanji and char.strip():
            char = "{{c" + str(currentCloze) + "::" + char + "}}"
            currentCloze += 1
        finalText += char
        if char == "]":
            currentReading = False
    return finalText


def onKanjiCloze(editor):
    nextClozeNumber = findNextClozeNumber(editor.note)
    fieldText = editor.note[sentenceField]
    sentenceToCloze = sentenceFromCloze(fieldText).replace("<br>", "").strip()
    sentenceWithClozeKanji = kanjiCloze(sentenceToCloze, nextClozeNumber)
    editor.note.__setitem__(kanjiField, sentenceWithClozeKanji)
    editor.note.flush()
    editor.mw.reset()


def addKanjiButton(buttons, editor):
    editor._links["clozekanji"] = onKanjiCloze
    return buttons + [
        editor._addButton(
            "", "clozekanji", "Create kanji field from reading field", "[漢]"
        )
    ]


addHook("setupEditorButtons", addKanjiButton)
