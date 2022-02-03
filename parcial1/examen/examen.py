while 1:
  x = int(input('ingrese un numero impar: '))
  print('')
  if x % 2 != 0:
    y = x
    break
  else:
    print('el numero ingresado no es impar')
    print('')

matrix = [[False for i in range(x)] for j in range(y)]

def print_matrix():
  for i in range(x):
        for j in range(y):
            print(matrix[i][j], end=" ")
        print()

def diagonal():
  for i in range(x):
        for j in range(y):
          if i == j:
            matrix[i][j] = True

def cruz():
  n = x / 2 - .5
  for i in range(x):
        for j in range(y):
          if j == n or i == n:
            matrix[i][j] = True

def equis():
  l = x - 1
  for i in range(x):
        for j in range(y):
          if i == j:
            matrix[i][j] = True
          if j == l:
            matrix[i][j] = True
        l -= 1

print('matriz inicial')
print('')
print_matrix()
diagonal()
print('')
print('matriz diagonal')
print('')
print_matrix()
matrix = [[False for i in range(x)] for j in range(y)]
cruz()
print('')
print('matriz en cruz')
print('')
print_matrix()
matrix = [[False for i in range(x)] for j in range(y)]
equis()
print('')
print('matriz en equis')
print('')
print_matrix()