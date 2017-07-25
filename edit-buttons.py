#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from aqt.editor import Editor, _html
from anki.hooks import addHook

from aqt.qt import *

jsFont = """
	var e = document.getElementById("FontName");
	var font = e.options[e.selectedIndex].value;
	var front = '<span style="font-family:' + font + '" >'
	var back = '</span>'
	var s = window.getSelection();
	var r = s.getRangeAt(0);
	var content = r.cloneContents();
	var span = document.createElement("span")
	span.appendChild(content);
	var new_ = wrappedExceptForWhitespace(span.innerHTML, front, back);
	setFormat("inserthtml", new_);
	if (!span.innerHTML) {
	    // run with an empty selection; move cursor back past postfix
	    r = s.getRangeAt(0);
	    r.setStart(r.startContainer, r.startOffset - back.length);
	    r.collapse(true);
	    s.removeAllRanges();
	    s.addRange(r);
	    }
	 """
         
jsSize = """
	var e = document.getElementById("FontSize");
	var num = e.options[e.selectedIndex].value;
	var front = '<span style="font-size:' + num + 'px" >'
	var back = '</span>'
	var s = window.getSelection();
	var r = s.getRangeAt(0);
	var content = r.cloneContents();
	var span = document.createElement("span")
	span.appendChild(content);
	var new_ = wrappedExceptForWhitespace(span.innerHTML, front, back);
	setFormat("inserthtml", new_);
	if (!span.innerHTML) {
		// run with an empty selection; move cursor back past postfix
		r = s.getRangeAt(0);
		r.setStart(r.startContainer, r.startOffset - back.length);
		r.collapse(true);
		s.removeAllRanges();
		s.addRange(r);
		}
	"""
    
jsCase = """
	var s = window.getSelection();
	var r = s.getRangeAt(0);
	var content = r.cloneContents();
	var c = content.textContent
	if (c!=c.toUpperCase()) {
	var c = c.toUpperCase();
	} else {
	var c = c.toLowerCase();
	}
	r.deleteContents();
	r.insertNode(document.createTextNode(c));
	"""

def addButtonSize(buttons, editor):
    editor._links['size'] = changeSize
    allFontSizes = ""
    for i in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 28, 32, 36, 40, 44, 48, 54, 60, 66, 72, 80, 88, 96]:
        allFontSizes = allFontSizes + '<option>' + str(i) + '</option>'
    return buttons + ['<select name="FontSize" id=FontSize tabindex=1 title="Change Font" onChange="pycmd(\'size\');return false;">' + allFontSizes + '</select>\n\n']
    
def addButtonFont(buttons, editor):
    editor._links['font'] = changeFont
    allFonts =  QFontDatabase()
    allFonts = allFonts.families()
    allFontsSelection = ""
    for font in allFonts:
        allFontsSelection = allFontsSelection + '<option>' + font + '</option>'
    return buttons + ['<select name="FontName" id=FontName tabindex=2 style="width:80px" title="Change Font" onChange="pycmd(\'font\');return false;">' + allFontsSelection + '</select>\n\n']

def addButtonCase(buttons, editor):
    editor._links['case'] = changeCase
    return buttons + [editor._addButton("iconname", "case","tooltip")]
    
def changeSize(editor):
    editor.web.eval(jsSize)
    
def changeFont(editor):
    editor.web.eval(jsFont)
    
def changeCase(editor):
    editor.web.eval(jsCase)
    
addHook("setupEditorButtons", addButtonFont)
addHook("setupEditorButtons", addButtonSize)
addHook("setupEditorButtons", addButtonCase)
