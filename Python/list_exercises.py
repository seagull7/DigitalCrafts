#1- Given an list of numbers, print their sum. When I say given something, 
# just make something up and store it in a variable.
def psum(list):
    total = 0
    for num in list:
        total += num
    return total
lst = [1, 2, 3, 4]
print psum(lst)

#2- Given an list of numbers, print the largest of the numbers.
def plarge(list):
    max = list[0]
    for num in list:
        if (num > max):
            max = num
    return max
lst = [1, 2, 8, 4]
print plarge(lst)

#3- Given an list of numbers, print the smallest of the numbers.
def plarge(list):
    max = list[0]
    for num in list:
        if (num > max):
            max = num
    return max
lst = [1, 2, 8, 4]
print plarge(lst)

#4- Given an list of numbers, print each number in the list that is even.
def peven(list):
    nlst = []
    for num in list:
        if (num % 2 == 0):
            nlst.append(num)
    return nlst
lst = [1, 2, 8, 4, 5]

for num in peven(lst):
    print num

#5- Given an list of numbers, print each number in the list that is greater than zero.
def ppgzero(list):
    nlst = []
    for num in list:
        if (num > 0):
            nlst.append(num)
    return nlst
lst = [1, 2, -8, 4, 5, -2 ,-3]
for num in pgzero(lst):
    print num

#6- Given an list of numbers, create a new list which contains every 
# number in the given list which is positive.
def ppositive(list):
    nlst = []
    for num in list:
        if (num > 0):
            nlst.append(num)
    return nlst
lst = [1, 2, -8, 4, 5, -2 ,-3]
nlst = ppositive(lst)

#7- Given an list of numbers, and a single factor (also a number), 
# create a new list consisting of each of the numbers in the first 
# list multiplied by the factor. Print this list.
def ppositive(list,factor):
    nlst = []
    for num in list:
        nlst.append(num * factor)
    return nlst
lst = [1, 2, -8, 4, 5, -2 ,-3]
factor = 3
print (ppositive(lst, factor))

#8- Given two lists of numbers of the same length, create a new list 
# by multiplying the pairs of numbers in corresponding positions in the two lists.
def pmult(list,list2):
    if (len(list) == len(list2)):
        nlst = []
        for num in range(len(list)):
            nlst.append(list[num]*list2[num])

        return nlst
lst = [1, 2, -8, 4, 5, -2 ,-3]
lst2 = [2, 3, 4, 5, -1, -2, -3]
print (pmult(lst, lst2))

#9- Given two two-dimensional lists of numbers of the size 2x2 two 
# dimensional list is represented as an list of lists: Calculate the 
# result of adding the two matrices. The number in each position in 
# the resulting matrix should be the sum of the numbers in the corresponding 
# addend matrices. 
def pmadd(list,list2):
    for i in range(len(list)):
        for j in range(len(list)):
            print(list[i][j]+list2[i][j])
lst = [[1, 2], [-8, 4]]
lst2 = [[2, 3], [4, 5]]
pmadd(lst, lst2)

#10- Use your solution in Matrix Addition, and extend it to work for a 
# pair of matrices of any size, as long as they have the same size.
def pmadd(list,list2):
    for i in range(len(list)):
        for j in range(len(list)):
            print(list[i][j]+list2[i][j])
lst = [[1, 2], [-8, 4]]
lst2 = [[2, 3], [4, 5]]
pmadd(lst, lst2)

#11- Given an list of numbers or strings, create a new list containing 
# the same elements as the first list, except with any duplicate values 
# removed. Print the list.
a = [1, 3, 5, -6]
b = []
    for i in a:
        if i not in b:
            b.append(i)


#12- Given two two-dimensional lists of numbers of the size 2x2 - calculate 
# the result of multiplying the two matrices. Print the resulting matrix. 
def pmadd(list,list2):
    a = (list[0][0] * list2[0][0]) + (list[0][1]*list2[1][0])
    b = (list[0][0] * list2[0][1]) + (list[0][1]*list2[1][1])
    c = (list[1][0] * list2[0][0]) + (list[1][1]*list2[1][0])
    d = (list[1][0] * list2[0][1]) + (list[1][1]*list2[1][1])
    nlist = [[a, b], [c, d]]
    return nlist
lst = [[2, -2], [5, 3]]
lst2 = [[-1, 4], [7, -6]]
print (pmadd(lst, lst2))

