#1
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print "FizzBuzz"
    elif number % 3 == 0:
        print "Fizz"
    elif number % 5 ==0:
        print "Buzz"
    else:
        print number
#2
sums = 0
for number in range(1, 1001):
    if number % 3 == 0:
        sums += number
    elif number % 5 ==0:
        sums += number

print sums

#3
end = int(input("#? "))


def fib(end):
    num = 0
    result = [1, 2]
    while (result[len(result)-1] < end+1):
        num = result[-1] + result[-2]
        result.append(num)
    result.pop()
    sums = 0
    for i in result:
        if i % 2 == 0:
            sums += i   
    return sums
print fib(end)

#4


