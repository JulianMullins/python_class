# exercise 1
team = 'New England Patriots'
# print(team[0:11])
# print(team[12:20])

# exercise 2
def countLetter(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count = count + 1
    print(count)

countLetter('Testing this function', 't')

# exercise 3
random_string = 'This is a completely random string with my name in it: Julian Mullins.'
suite_mates = ('Brandon Kam', "Naeli Elizalde", "Gwendolyn Lee")

phrase = 'My suite mates are: ' + ', '.join(suite_mates)

print(random_string.find('Julian'))
print(phrase)

# exercise 4
item_list = ('bananas', 'rice', 'paprika', 'potato chips')

def shopping_list(list):
    count = 0
    total_price = 0
    longest = 0

    while(count < len(list)):
        for j in range(0, len(list[count])):
            if(len(list[count]) > longest):
                longest = len(list[count]) + 10
        count += 1

    count = 0

    while(count < len(list)):
        total_item_price = 0

        for i in range(0, len(list[count])):
            total_item_price += int(ord(list[count][i])-96)

        total_price += total_item_price
        price = '$' + '%.2f' % total_item_price
        print(str(list[count]).ljust(longest) + price)
        count += 1
        
    total_price = '$' + '%.2f' % total_price
    print(''.ljust(longest+5, '-'))
    print('Total'.ljust(longest) + total_price)

shopping_list(item_list)