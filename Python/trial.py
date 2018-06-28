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
