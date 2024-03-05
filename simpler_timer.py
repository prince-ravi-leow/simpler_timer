#!/usr/bin/env python3

import time
from datetime import timedelta
from math import modf

class SimplerTimer:
	"""

	⏱️ SimplerTimer - a simple interactive-first timer for all your Python timekeeping needs

	Simple usage:
	>>> timer = SimplerTimer()
	>>> my_awesome_function()
	>>> timer.end()
	>>> timer.report()
	Elapsed time (H:MM:SS.ff): 0:00:03.005237
	"""
	def __init__(self):
		"""
		Initialise timer
		"""
		self._start_time = time.time()
		self._elapsed_time = None
		self.status = "Active"
		self._durations = []

	def __str__(self):
		return f'Timer status: {self.status}'
	
	def is_active(self):
		"""
		Boolean evaluation of timer activity status
		"""
		if self._start_time:
			return True
		else:
			return False	

	def start(self):
		"""
		(Re)-start timer (requires timer to be ended beforehand)
		"""
		if not self._elapsed_time:
			raise Exception("Timer not ended. Call .end() to stop.")
		self._start_time = time.time()
		self._elapsed_time = None
		self.status = "Active"

	def pause(self):
		"""
		Pause running timer (changes status to: Paused)
		"""
		if not self.is_active():
			raise Exception("Timer inactive. Call .start() to start.")
		self._durations.append(time.time())
		self.status = "Paused"

	def resume(self):
		"""
		Resume timer (changes status to: Active (resumed))
		"""
		if not self.is_active():
			raise Exception("Timer inactive. Call .start() to start.")
		self._durations.append(time.time())
		self.status = "Active (resumed)"

	def end(self):
		"""
		Stop the timer and return elapsed time (SS.ff)
		"""
		if not self._start_time:
			raise Exception("Timer not running. Call .start() to initiate.")
		if self.status == "Paused":
			self._durations.append(time.time())
		if len(self._durations) == 0:
			self._elapsed_time = time.time() - self._start_time
			self._start_time = None
			self.status = "Inactive"
		else:
			end = time.time()
			diff = 0
			odd_ts = self._durations[::2]
			even_ts = self._durations[1::2]
			for odd,even in zip(odd_ts,even_ts):
				diff += even - odd
			self._elapsed_time = end - diff - self._start_time
			self._start_time = None
			self.status = "Inactive"
			self._durations = []
			
		return self._elapsed_time
	
	def progress(self):
		"""
		Report progress of running timer
		"""
		if not self._start_time:
			raise Exception("Timer not running. Call .start() to initiate.")
		if len(self._durations) == 0:
			prog = time.time() - self._start_time
		else:
			end = time.time()
			diff = 0
			odd_ts = self._durations[::2]
			even_ts = self._durations[1::2]
			for odd,even in zip(odd_ts,even_ts):
				diff += even - odd
			prog = end - diff - self._start_time
			
		return prog	
	
	def recall(self):
		"""
		Recall elapsed time (SS.ff)
		"""
		if not self._elapsed_time:
			raise Exception("Timer not ended. Call .end() to stop.")
		return self._elapsed_time

	def report(self, strip:bool = None):
		"""
		Report execution time (H:MM:SS.ff)
		"""
		if not self._elapsed_time:
			raise Exception("Timer not ended. Call .end() to stop.")
		if not strip:
			seconds = self._elapsed_time
			msg = "Elapsed time (H:MM:SS.ff):"
		else:
			seconds = int(modf(self._elapsed_time)[1])
			msg = "Elapsed time (H:MM:SS):"
		exec_time = str(timedelta(seconds = seconds))
		print(f"{msg} {exec_time}")

	def timestamp(self, strip:bool = None):
		"""
		Convert stored elapsed time float to H:MM:SS.ff-formatted timestamp
		"""
		if not self._elapsed_time:
			raise Exception("Timer not ended. Call .end() to stop.")
		if not strip:
			seconds = self._elapsed_time
		else:
			seconds = int(modf(self._elapsed_time)[1])
		return str(timedelta(seconds = seconds))	
	
def simplerer_timer(start:float = None) -> float:
	"""
	*** (even) simpler timer ***
	Usage:
	>>> from simpler_timer import simplerer_timer
	>>> start = simplerer_timer()
	>>> my_awesome_function()
	>>> simplerer_timer(start)
	Elapsed time (H:MM:SS.ff): 0:00:01.340824
	1.3408238887786865
	"""

	if not start:
		return time.time()
	else:
		elapsed_time = time.time() - start
		elapsed_time_string = str(timedelta(seconds = elapsed_time))
		print(f"Elapsed time (H:MM:SS.ff): {elapsed_time_string}")
		return elapsed_time