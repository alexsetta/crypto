import datetime, time

while True:
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
	print(now)
	time.sleep(60)