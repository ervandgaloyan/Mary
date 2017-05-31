#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import main_func as m_f
import wikipedia as wiki
import time

wiki.set_lang("ru")
def paragraph(name):
	try:
		#print(wiki.summary(name,sentences=4))
		m_f.say_wiki(wiki.summary(name,sentences=2))
	except:
		m_f.say("такой стати не существует")
		time.sleep(1)
		m_f.say("попробую найти")
		search(name)
	return 0

def search(name):
	result = wiki.search(name)
	if len(result) > 0 :
		loop = len(result) if len(result) < 4 else 4
		m_f.say("я нашла несколько статей")
		for l in range(1,loop):
			m_f.say(result[l])
		m_f.say("какой из них тебе нужен?")
		rec = input(" - ")
		parag = result[1] if rec == "первый" else result[2] if rec == "второй" else result[3] if rec == "третий" or rec == "последный" else 0
		if parag == 0:
			m_f.say("хорошо")
			return 0

		paragraph(parag)
		return 0
	else:
		m_f.say("Прости нечего не смогла найти")

	return 0
#search("звездные войны")
#paragraph("звездные войны")
