# Дано двузначное число. Определите, входит ли в него цифра 5.
# Попробуйте решить задачу с использованием целочисленного деления и деления с остатком.

x = int(input("Введите двузначное число: "))
if x % 5 == 0 or x // 10 == 5:
    print('В число входит цифра 5')
else:
    print('В число не входит цифра 5')