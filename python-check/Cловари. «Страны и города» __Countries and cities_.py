''' Словари. Dictionary
by Nataliya Sashnikova.
«Страны и города» ""Countries and cities".
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

исходные данные:
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod '''

d = {}
for i in range(int(input())):
    country, *city = input().split() # * - объединение элементов
    d[country] = city
list2 = []
for j in range(int(input())):
    city = input()
    list2.append(city)
    for key, value in d.items():
        if list2[j] in value:
            print(key)
