import random
import copy

class Dungeon:
    def __init__(self):
        self.randsize()
        self.generateroom()
        self.cleanroom()
        self.setdoor()
        self.setchest()
        self.setenemy()
        self.setplayer()

    def randsize(self):
        self.x = random.randint(4, 10)
        self.y = random.randint(4, 10)

    def generateroom(self):
        choicelist = ['█', '░']
        self.room = [[random.choice(choicelist) for i in range(self.x)] for j in range(self.y)]
    
    def cleanroom(self):
        for i in range(0, self.x, 2):
            for j in range(0, self.y, 2):
                if self.room[j][i] == 0:
                    self.room[j][i] = 1
    
    def setdoor(self):
        rancoordx = random.randint(0, self.x - 1)
        rancoordy = random.randint(0, self.y - 1)
        self.room[rancoordy][rancoordx] = 'D'
        self.door = [rancoordy, rancoordx]
    
    def setchest(self):
        rancoordx = random.randint(0, self.x - 1)
        rancoordy = random.randint(0, self.y - 1)
        while rancoordx == self.door[1] and rancoordy == self.door[0]:
            rancoordx = random.randint(0, self.x - 1)
            rancoordy = random.randint(0, self.y - 1)
        self.room[rancoordy][rancoordx] = 'C'
        self.chest = [rancoordy, rancoordx]
        self.chest_open = 1
    
    def setenemy(self):
        self.enemies = random.randint(2,5)
        for x in range(self.enemies):
            rancoordx = random.randint(0, self.x - 1)
            rancoordy = random.randint(0, self.y - 1)
            while rancoordx == self.door[1] and rancoordy == self.door[0] or rancoordx == self.chest[1] and rancoordy == self.chest[0]:
                rancoordx = random.randint(0, self.x - 1)
                rancoordy = random.randint(0, self.y - 1)
            self.room[rancoordy][rancoordx] = 'E'
    
    def setplayer(self):
        rancoordx = random.randint(0, self.x - 1)
        rancoordy = random.randint(0, self.y - 1)
        while rancoordx == self.door[1] and rancoordy == self.door[0] or rancoordx == self.chest[1] and rancoordy == self.chest[0]:
            rancoordx = random.randint(0, self.x - 1)
            rancoordy = random.randint(0, self.y - 1)
        self.croom = copy.deepcopy(self.room)
        self.croom[rancoordy][rancoordx] = 'P'
        self.player = [rancoordy, rancoordx]
    
dungeon = Dungeon()
bombs = 10
hearts = 10
level = 1

def print_room():
    print()
    for i in range(dungeon.y):
        print('              ', end='')
        for j in range(dungeon.x):
            print(dungeon.croom[i][j], end=' ')
        if i == (dungeon.y / 2) - 1:
            print('              pisos bajados: ', level, end='')
        if i + .5 == (dungeon.y / 2):
            print('              pisos bajados: ', level, end='')
        print()
    print()

def chest_luck():

    if dungeon.chest_open == 1:
        x = random.randint(0, 5)
        if x == 1:
            print('encontraste ', x, 'bomba')
            print('')
        else:
            print('encontraste ', x, 'bombas')
            print('')
    
    else:
        print('el cofre ya fue abierto')
        print('')
        x = 0

    dungeon.chest_open = 0

    return x

def fight(hearts):
    r1 = random.randint(0,4)
    r2 = random.randint(5,10)
    vhearts = r2 - r1

    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('comienza el combate!')
    print('')
    mchoose = random.randint(r1,r2)
    print('predice el mismo numero que tu enemigo entre ', r1, ' y ',  r2, ': ')
    print('')
    pchoose = int(input())
    print('')

    while mchoose != pchoose:
        hearts -= 1
        if hearts == 0:
            print('has muerto')
            print('')
            result = 0
            break
        print('perdiste un corazon, corazones restantes: ', hearts)
        print('')
        print('predice el mismo numero que tu enemigo entre ', r1, ' y ',  r2, ': ')
        print('')
        pchoose = int(input())
        print('')
        

    if mchoose == pchoose:
        print('derrotaste a tu enemigo! ganaste',  vhearts, 'corazones')
        print('')
        hearts += vhearts
        result = 1

    print('se acabo el combate!')
    print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')

    return result, hearts

print_room()

