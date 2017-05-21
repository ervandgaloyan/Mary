#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import speech_recognition as sr

import main_func as m_f

import random

func_arr = m_f.txt_read('func.txt')
answer = m_f.txt_read_dict('answers.txt')

for s in answer:
	answer[s] = answer.get(s).split(',')


while True:
	rec = input(" - ")
	#rec = m_f.stand_text(str(m_f.__rec__()))
	func = m_f.stand_text(str(m_f.get_func(func_arr,rec)))
	try:
		m_f.text_to_func[func]()
	except KeyError:
		if answer.get(rec):
			ans = random.choice(answer.get(rec))
			print(ans)
			#m_f.say(ans)
#while True:
#	rec = m_f.stand_text(str(m_f.__rec__()))
#	func = m_f.stand_text(str(m_f.get_func(func_arr,rec)))
#	m_f.log(str(rec) + ' : ' + str(func))
#	print(rec)
#	try:
#		m_f.text_to_func[rec]()
#	except KeyError:
#		ans = answer.get(rec)
#		if ans != None:
#			m_f.say(ans)
	