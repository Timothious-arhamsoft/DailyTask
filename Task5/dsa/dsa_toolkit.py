def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)

def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return Fibonacci(num-1) + Fibonacci(num-2)

def sum_of_num(num):
    result = []
    while num!=0:
        result.append(num%10)
        num = num // 10
    return sum(result)

def recursive_sum_of_num(num):
    if num == 0:
        return 0
    return num%10 + recursive_sum_of_num(num//10)
