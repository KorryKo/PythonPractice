''' Словари. Dictionary
В единственной строке записан текст. 
Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов или символами конца строки '''

A = {}
for w in input().split():
    A[w] = A.get(w, 0) + 1
    print(A[w] - 1, end=' ')

''' В словарях существует метод .get(). В обычном случае, если вы вызываете несуществующий ключ name_dict['key'], вы получите исключение KeyError. Однако, если вызвать ключ через метод d.get('key'), то исключения не будет и, если ключа нет, то словарь возвратит None. Если вы хотите назначить переменную вместо отсутствующего ключа, то можно назначить второй параметр: d.get('key', 0).

Лучше всего это применять при переборе числовых ключей:
A[w] = A.get(w, 0) + 1 '''
