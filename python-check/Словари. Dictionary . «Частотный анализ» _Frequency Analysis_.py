''' Словари. Dictionary
by Nataliya Sashnikova.
«Частотный анализ» "Frequency Analysis".
Дан текст: в первой строке записано количество строк в тексте, а затем сами строки. 
Выведите все слова, встречающиеся в тексте, по одному на каждую строку. 
Слова должны быть отсортированы по убыванию их количества появления в тексте, 
а при одинаковой частоте появления — в лексикографическом порядке.
Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова. 
Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: 
частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. 
Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу, 
а если они равны — то по второму. Это почти то, что требуется в задаче.
исходные данные:
9
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme '''

d = {}
for i in range(int(input())):
    for word in input().split():
        d[word] = d.get(word, 0) + 1 # в словарь добавляется последнее значение суммы
  
for i in sorted(d.items(), key=lambda x:(-x[1],x[0])): 
    print(i[0])
    
#Since your "values" are numeric, you can easily reverse the sort order by changing the sign.
#In other words, this sort puts things in order by value (-x[1]) 
#(the negative sign puts big numbers first) and then for numbers which are the same, 
#it orders according to key (x[0]).
