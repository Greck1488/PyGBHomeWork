# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. 

def Formula_I():
    num = int(input("Введи целое число:"))
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print("Сумма цифр целого числа равна: ", sum)
    return sum
    

def Formula_F():
    num = (float(input("Введи вещественное число:")))
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    print("Сумма цифр вещественного числа равна: ", sum)

I_num = Formula_I()
F_num = Formula_F()

input("Press Enter to exit")