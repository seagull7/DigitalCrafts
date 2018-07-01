import matplotlib.pyplot as plt
import math
from numpy import arange

#1- Write a function hello which takes a name parameter and says Hello to the name.
def hello(name):
    print ("Hello, " + name)

#2- Write a function f(x) that returns x + 1 and plot it for x values of -3 to 3 in 
# increments of 1.
def f(x):
    return x+1

xs = list(range(-3, 4))
ys = []

for x in xs:
    ys.append(f(x)) 
plt.plot(xs, ys) 
plt.show()
plt.close()

#3- 
def f(x):
    return x*x

xs = list(range(-5, 6))
ys = []

for x in xs:
     ys.append(f(x)) 
plt.plot(xs, ys) 
plt.show()
plt.close()

#4-
def f(x):
    if (x%2==0):
        return -1
    else:
        return 1

xs = list(range(-5, 6))
ys = []

for x in xs:
     ys.append(f(x)) 
plt.bar(xs, ys) 
plt.show()
plt.close()

#5-
def f(x):
    return math.sin(x)

xs = list(range(-5, 6))
ys = []

for x in xs:
     ys.append(f(x)) 
plt.plot(xs, ys) 
plt.show()
plt.close()

#6-
def f(x):
    return math.sin(x)

xs = arange(-5, 6, 0.1) 
ys = []

for x in xs:
     ys.append(f(x)) 
plt.plot(xs, ys) 
plt.show()
plt.close()

#7-
def celcius_to_fahrenheit(x):
    return (x * 9 /5) + 32

def celcius(x):
    return x
xs = arange(-5, 6, 0.1) 
ys = []
fs = []

for x in xs:
     ys.append(celcius_to_fahrenheit(x))
for x in xs:
    fs.append(celcius(x))
plt.plot(xs, ys, xs, fs) 
plt.show()
plt.close()

#8- 
def again():
    answer = raw_input("do you want to play again? (Y on N)? ")
    if answer == "Y":
        return True
    else:
        return False

#9- 
def again():
    answer = raw_input("Do you want to play again? (Y on N)? ")
    if answer.upper() == "Y":
        return True
    elif answer.upper() == "N":
        return False
    else:
        print ("Inalid answer:")
        again()
