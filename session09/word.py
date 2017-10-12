# fin = open('words.txt')
# line = fin.readline()
# print(rep(line))

fin = open('words.txt')

def find_long_words():
    for line in fin:
        word = line.strip()
        if(len(word) > 20):
            print(word, len(word))

#find_long_words()

def has_no_e(word):
    for letter in word:
        if letter.lower() == 'e':
            return False
    return True

    # return not 'e' in word.lower()

#print(has_no_e('halloe'))

def find_words_no_e():
    count_e = 0
    total_count = 0
    percentage = 0

    for line in fin:
        total_count += 1
        word = line.strip()
        if has_no_e(word):
            count_e += 1
            #print(word)
    
    percentage = count_e / total_count
    return percentage
    
#print('Percentage of words with no e is {:2f}' .format(find_words_no_e() * 100))

# exercise 1.3
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

# print(avoids('Babson', 'abcd'))

# exercise 1.3 (part 2)
def avoids_input():
    total_count = 0
    avoid_count = 0
    forbidden = input('Enter a string of forbidden letters: ').strip()
    for line in fin:
        word = line.strip()
        total_count += 1
        for letter in word:
            if letter in forbidden:
                continue
            else:
                avoid_count +=1
    print('total word count: ' + str(total_count))
    print('total word count without the letters ' + forbidden + ': ' + str(avoid_count))

#avoids_input()

# exercise 1.4
def uses_only(word, letters):
    for letter in word:
        if not letter.lower() in letters:
            return False
    return True

# print(uses_only('adef', 'abcdefghi'))

# exercise 1.5
def uses_all(word, req_letters):
    for letter in req_letters:
        if not letter in word:
            return False
    return True

# print(uses_all('blah', 'halbs'))

# exercise 1.6
def is_abecedarian(word):
    word = word.lower()
    start = ord(word[0])

    for letter in word:
        if(ord(letter) >= start):
            start = ord(letter)
        else:
            return False
    return True

# print(is_abecedarian('abcdefghijklmnopqrstuvwxyz'))


# exercise 2.1
def is_abecedarian_recurse(word):
    word = word.lower()
    start = ord(word[0])

    for letter in word:
        if(ord(letter) >= start):
            start = ord(letter)
        else:
            return False
    return True
