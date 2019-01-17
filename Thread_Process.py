from threading import Thread
from multiprocessing import Process

def spawn_thread(function, arguments):
	thread = Thread(target = function, args = arguments)
	thread.start()

def spawn_process(function, arguments):
	process = Process(target = function, args = arguments)
	process.start()