#1- Given a string, print the string uppercased.
word = raw_input("Give me a string. ")
print (word.upper())

#2- Given a string, print the string uppercased.
word = raw_input("Give me a string. ")
print (word.capitalize())

#3- Given a string, print the string reversed.
word = raw_input("Give me a string. ")
print (word[::-1])

#4- Given a paragraph of text as a string, print the paragraph in leetspeak. 
# To translate a string to leetspeak, you need to replace make the following 
# character replacements (treat all input characters as uppercase):
word = raw_input("Give me a paragraph. ")
new_word = ""
for letter in word:
    if (letter.upper() == "A"):
        new_word += "4"
    elif (letter.upper() == "E"):
        new_word += "3"   
    elif (letter.upper() == "G"):
        new_word += "6"  
    elif (letter.upper() == "I"):
        new_word += "1"  
    elif (letter.upper() == "O"):
        new_word += "0"  
    elif (letter.upper() == "S"):
        new_word += "5"  
    elif (letter.upper() == "T"):
        new_word += "7"  
    else:
        new_word += letter
print (new_word)

#5- Given a word as a string, print the result of extending any long vowels to 
# the length of 5.
word = raw_input("Give me a word. ")
new_word = ""
for number in range(len(word)-1):
    if (word[number] == word[number+1] and word.upper()[number] == "A" or word[number] == "E" or word[number] == "I" or word[number] == "O" or word[number] == "U"):
        new_word += word[number] + word[number] + word[number] + word[number]
    else:
        new_word += word[number]
new_word += word[len(word)-1]
print (new_word)

#6- Given a string, print the Caesar Cipher (or ROT13) of that string. 
# Use your solution to decipher the following text: "lbh zhfg hayrnea 
# jung lbh unir yrnearq"
word = "lbh zhfg hayrnea jung lbh unir yrnearq"
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
position = 0
new_position = 0
for letter in word:
    if (letter.isspace() == False):
        position = alphabet.index(letter)
        new_position = position - 13
        if new_position < 0:
            new_position += 26
        print (alphabet[new_position]),