
import numpy as np

#EJERCICIO 1

#El programa debe recibir una matriz del usuario
#def matrix

def getmatrix(m, n):
        A = []
        for i in range(n):
            fila = []
            for j in range(m):
                fila.append(int(input(f"Introducir el valor de la posición ({i + 1},{j + 1}): ")))
            A.append(fila)
        return np.asarray(A)
#Definimos el determinante

def getdet(mtx):
     return np.linalg.det(mtx)

#el tamaño de la matriz será 7 x 7. Son 7 vectores de P6, de la forma ax**6 + bx**5 + cx**4 + dx**3 + ex**2 + fx + G 

#Solicitamos la matriz

mtx = getmatrix(7,7) #---> 7 x 7
print('La matriz introducida es: ', mtx)

#1 VERIFICAR SI EL CONJUNTO DE VECTORES PUEDE SER BASE.

#1.A Verificar independiencia lineal.

det1 = getdet(mtx)
if det1 == 0:
     print("Los vectores no son linealmente independiente")
else:

     print('Verificamos el rango de la base canónica.')
     rangeC = 7 #---> La base canonica de P6 puede represetarse como una matriz 7 x 7 en la que unicamente hay unos en la diagonal. 
     print('El rango de la matriz de vectores canonicos es: ', rangeC)
     print('''En este caso, si los vectores son linealmente independientes y el rango de la matriz de vectores es igual al rango
            de la matriz de vectores canonicos, entonces se cumple la segunda condición. 
     
     ''')
     mtxrank = np.linalg.matrix_rank(mtx)
     print('El rango de la matriz es ', mtxrank)
     confirm =  input('Verificar la igualdad de rangos. [y]: ')
     if 'y' in confirm:
          print('El conjunto de vectores es base del espacio P6.')

#Item 1: El programa debe arrojar el sistema de ecuaciones lineales necesario para determinar si el conjunto es base del espacio vectorial. 

#1 Matriz de coeficientes sera mtx

for i in range(mtx.shape[0]):
     print(f"{mtx[i, 0]}x**6 + {mtx[i, 1]}x**5 {mtx[i, 1]}x**4 + {mtx[i, 1]}x**3 + {mtx[i, 1]}x**2 + {mtx[i, 1]}x+ {mtx[i, 1]}  = 0")