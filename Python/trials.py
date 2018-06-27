factor = int(input("Pick a number to see its factors! "))
x = 1
while (x < (factor+1)):
    if (factor % x == 0):
        print x 
    x += 1


