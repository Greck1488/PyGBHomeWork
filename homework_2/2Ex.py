#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def Count():
    i = 1
    while i < n:
        j = i * (1 + i)
        i = i + 1
    print(j)


n = int(input("Введи число, до которого нужно посчитать произведения: "))
N_result = Count()
input("Press Enter to exit")
