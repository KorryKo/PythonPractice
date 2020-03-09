''' coded by Nataliya Sashnikova. not a draft
Input data:
Ivanov paper 10
Petrov pens 5
Ivanov marker 3
Ivanov paper 7
Petrov envelope 20
Ivanov envelope 5

Output data:
Ivanov:
envelope 5
marker 3
paper 17
Petrov:
envelope 20
pens 5 '''


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
    s = {}
    for val in value:
        s[val[0]] = s.get(val[0], 0) + int(val[1])
    for key in sorted(s.keys()):
        print(key, end=" ")
        print(s[key])
