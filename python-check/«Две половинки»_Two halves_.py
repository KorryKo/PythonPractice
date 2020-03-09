s = input()
x = len(s)
l1 = x - x // 2
print(s[l1:] + s[:l1])
