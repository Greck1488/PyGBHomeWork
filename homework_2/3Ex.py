#Реализуйте алгоритм перемешивания списка. 
# Список размерностью 10 задается случайными целыми числами, выводится на экран, затем перемешивается, опять выводится на экран.
## Я не понял как делать без шаффла =(
 
list = ['Russke', '442', '25/17', 'FraEr04ek', 'Li$t', 'False', 'qwerty ']
print(list) 

import random
random.shuffle(list)
print('mixed list: ')
print(list) 

input("END")