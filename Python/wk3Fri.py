#1
import math
for i in range(1000):
    for j in range(1000):
        for k in range (1000):
            if (i < j < k):
                if (i + j + k == 1000):
                    if (math.pow(i, 2) + math.pow(j, 2) == math.pow(k, 2)):
                        print i
                        print j
                        print k
                        break

#2
a = raw_input("Give string")
b = raw_input("Give sting with extra char")
for i in b:
    if (i not in a):
        print i