import time

secondsSinceEpoch = int(time.time())
daysSinceEpoch = int(secondsSinceEpoch / 86400)
timeData = time.localtime()

days = int(timeData.tm_mday)
hours = int(timeData.tm_hour)
mins = int(timeData.tm_min)
secs = int(timeData.tm_sec)
currentTime = ('current time: %d days, %d hours, %d mins %d secs') % (days, hours, mins, secs)

print(currentTime)
print('Days since epoch:', daysSinceEpoch)