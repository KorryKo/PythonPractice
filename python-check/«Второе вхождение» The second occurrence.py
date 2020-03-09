s = input()
k = 0
for i in range(len(s)):
    if s[i] == 'f':
        k += 1 # если встречается первое f: к=1; когда следующее f-добавляется +1 
        if k == 2: # когда нашлось два f, выводится значение индекса
            print(i)
if (s.count('f')) == 1:
    print (-1)
if (s.count('f')) == 0:
    print (-2)
