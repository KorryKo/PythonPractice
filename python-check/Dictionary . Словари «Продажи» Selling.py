# Nataliya Sashnikova
# Пробное решение (черновик), заменено на другое
''' Входные данные 
Ivanov aaa 1
Petrov aaa 2
Sidorov aaa 3
Ivanov aaa 6
Petrov aaa 7
Sidorov aaa 8
Ivanov bbb 3
Petrov bbb 7
Sidorov aaa 345
Ivanov ccc 45
Petrov ddd 34
Ziborov eee 234
Ivanov aaa 45 '''


d = {}
while True:
    try:
        l = input()
        key, *value = l.split()
        if key in d:
            d[key].append(value)
        else:
            d[key] = [value]
     # Loop continuously
    except EOFError:
        #print ("Error: EOF or empty input!")
        l == ""
        break
for key, value in sorted(d.items()):
    print(key +":")
    a = int(value[0][1])
    value1 = {}
    s = {}
    for val in value: # val - слово в значении value   
        value1[val[0]] = val[1]
        if val[0] in s.keys():
            s[val[0]] = val[1]
            a = int(a) + int(val[1])
            s[val[0]] = a
            value1.update(s)
        else:
            s[val[0]] = val[1]
            value1[val[0]] = val[1]
    for key in sorted(value1.keys()):
        print(key, end=" ")
        print(value1[key])
        
'''  Выходные данные
Ivanov:
aaa 52
bbb 3
ccc 45
Petrov:
aaa 9
bbb 7
ddd 34
Sidorov:
aaa 356
Ziborov:
eee 234 '''       
        
