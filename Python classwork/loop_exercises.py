#1- Using a for loop and the range function, print out the numbers between 1 and 
# 10 inclusive, one on a line. 
for num in range(1, 10):
    print num,

#2- Same as the previous problem, except you will prompt the user for the number 
# to start on and the number to end on. 
start = raw_input("pick a starting number ")
end = raw_input("pick an ending number ")
for num in range(start, end):
    print num,

#3- Print each odd number between 1 and 10 inclusive. 
for num in range(1, 11, 2):
    print num,

#4- Print a 5x5 square of * characters. 
print ("*****\n")*5

#5- Print a NxN square of * characters. Prompt the user for N. 
x = int(input("How big shoudl the square be? "))
i=0
row = ""
while(i < x):
    row += "*"
    i += 1
print (row + "\n") * x

#6- Given a height and width, input by the user, print a box consisting of * 
# characters as its border. 
y = int(input("How tall should the box be? "))
x = int(input("How wide should the box be? "))
i = 0
j = 0
row = ""
side = "*"
while(i < x):
    row += "*"
    i += 1
while(j < (x-2)):
    side += " "
    j += 1    
side += "*"
fsides = side + "\n"

print (row)
print (fsides)*(y-2),
print (side)
print (row)

#7- Print a triangle consisting of * characters:
print('   *')
print('  ***')
print(' *****')
print('*******')

#8- Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.
y = int(input("How tall do you want your pyramid? "))
x = 1
while(y > 0):
    print (" ")*y +("*")*x
    x += 2
    y -= 1

#9- Print the multiplication table for numbers from 1 up to 10. 
print ("MULTIPLICATION TABLE:")
topline = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 1
print topline
while(x < 11):
    line = [x]
    for number in numbers:
        line.append((x * number))
    print line

    x += 1

#10- Given a string, input by the user, print that string with a box around it. 
# The box should stretch to the length of the string. 
word = raw_input("Pick a word to have a border put around it! ")
print ("*")*(len(word)+4)
print ("* " + word + " *")
print ("*")*(len(word)+4)

#11- Print the first 100 triangle numbers. 
x = 1
while(x < 101):
    y = ((x*(x+1))/2)
    print y 
    x += 1


#12- Given a number, print its factors. What are factors? 
factor = int(input("Pick a number to see its factors! "))
x = 1
while (x < (factor+1)):
    if (factor % x == 0):
        print x 
    x += 1