seconds = 42 * 60 + 42
minutes = seconds / 60
hours = minutes / 60

miles = 10/1.61

print('Seconds in 42 minutes 42 seconds:', seconds)
print('Miles in 10 kilometers:', miles)
print('Average pace (time per mile in seconds):', miles/seconds)
print('Average pace (time per mile in minutes):', miles/minutes)
print('Average speed in mph:', miles/hours)