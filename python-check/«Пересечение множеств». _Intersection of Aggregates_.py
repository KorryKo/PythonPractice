# Множества. Aggregates. Natalia Sashnikova
# «Пересечение множеств». "Intersection of Aggregates"
# Даны два списка чисел
# Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания


a = list(set([int(j) for j in input().split()]) & set([int(j) for j in input().split()]))
for elem in sorted(a): # нашла ошибку через 2 года )
    print(elem, end=' ')
