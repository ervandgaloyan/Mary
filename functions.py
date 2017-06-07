#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import main_func as m_f
import interrupt
import forecast
import random,time
import os

def __light_ON__():
	m_f.log(wr = 'Light is ON')
	m_f.status_update(4,1)
	m_f.say('включила')
	return 0
def __light_OFF__():
	m_f.log(wr = 'Light is OFF')
	m_f.status_update(4,0)
	m_f.say('выключила')
	return 0
def __door_open__():
	m_f.log(wr = 'Door is opend')
	m_f.status_update(1,1)
	m_f.say('дверь открыта')
	return 0
def __door_close__():
	m_f.log(wr = 'Door is closed')
	m_f.status_update(1,0)
	m_f.say('дверь закрыта')
	return 0
def __close_all__():
	import sys
	m_f.log(wr = 'Close all')
	m_f.log(cl = 1)
	m_f.say('пока')
	interrupt.stop()
	sys.exit(0)
	return 0
def __anecdote__():
	anecdote = m_f.txt_read_dict('anecdote.txt')
	anec = random.choice(list(anecdote.items()))
	m_f.say(anec[1])
	time.sleep(2)
	m_f.say('нравиться?')

	rec = m_f.stand_text(str(m_f.__rec__()))
	print(rec)
	if (rec != 'да' and rec != 'очень' and rec != 'класс' and rec != 'круто'):
		print("yes")
		anecdote.pop(anec[0])
		m_f.txt_write('anecdote.txt',anecdote)
	del anecdote
	return 0

def __volumeUp__():
	print(m_f.get_vol())
	m_f.set_vol((1-float("%.5f" % m_f.get_vol()))/2 + m_f.get_vol())
	print(m_f.get_vol())
	return 0

def __volumeDown__():
	print(m_f.get_vol())
	m_f.set_vol(float("%.5f" % (m_f.get_vol()-m_f.get_vol()/2)))
	print(m_f.get_vol())
	return 0	

def __update__():
	m_f.api_other_write("func",m_f.api_other("func"))
	m_f.api_other_write("answers",m_f.api_other("answers"))
	m_f.say("обнавила")
	time.sleep(1)
	m_f.restart()
	return 0

def __howOld__():
	year = time.strftime('%y') if int(time.strftime('%W')) >= 48 else int(time.strftime('%y'))-1 
	m_f.say("мне {}{}".format(year," лет"))
	return 0

def __sayTime__():
	say = "сейчас {}{}{}{}".format(time.strftime('%H')," часов ",time.strftime('%M')," минут")
	m_f.say(say)
	os.remove("mp3/{}{}".format(m_f.ru_to_en(say),".mp3"))
	return 0
def __sayDate__():
	months_ru = {
		"01" : "Январь",
		"02" : "Февраль",
		"03" : "Март",
		"04" : "Апрель",
		"05" : "Май",
		"06" : "Июнь",
		"07" : "Июль",
		"08" : "Август",
		"09" : "Сентябрь",
		"10" : "Октябрь",
		"11" : "Ноябрь",
		"12" : "Декабрь"
	}
	say = "день {}{}{}".format(time.strftime('%d'),", месяц, ",months_ru[time.strftime('%m')])
	m_f.say(say)
	os.remove("mp3/{}{}".format(m_f.ru_to_en(say),".mp3"))
	return 0
def __weather__():
	forecast.measure()
	m_f.say("сийчас {} градусов, а влажность {}".format(forecast.temp , forecast.hum))
def __forecast__():
	forecast.weather_forecast()
	m_f.say("завтра ожидается от {} до {} градусов {}".format(forecast.low, forecast.high, "тепла" if forecast.low > 0 else "мароза"))
def __night__():
	interrupt.hand_mode = True
	m_f.say("отключила")
	return 0 