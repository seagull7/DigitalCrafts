import math
#1-
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
} 
print phonebook_dict["Elizabeth"]
phonebook_dict["Kareen"] = "938-489-1234"
del phonebook_dict["Alice"]
phonebook_dict["Bob"] = "968-345-2345"
print (phonebook_dict)

#2- 
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
     {
       'name': 'Jasmine',
       'email': 'jasmine@yahoo.com',
       'interests': ['photography', 'tennis']
     },
     {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
     }
    ]
} 
print (ramit["email"])
print (ramit['interests'][0])
print (ramit['friends'][0]['email'])
print (ramit['friends'][1]['interests'][1])

#3-(letter summary)
def letter_histogram(word):
    dic = {}
    for i in word:
        counter = 0
        for j in word:
            if (i == j):
                counter += 1
                dic[i] = counter
    return dic
print (letter_histogram("Hello"))

#4- (Word Summary)
def word_histogram(text):
    dic = {}
    arr = []
    word = ''
    for i in text:
        if i != " ":
            word += i
        elif i == " ":
            arr.append(word)
            word = ""
    arr.append(word)
    for i in arr:
        counter = 0
        for j in arr:
            if (i == j):
                counter += 1
                dic[i] = counter
    return dic
print (word_histogram("to be or not to be"))

#5- (Bono)
def top(tally):
    max_val = max(tally, key=tally.get)
    return max_val