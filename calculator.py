num1 = float(input())
num2 = float(input())
toDo = str(input())
if toDo == '+':
    print(num1 + num2)
elif toDo == '-':
    print(num1 - num2)
elif toDo == '/':
    if num2 ==0:
        print('Деление на 0!')
    else:
        print(num1 / num2)

elif toDo == '*':
    print(num1 * num2)
elif toDo == 'mod':
    if num2 ==0:
        print('Деление на 0!')
    else:
        print(num1 % num2)
elif toDo == 'pow':
    print(num1 ** num2)
elif toDo == 'div':
    if num2 ==0:
        print('Деление на 0!')
    else:
        print(num1 // num2)