while 1:
    print('bombas disponibles: ', bombs, ' enemigos restantes: ', dungeon.enemies, ' corazones restantes: ', hearts)
    print('')
    print('a donde quieres mover el jugador?')
    print('')
    mov = str.lower(input('arriba (w), izquierda (a), abajo (s), derecha (d): '))
    print('')

    if mov == 'w':
        if dungeon.player[0] == 0:
                print('ya te encuentras al final del cuarto')
                print('')
        else:
            if dungeon.croom[dungeon.player[0] - 1][dungeon.player[1]] == 'E':
                result, hearts = fight(hearts)
                if result == 0:
                    print('')
                    print('Fin del juego')
                    break
                if result == 1:
                    dungeon.croom[dungeon.player[0] - 1][dungeon.player[1]] = '░'
                    dungeon.enemies -= 1

            if dungeon.croom[dungeon.player[0] - 1][dungeon.player[1]] == 'C':
                bombs += chest_luck()

            if dungeon.croom[dungeon.player[0] - 1][dungeon.player[1]] == 'D':
                if dungeon.enemies == 0:
                    dungeon = Dungeon()
                    level += 1
                else:
                    print('la puerta esta bloqueada, derrota a todos los enemigos restantes para poder pasar')
                    print('')

            if dungeon.croom[dungeon.player[0] - 1][dungeon.player[1]] == '█':
                if bombs == 0:
                    print('no quedan mas bombas para usar')
                    print('')
                else:
                    dungeon.croom[dungeon.player[0] - 1][dungeon.player[1]] = '░'
                    bombs -= 1

            if dungeon.croom[dungeon.player[0] - 1][dungeon.player[1]] == '░': 
                print('el jugador avanza hacia arriba')
                print('')
                dungeon.player[0] -= 1
                dungeon.croom[dungeon.player[0] + 1][dungeon.player[1]] = '░'
                dungeon.croom[dungeon.player[0]][dungeon.player[1]] = 'P'
                
                    
    if mov == 'a':
        if dungeon.player[1] == 0:
                print('ya te encuentras al final del cuarto')
                print('')
        else:
            if dungeon.croom[dungeon.player[0]][dungeon.player[1] - 1] == 'E':
                result, hearts = fight(hearts)
                if result == 0:
                    print('')
                    print('Fin del juego')
                    break
                if result == 1:
                    dungeon.croom[dungeon.player[0]][dungeon.player[1] - 1] = '░'
                    dungeon.enemies -= 1

            if dungeon.croom[dungeon.player[0]][dungeon.player[1] - 1] == 'C':
                bombs += chest_luck()

            if dungeon.croom[dungeon.player[0]][dungeon.player[1] - 1] == 'D':
                if dungeon.enemies == 0:
                    dungeon = Dungeon()
                    level += 1
                else:
                    print('la puerta esta bloqueada, derrota a todos los enemigos restantes para poder pasar')
                    print('')

            if dungeon.croom[dungeon.player[0]][dungeon.player[1] - 1] == '█':
                if bombs == 0:
                    print('no quedan mas bombas para usar')
                    print('')
                else:
                    dungeon.croom[dungeon.player[0]][dungeon.player[1] - 1] = '░'
                    bombs -= 1

            if dungeon.croom[dungeon.player[0]][dungeon.player[1] - 1] == '░':   
                print('el jugador avanza hacia la izquierda')
                print('')
                dungeon.player[1] -= 1
                dungeon.croom[dungeon.player[0]][dungeon.player[1] + 1] = '░'
                dungeon.croom[dungeon.player[0]][dungeon.player[1]] = 'P'
    
    if mov == 's':
        if dungeon.player[0] == dungeon.y - 1:
                print('ya te encuentras al final del cuarto')
                print('')
        else:
            if dungeon.croom[dungeon.player[0] + 1][dungeon.player[1]] == 'E':
                result, hearts = fight(hearts)
                if result == 0:
                    print('')
                    print('Fin del juego')
                    break
                if result == 1:
                    dungeon.croom[dungeon.player[0] + 1][dungeon.player[1]] = '░'
                    dungeon.enemies -= 1

            if dungeon.croom[dungeon.player[0] + 1][dungeon.player[1]] == 'C':
                bombs += chest_luck()

            if dungeon.croom[dungeon.player[0] + 1][dungeon.player[1]] == 'D':
                if dungeon.enemies == 0:
                    dungeon = Dungeon()
                    level += 1
                else:
                    print('la puerta esta bloqueada, derrota a todos los enemigos restantes para poder pasar')
                    print('')

            if dungeon.croom[dungeon.player[0] + 1][dungeon.player[1]] == '█':
                if bombs == 0:
                    print('no quedan mas bombas para usar')
                    print('')
                else:
                    dungeon.croom[dungeon.player[0] + 1][dungeon.player[1]] = '░'
                    bombs -= 1

            if dungeon.croom[dungeon.player[0] + 1][dungeon.player[1]] == '░':
                print('el jugador avanza hacia abajo')
                print('')
                dungeon.player[0] += 1
                dungeon.croom[dungeon.player[0] - 1][dungeon.player[1]] = '░'
                dungeon.croom[dungeon.player[0]][dungeon.player[1]] = 'P'
    
    if mov == 'd':
        if dungeon.player[1] == dungeon.x - 1:
                print('ya te encuentras al final del cuarto')
                print('')
        else:
            if dungeon.croom[dungeon.player[0]][dungeon.player[1] + 1] == 'E':
                result, hearts = fight(hearts)
                if result == 0:
                    print('')
                    print('Fin del juego')
                    break
                if result == 1:
                    dungeon.croom[dungeon.player[0]][dungeon.player[1] + 1] = '░'
                    dungeon.enemies -= 1

            if dungeon.croom[dungeon.player[0]][dungeon.player[1] + 1] == 'C':
                bombs += chest_luck()

            if dungeon.croom[dungeon.player[0]][dungeon.player[1] + 1] == 'D':
                if dungeon.enemies == 0:
                    dungeon = Dungeon()
                    level += 1
                else:
                    print('la puerta esta bloqueada, derrota a todos los enemigos restantes para poder pasar')
                    print('')

            if dungeon.croom[dungeon.player[0]][dungeon.player[1] + 1] == '█':
                if bombs == 0:
                    print('no quedan mas bombas para usar')
                    print('')
                else:
                    dungeon.croom[dungeon.player[0]][dungeon.player[1] + 1] = '░'
                    bombs -= 1

            if dungeon.croom[dungeon.player[0]][dungeon.player[1] + 1] == '░':
                print('el jugador avanza hacia la derecha')
                print('')
                dungeon.player[1] += 1
                dungeon.croom[dungeon.player[0]][dungeon.player[1] - 1] = '░'
                dungeon.croom[dungeon.player[0]][dungeon.player[1]] = 'P'
    
    if dungeon.enemies == 0:
        print('no quedan mas enemigos en el cuarto, la puerta se ha abierto!')
        print('')

    print_room()
    print('')
