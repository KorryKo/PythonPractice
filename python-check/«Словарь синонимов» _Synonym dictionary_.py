'' Словари. Dictionary. 
Nataliya Sashnikova
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.

Входные данные:
10
95UUSA4P3K 140YAZQF1W2
JIGCEL82Y3BXJ 277WMID9GFAWGC
X36U1924TQ GUDPNJ60NR3A
TR7JOPXQ0JK64CM O6BJSY7MHMAI8S
17HZOQO20CDQ1UG VVIPAVTVY202R
8T1A0XRRKKXEV 7L2UKWCJ917G1Q
WLPOJYRN0G3MC 5QWJPM4FG58
Z8TN35IQAF GXUPQY7I3AJCX3
5F382242HD25Q 3IV9JL29DNP64
KZWNAOSV8H8APVF LDAIALO4YMXE7
WLPOJYRN0G3MC '''

n = int(input())
p = dict(input().split() for j in range(n))
k = input()
for key, value in p.items():
    if k == value:
        print(key)
    if k == key:
        print(value)
