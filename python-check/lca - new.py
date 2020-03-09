d = {} # build the dictionary
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    d[child] = parent
def f(x, d): # create a function to be used as many times as needed
    list = [x]
    while x: # while child has his direct parent (the same as --> while x in d: - or- --> while x in d.keys():):
        try:
            x = d[x] # a child becomes a parent - down to the root
            list.append(x) # all existing parents
        except KeyError:
            break
    return list
    
m = int(input())
for i in range(m):
    a1, a2 = input().split()
    for a in f(a2, d): # for every data in a list
        if a in f(a1, d): # for every data in a list
            print(a)
            break
