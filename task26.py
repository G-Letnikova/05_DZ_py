# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии

num = input('введите числа m и n: ').split()
# print(num)
n, m = [int(i) for i in num]


def stepen(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b > 1:
        return a * stepen(a, b - 1)
    if b < 0:
        return 1 / a * stepen(a, b + 1)


print(stepen(n, m))
