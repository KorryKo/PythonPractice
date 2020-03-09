# Напишите программу, которая считывает список чисел lst из первой строки и число xx из второй строки,
# которая выводит все позиции, на которых встречается число x в переданном списке lst.
# Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
lst = [int(x) for x in input().split()]
x = int(input())
if x not in lst:
    print('Отсутствует')
else:
    indexes = [i for i, j in enumerate(lst) if j == x]
    for m in indexes:
        print(m, end=' ')