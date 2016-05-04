
from datetime import datetime, timedelta


def getNDaysBeforeToday(N):
	dates = []
	for i in range(1,N+1):
		date_N_days_ago = datetime.now() - timedelta(days=i)
		dates.append(date_N_days_ago.strftime("%Y-%m-%d"))
	return dates


import os

print os.path.split("/a/b/c.txt")