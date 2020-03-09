''' Словари. Dictionary.
«Самое частое слово» "The most frequent word". 
by Natalia Sashnikova.
Дан текст: в первой строке задано число строк, далее идут сами строки. 
Выведите слово, которое в этом тексте встречается чаще всего. 
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.'''


d = {}
for i in range(int(input())):
    for word in input().split():
        d[word] = d.get(word, 0) + 1

for i in sorted(d.items(), key=lambda x: (x[0])): #(i[0]-->keys, i[1]-->values)    
    if i[1] == max(d.values()):
        print(i[0])
        break
