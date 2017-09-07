import datetime

#class 2 work only

#1 The volume of a sphere with radius 5:
volume = (4/3) * 3.1415926 * (5**3)
print('Volume: ', volume)

#2 wholesale cost of 60 book copies
cover_price = 24.95
discount_price = cover_price - (.4 * cover_price)
wholesale_cost = (discount_price * 60) + (59 * .75) + 3
print('Wholesale Cost:', wholesale_cost)

#3 what time do I get home for breakfast?
start_time = datetime.datetime(100, 1, 1, 6,52) #instantiate a dummy date with the starting time
easy_pace = start_time + datetime.timedelta(minutes=8, seconds=15)
tempo_time = easy_pace + datetime.timedelta(minutes=21, seconds=36)
final_time = tempo_time + datetime.timedelta(minutes=8, seconds=15)
print('I will arrive home at: ', final_time.time())

#4 percent grade increase
starting_grade = 82
current_grade = 89
percent_increase = ((current_grade - starting_grade) / starting_grade) * 100
text = 'Percent increase: %.1f' % percent_increase
print(text)