#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import main_func as m_f
import time
import urllib.request, json 

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
				m_f.say("хорошо")
			else:
				hand_mode = True
				m_f.say("как хочешь")
		t = threading.Timer(30*60.0,main)
		t.start()
		if not hand_mode:
			#all interrupt functions
			if int(time.strftime('%H')) >= 23 :
				m_f.dont_say = 1
		
def stop():
	global start
	start = False
	t.join()

def updated():
	with urllib.request.urlopen("http://web-world.gq/api/index.php?updated=test") as url:
		data = json.loads(url.read().decode())
	if data['updated'] == '1':
		m_f.api_update_status()
	#u = threading.Timer(1.0,updated)
	#u.start()