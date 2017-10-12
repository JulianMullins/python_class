import json

def histogram(s):
    d = dict()
    for c in s.lower():
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

        # can rewrite if/else with: d[c] = d.get(c, 0) + 1
    return d

#print(histogram('Bookkeeper'))

def return_key_value(d):
    for k in d.keys():
        print(k)
    for v in d.values():
        print(v)

#return_key_value(histogram('This is a random string of words'))

with open('demo.json') as json_data:
    d = json.load(json_data)
    print(d)
