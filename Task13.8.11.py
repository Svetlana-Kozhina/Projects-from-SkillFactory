# Напишите программу, которая на вход принимает последовательность целых чисел, и возвращает True,
# если все числа ненулевые, и False, если хотя бы одно число равно 0.

a = list(map(int, input('Введите последовательность целых чисел: ').split()))
print(all(a))