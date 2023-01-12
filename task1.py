# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def check_simple(n: int):
    i = 2
    while n % i != 0 or i == n - 1:
        i += 1
    if i == n:
        return n

def simple_numbers(n: int) -> list:
    simple_multipliers = [1]
    for i in range(2, n+1):
        if n % i == 0:
            if check_simple(i) != None:
                simple_multipliers.append(check_simple(i))
            else:
                continue
    return simple_multipliers


n = int(input('Введите натуральное число N: '))
simple_multipliers = simple_numbers(n)
print(simple_multipliers)