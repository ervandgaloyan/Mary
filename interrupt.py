#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import main_func as m_f
import time
start = True
hand_mode = True
asked = False

def main():
	global start
	global t
	global hand_mode
	global asked
	if start :
		if int(time.strftime('%H')) >= 23 and hand_mode and not asked:
			asked = True
			m_f.say("Включить? ночной режим")
			#rec = m_f.stand_text(str(m_f.__rec__()))
			rec = input(" - ")
			if rec == "да" or rec == "конечно":
				hand_mode = False
				print(hand_mode)
			else:
				hand_mode = True
				print(hand_mode)
		t = threading.Timer(30*60.0,main)
		t.start()
		if not hand_mode:
			#all interrupt functions
			if int(time.strftime('%H')) >= 23 :
				m_f.dont_say = 1
	else:
		print("interrupt Stoped")
		

def stop():
	global start
	start = False
	t.join()