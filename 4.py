# <Задание 4>
# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.


number = int(input('Enter the number:'))
a = ''
while number > 0:
    a = str(number % 2) + a
    number = number // 2
print(a)