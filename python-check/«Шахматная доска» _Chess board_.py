# Natalia Sashnikova. «Шахматная доска» "Chess board"

# «Даны два числа n и m. 
# Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. 
# В левом верхнем углу должна стоять точка.

n, m = [int(i) for i in input().split()]
a = [['*'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i][j] = '.'
for row in a:
    print(' '.join([elem for elem in row]))
