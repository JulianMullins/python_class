import time

secondsSinceEpoch = int(time.time())
daysSinceEpoch = int(secondsSinceEpoch / 86400)
timeData = time.localtime()

print('current time: ', str(timeData.tm_hour) + ':' + str(timeData.tm_min) + ':' + str(timeData.tm_sec))
print('Days since epoch:', daysSinceEpoch)