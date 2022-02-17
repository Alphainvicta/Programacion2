#cuatro articulos (el, la, los, las)
#el sujeto sigue despues
#el verbo sigue despues
#el predicado sigue despues
#todas las oraciones deben tener estas cuatro cosas
import random

class Oracion():
  def __init__(self, articulo, sujeto, verbo, predicado):
    self.articulo = articulo
    self.sujeto = sujeto
    self.verbo = verbo
    self.predicado = predicado

    self.articulos()
    self.sujetos()
  
  def articulos(self):
    lista_articulo = ['el', 'la', 'los', 'las']
    while True:
      if any(i in self.articulo for i in lista_articulo) == False:
        print('no se ha introducido un articulo correcto')
        self.articulo = input()
      else: break
  
  def sujetos(self):
    while True:
      if self.articulo == 'el' and self.sujeto[(len(self.sujeto) - 1)] != 'o':
        print('no se utilizo de forma correcta el sujeto con el articulo')
        self.sujeto = input()
      if self.articulo == 'la' and self.sujeto[(len(self.sujeto) - 1)] != 'a':
        print('no se utilizo de forma correcta el sujeto con el articulo')
        self.sujeto = input()
      if self.articulo == 'los' and self.sujeto[(len(self.sujeto) - 2)] != 'o' and self.sujeto[(len(self.sujeto) - 1)] != 's':
        print('no se utilizo de forma correcta el sujeto con el articulo')
        self.sujeto = input()
      if self.articulo == 'las' and self.sujeto[(len(self.sujeto) - 2)] != 'a' and self.sujeto[(len(self.sujeto) - 1)] != 's':
        print('no se utilizo de forma correcta el sujeto con el articulo')
        self.sujeto = input()
      else: break



def nueva_oracion():
  while 1:
    print('ingresa una oracion de 4 palabras iniciando con lo siguiente... el, la los, las')
    print('')
    oracion = input()
    splitoracion = oracion.split()
  
    if len(splitoracion) != 4:
      print('no se han encontrado todos los elementos requeridos, intentalo de nuevo')
    else: 
      noracion =  Oracion(splitoracion[0], splitoracion[1], splitoracion[2], splitoracion[3])
      break
  return noracion
      

def imprimir_oracion(oracion):
    print(oracion.articulo, end=' ')
    print(oracion.sujeto, end=' ')
    print(oracion.verbo, end=' ')
    print(oracion.predicado, end=' ')

oracion1 = nueva_oracion()
oracion2 = nueva_oracion()
oracion3 = nueva_oracion()
oracion4 = nueva_oracion()
roracion = []

lista = [oracion1, oracion2, oracion3, oracion4]

roracion.append(lista[random.randint(0, 3)].articulo)
roracion.append(lista[random.randint(0, 3)].sujeto)
roracion.append(lista[random.randint(0, 3)].verbo)
roracion.append(lista[random.randint(0, 3)].predicado)

imprimir_oracion(oracion1)
print('')
print('')
imprimir_oracion(oracion2)
print('')
print('')
imprimir_oracion(oracion3)
print('')
print('')
imprimir_oracion(oracion4)
print('')
print('')
imprimir_oracion(roracion)
    