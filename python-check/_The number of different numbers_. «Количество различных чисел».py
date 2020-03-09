# Множества. Aggregates. Natalia Sashnikova
# "The number of different numbers". «Количество различных чисел»
# Дан список чисел. 
# Определите, сколько в нем встречается различных чисел.
# Примечание. Эту задачу на Питоне можно решить в одну строчку.

print(len(set([int(i) for i in input().split()])))
