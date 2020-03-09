s = input()
y = s.find(' ')
print(s[y+1:] + s[y] + s[:y])
