# Англо-латинский словарь. English-Latin Dictionary.
# by Nataliya Sashnikova
# Выведите соответствующий данному латинско-английский словарь, в точности соблюдая формат входных данных. 
# В частности, первым должен идти перевод лексикографически минимального латинского слова, далее — второго в этом порядке и т.д. 
# Внутри перевода английские слова должны быть также отсортированы лексикографически.


e_l = {}
l_e = {}
for i in range(int(input())):
    eng, *lats = input().replace(',', '').split()
    e_l[eng] = lats
    for lat in lats:
        if lat in lats:
            l_e[lat] = l_e.get(lat, []) + [eng] #создаем значения латинско-английского словаря
            l_e.pop("-", None)
print(len(l_e))
for lat in sorted(l_e.keys()):
    print(lat, end=" - ")
    print(*l_e[lat], sep=", ")
