# Напишите программу, которая принимает на вход координаты точки (X и Y)
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 

x = int(input("Введите число абциссы Х\n"))
y = int(input("Введите число ординаты Y\n"))

print("Итак, по ТЗ нам надо узнать к какой плоскости относится точка...")
if x > 0 and y > 0:
    print("и Абцисса и Ордината, положительные. Значит точка в плоскости №1" )
elif x < 0 and y > 0:
    print("Абцисса меньше чем 0. Но ордината больше чем 0. Значит точка в плоскости №2"  )
elif x > 0 and y < 0:
    print("Абцисса больше чем 0. Но ордината меньше чем 0. Значит точка в плоскости №2"  )
elif x < 0 and y < 0:
    print("и Абцисса и Ордината, положительные. Значит точка в плоскости №3"  )
else:
    print("Итак, напомню правило №1 - Когда говорят введите число, вводи число умник! P.S. 0 это исключение")

print(input("Для выхода нажмите Enter"))