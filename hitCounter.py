from datetime import datetime
import time


hit_time = []

def record_hit():
	hit_time.append(datetime.now())

def get_count():
	start_time = round(time.time() * 1000)
	cnt = 0
	