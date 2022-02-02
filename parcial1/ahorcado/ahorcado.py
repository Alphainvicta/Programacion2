palabra_secreta = ['asdf', 'qwertyui', 'zxcvbnmlkjhg']
oportunidades = [30, 20, 10]
lista = []
jugador = ''

while 1:
    x = int(input('elige la dificultad del 1 al 3: '))
    print('')
    if  x > 3 or x < 1:
        print('selecciona una opcion poniendo un numero del 1 al 3...')
        print('')    
    else:
        x -= 1
        break

t = oportunidades[x]
c = 0

for i in range(len(palabra_secreta[x])):
    if i == 1 or i == 3 or i == 5:
        lista.append('*')
        print('*', end=' ')
    else:
        lista.append('_')
        print('_', end=' ')    

print('')
print('')

while 1:
    jugador = str(input())
    if jugador == '*':
        for i,ii in enumerate(palabra_secreta[x]):
            for j, jj in enumerate(lista):
                if j == i and jj == '*':
                    lista[i] = ii
                    c += 1
    else: 
        for i,ii in enumerate(palabra_secreta[x]):
            for j in jugador:
                if j == ii:
                    lista[i] = ii
                    c += 1
    print('')
    if c == 0:
        t -= 1
    c = 0
    if t == 0:
        print('')
        print('fin del juego')
        print('')
        break
    if '_' not in lista:
        print('')
        print('Felicidades ganaste el juego!')
        print('')
        break
    for i in lista:
        print(i, end=' ')
    print('')
    print('')
    print('intentos restantes: ', t)
    print('')
