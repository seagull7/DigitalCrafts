#1
name = raw_input('What do they call you? ')

greetings = "Well met, %s!" %(name)

print (greetings)

#2
name = raw_input('What do they call you, again? Speak up son! ')
l = len(name)

greetings = "WELL MET, %s! YOUR NAME HAS %d LETTERS IN IT, SPEAK THEM PROUDLY!\n" %(name.upper(), l)

print (greetings)

#3 
print ("Let's play a game %s, give me some words and I will make you a sentence!" %(name))
fname = raw_input("Give me a random name, young %s! " %(name))
fweapon= raw_input("Now how about a random weapon? dont think to hard now. ")
print (fname + " needs some work using his " + fweapon + " before he goes into true combat!\n")

#4
day = int(input('Now, young ' + name + ", give me a number between 0 and 6 to determine your day on the watch schedule! "))
if (day >-1 and day <7):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print ("Your day to watch will be " + week[day] + " young " + name + "!\n")
else:
    print ("That isn't between 0 and 6, now you will be on watch every work day!\n")

#5
def workday():
    day = int(input('Now, young ' + name + ", give me a week day (in number from from 0-6) and I will tell you if you have it off or not! " ))
    if (day == 5 or day == 6):
        print ("This is not a day to work, go make merry with your friends!\n")
    elif (day > -1 and day < 5):
        print ("This is a day for hard work!\n")
    else:
        print ("That is not a day of the week! Try again young " + name  + "!\n")
        workday()

workday()

#6
temp = int(input("Hey, " + name +  " did you know your camp uses Fahrenheit, not Celcius?\n Give me the temp and I'll convert it for you! "))
ntemp = temp * 1.8 + 32 
ntemp = str(ntemp)
print ("The temperature is about " + ntemp + " degrees in Celcius\n")

#7
print ("While we are sharing life tips, let me share with you how to tip properly, young " + name + "!")

serv = raw_input("How well was your service last night at dinner? good, fair, or bad? ")
if (serv.upper() == 'GOOD'):
    multiplier = .2
elif (serv.upper() == 'FAIR'):
    multiplier = .15
elif (serv.upper() == 'BAD'):
    multiplier = .1
else:
    print ("That wasn't an option, try again please.")

cost = int(input("What did your meal cost before the tip? "))

total = cost * multiplier
print ("You should have tipped the young maiden ${:.2f} for your meal!\n").format(total)

#8
friends = int(input("Oh! you say you were out with frinds though, and that total was split between you? How many friends were you with? "))
friends = friends + 1
serv = raw_input("How well was your service last night at dinner again? good, fair, or bad? ")
if (serv.upper() == 'GOOD'):
    multiplier = .2
elif (serv.upper() == 'FAIR'):
    multiplier = .15
elif (serv.upper() == 'BAD'):
    multiplier = .1


cost = int(input("What did your meal cost before the tip again? "))

total = ((cost/friends)+(cost%friends)) * multiplier
print ("You should have tipped the young maiden ${:.2f} for your meal!\n").format(total)

#9
print ("Before you go, have you heard me count to 10 before? It's really quite a show, trust me. Here goes\n")
i = 1
while (i < 11):
    print i
    i = i + 1

#10
print ("\nLast things last, I want to give you some money. Why? Because I'm a nice guy thats why!!!")
answer = raw_input("So, do you want a coin? Yes or no?")
count = 0
def gimme(count):
    answer = raw_input("Do you want another? ")
    if (answer.upper() == "YES"):
        count = count + 1
        gimme(count)
    else:
        print ("Have fun with your " + str(count) + " coins! Don't spend them all in one place!")
if (answer.upper() == "YES"):
    count = count + 1
    gimme(count)
else:
    priomnt ("Well fine then!")


