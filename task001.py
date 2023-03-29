# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: 
# an= a1 + (n-1) * d.
# Каждое число вводится с новой строки.

start = int(input('Введите первое число прогресии: '))
step = int(input('Введите разность арефметической прогрессии: '))
size = int(input('Введите размер списка генерации: '))

progression = [start]
second_position = start+step
for i in range(size):
    second_position = second_position+step
    progression.append(second_position)
print('Арефметическая прогрессия числа:', [step], 'в диапозоне от числа:', [start])
print(progression)