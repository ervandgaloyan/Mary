#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import speech_recognition as sr
import time
from pygame import mixer
import functions as f
import urllib.request, json 
import os, sys
import random

dont_say = 0
mixer.init()
mixer.music.set_volume(0.5)

r = sr.Recognizer()

# RU to En #

_rus_chars = u"ё!;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ, "
_eng_chars = u"e-----icukengsszx-f=vaproldjeycsmit_b_-ICUKENGSSZX_F_VAPROLDJE-YCSMIT_B_--"
_trans_table = dict(zip(_rus_chars, _eng_chars))

def ru_to_en(s):
    return u''.join([_trans_table.get(c, c) for c in s])

#----------#
def txt_read(name):
	file = open(name,'r')
	lines = []
	for l in file:
		abc = l[:-1].split(' : ')
		lines.append(abc)
	file.close()
	return tuple(lines)
def txt_read_dict(name):
	file = open(name,'r')
	d = {}
	for l in file:
		abc = l[:-1].split(' : ')
		d[abc[0]] = abc[1]
	file.close()
	return d

def txt_write(name,arr):
	file = open(name,'w')
	for l in arr:
		file.write(l + ' : ' + arr.get(l) + '\n')
	file.close()
	return 0

def log(wr = 0,name = 'log.txt',op = 0,cl = 0):
	global logs
	if wr != 0:
		logs.write(time.strftime('%x') + ' ' + time.strftime('%X') + ' - ' + wr + "\n")
		return 1
	if op == 1:
		return open(name,'a')
	if cl == 1:
		logs.close()
		return 1
	return 0
def get_func(array,name):
	for l in array:
		if l[0] == name:
			return l[1]
	return 0

def __rec__():
	with sr.Microphone() as source:
	    print("Start config")
	    audio = r.adjust_for_ambient_noise(source)
	    print("Скажите что-нибудь")
	    audio = r.listen(source)
	print("Sending...")
	try:
	    return r.recognize_google(audio, language="ru-RU")
	except sr.UnknownValueError:
	    log(wr = "rec : UnknownValueError")
	    return 1
	except sr.RequestError as e:
	    log(wr = "rec : RequestError : " + e)
	    return 1

def stand_text(text):
	text = text.lower()
	text = text.strip()
	return text


def say(name_origin):
	global dont_say
	if dont_say == 0:
		name = ru_to_en(name_origin)
		try:
			mixer.music.load('mp3/'+name+'.mp3')
		except:
			say_update(name_origin)
			time.sleep(1)
			log(wr = "say_update - word : " + name_origin)
			try:
				mixer.music.load('mp3/'+name+'.mp3')
			except:
				mixer.music.load('mp3/except_load_error.mp3')
			else:
				mixer.music.load('mp3/'+name+'.mp3')
		finally:
			mixer.music.play()
			while mixer.music.get_busy():
				time.sleep(0.2)
	return 0

def say_update(word):
	from gtts import gTTS
	try : 
		tts = gTTS(text=word, lang='ru')
		tts.save('mp3/'+ru_to_en(word)+'.mp3')
	except:
		return 1
	return 0
def get_vol():
	return mixer.music.get_volume()
def set_vol(vol):
	return mixer.music.set_volume(vol)	

def api_other(file):
	with urllib.request.urlopen("http://web-world.gq/api/other.php?file=" + file) as url:
		data = json.loads(url.read().decode())
	return data
def api_other_write(file,data):
	file = open(file+".txt", "w")
	for d in data:
		file.write(d["query"] + " : " + d["answer"] + "\n")
	file.close()
	return 0

def restart():
	python = sys.executable
	os.execl(python,python, * sys.argv)

def answer_search(query,d):
	prcent = {}
	max = 59
	for l in d:
		pr = 0
		for q in query:
			pr = 100//len(l.split()) + pr if l.find(q) != -1 else pr
		prcent[d[l]] = pr
	for p in prcent:
		if prcent[p] > max:
			max = prcent[p]	
			ans = p

	ans = random.choice(ans.split(',')) if max != 59 else False
	del prcent
	del max
	del pr
	return ans

text_to_func = {
		"light_on" : f.__light_ON__,
		"light_off" : f.__light_OFF__,
		"door_open" : f.__door_open__,
		"door_close" : f.__door_close__,
		"by" : f.__close_all__,
		"anecdot" : f.__anecdote__,
		"vol_up" : f.__volumeUp__,
		"vol_down" : f.__volumeDown__,
		"how_old" : f.__howOld__,
		"update" : f.__update__,
		"say_time" : f.__sayTime__,
		"say_month" : f.__sayDate__
}

logs = log(op = 1)

