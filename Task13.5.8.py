# Проверьте, все ли элементы в списке являются уникальными.

x = [1, 3, 5, 6, 1]
m = set(x)
if len(x) == len(m):
    print('Все элементы в списке являются уникальными')
else:
    print('Не все элементы в списке являются уникальными')