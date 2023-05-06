import math 
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
import pandas
import random 

# Autor: Juan David Vega
# Fecha de creación: 26 de abril de 2023

# Aquí comienza el código

print('''
1. Construir un numero que lea un entero mayor a 2.
2. Vectores aleatorios
3. Vectores ordenados
4. Regresión lineal 
5. Multiplicación de matrices
6. Cambiar la base de un numero

''')
conf = int(input("Introduzca el punto del taller que desea visualizar: "))

if conf == 1:
    #PUNTO NUMERO 1 

    #Construir un programa que lea un número entero mayor que 2 y devuelva 
    #como resultado el número primo de valor más cercano, en este caso, menor o igual 
    #al numero leído. 

    #Entrada, el numero debe ser entero

    n = input("Introduzca el número: ")

    #Verificar si el numero es entero o flotante. En caso de obtener true manda q es entero, en caso de
    #no, manda a que es float
    if n.isdigit():
        num = int(n)
        print("El numero es entero")

    #El numero tiene que ser mayor a dos
        if num > 2:
    #Verificar los numeros primos
            list1 = []
            list2 = []
            prime = []
            primesub = []
            for i in range(num, 0, -1):
                list1.append(i)
            for j in range(2, num+1):
                list2.append(j)
            for k in list1:
                for z in list2:
                    num = k%z
                    if num == 0:
                     primesub.append(k)
    #Se añaden todos los modulos de operaciones, solamente los numeros que se repiten 2 veces
    #serán aquellos que tienen cociente 0, esto es cuando se dividen entre 1 y ellos mismos. 
            for w in primesub:
                count = primesub.count(w)
                if count <= 1:
                    prime.append(w)
    #Aqui se obtienen los primos, ahora eliminar los repetidos de la lista 
            nprime = list(set(prime))
    #Ordenamos de menor a mayor
            nprimeorder = sorted(nprime, reverse=False)
    #El ultimo valor de la lista será el numero primo mas cercano al valor introducido 
            lastprimevalue = nprimeorder[-1]
            
    #print(list1)
    #print(list2)
    #print(primesub)
    #print(nprimeorder)
    print('El numero primo mas cercano a', n, 'Es: ', lastprimevalue)

if 2 == conf:
    #PUNTO 2 TALLER

    #Tomar el numero n entero positivo 
    #n = input("Introduzca el número: ")
    n = '5'
    if n.isdigit():
        num = int(n)
        print("El numero es entero")
        if num > 0: 
            print('El numero es positivo')
    #El programa debe generar n valores. asi que: 
            values = []
            for i in range(0, num):
                ran = random.randint(0,10)
                values.append(ran)
    #Convertir los valores a vector
            vector = np.asarray(values)
    #Encontrar media de los elementos 
            average = np.mean(vector)
    #Encontrar los valores del vector mayores a la media y guardarlos en otro vector
            values2 = []
            vector2 = np.asarray(values2)
            for k in vector:
                if k > average:
                    vector2 = np.append(vector2, k)

    #3 HACER QUE LOS ELEMENTOS ESTEN ORDENADOS DE MAYOR A MENOR
            vector2ord = np.sort(vector2)

    print(values)
    print(vector)
    print(average)
    print(vector2)
    print(vector2ord)
    '''

    '''
if 4 == conf:
    #4 CALCULAR LA REGRESION LINEAL CON DOS LISTAS DE DATOS X, Y 

    x = [1,2,3,4,5]
    y = [2,3,4,5,6]

    #1 Hallar cantidad de datos (n)
    n = len(x)
    #Hallar sumatoria de x
    sumx = 0
    for i in x:
        sumx = sumx + i
    print(sumx)


    #Hallar la sumatoria cuadrada de x 
    sumx2 = 0
    for i in x:
        sumx2 = sumx2 + i**2

    #Hallar sumatoria de y
    sumy = 0
    for j in y:
        sumy = sumy + j
    print(sumy)


    #Hallar la suma de x * y
    sumxy = 0
    for k in range(len(x)):
        sumxy = sumxy + (x[k]*y[k])
    print(sumxy)

    sumax2 = sumx**2

    #Hallar la pendiente de la recta
    m = (n * sumxy - sumx * sumy) / (n * sumx2 - sumax2)
    #Hallar el intercepto 
    b = (sumy - m * sumx) / n

    #recta 

    m1 = str(m)
    b1 = str(b)

    print('La recta obtenida es: ', 'y = ', m1, 'x', '+', b1)

    #Ahora con python 
    x = np.array([1,2,3,4,5])
    y = np.array([2,3,4,5,6])


    # Ajuste de regresión lineal
    m, b = np.polyfit(x, y, 1)

    # Impresión de la ecuación de la función
    print(f"y = {m:.2f}x + {b:.2f}")
    '''
    '''

if 5 == conf:
    #5 MULTIPLICACION DE MATRICES 

    #DEFINIR FUNCION QUE PERMITA AL USUARIO INTRODUCIR LA MATRIZ QUE DESEE 1 (TODAS LAS OPERACIONES SERAN ENTRE 2 MATRICES)
    #MATRIZ 1
    def getmatrix(m, n):
        A = []
        for i in range(n):
            fila = []
            for j in range(m):
                fila.append(int(input(f"Introducir el valor de la posición ({i + 1},{j + 1}): ")))
            A.append(fila)

        return np.asarray(A)

    #MATRIZ2

    def getmatrix(m1, n1):
        A = []
        for i in range(n1):
            fila = []
            for j in range(m1):
                fila.append(int(input(f"Introducir el valor de la posición ({i + 1},{j + 1}): ")))
            A.append(fila)
        return np.asarray(A)





    #1 Obtener las matrices 

    #MATRIZ1     
    n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
    m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
    mtx1 = getmatrix(m,n)
    print('La matriz 1 es: ', mtx1)
    #MATRIZ 2
    n1 = int(input('Introduzca la cantidad n de filas MATRIZ (2): '))
    m1 = int(input('Introduzca la cantidad m de columnas MATRIZ (2): '))
    mtx2 = getmatrix(m1,n1)
    print('La matriz 2 es: ', mtx2)
    '''
    '''
    mtx1 = np.array([[1,2],[2,3]])
    mtx2 = np.array([[1,2],[3,4]])
    #1 Tiene que cumplirse el "teorema de la dimension", en realidad no es el teorema de la dimension pero
    #asi le dicen algunos, m x n * n x p = m x p

    sha1 = mtx1.shape
    sha2 = mtx2.shape
    n = 2
    m = 2

                #print(sha1[0]) ----> fila
                #print(sha1[1]) ----> columna
                #print(mtx1) -----> Matriz

    if sha1[1] == sha2[0]:
        print('La multiplicacion es posible')

    list = []
    listarray = np.asarray(list)

    print(sha1, sha2)
    #Vamos a definir la multiplicacion, tenemos que multiplicar componente i j y luego sumarlos
    for i in range(sha1[0]):
        list1 = []
        for j in range(sha2[1]):
            valor = 0
            for k in range(sha2[0]):
                print(mtx1[i][j] * mtx2[j][i])
                valor += (mtx1[i,k] * mtx2[k,j])
                list1.append(valor) 
        list.append(list1)
    print('la lista es: ',  list)
    print(list)


if 6 == conf:
    #6 PASAR UN NUMERO A UNA BASE 

    #Lea el numero necesario

    #Tomar el numero n entero positivo 
    #n = input("Introduzca el número n: ")
    #m = input("Introduzca el número m: ")

    b = '4' #Base 
    n = '35' #Numero en base 10
    ncopy = n[:]
    nf = [] #Numero en base b al reves
    nN = ''
    n1 = []
    if n.isdigit():
        num = int(n)
        print("El numero", n, " es entero")
        if num > 0: 
            print('El numero es positivo')
            if b.isdigit():
                base = int(b)
                print("El numero base ", b, 'es entero')
                if base > 0 and base < 10:
                    print('El numero es positivo y menor a 10')
#El siguiente while indica que mientras la division normal entre el numero y la base sea diferente de 0, es decir, lo normal
#mantenga el ciclo
                    while num/base != 0:
#Halla el residuo y lo añade a una lista 
                        nf.append(num%base)
                        print(nf)
                        num = num // base

    #               print('Numero: ', nf)
                    reversenf = nf[::-1]
    #               print(reversenf)
                    nN = "".join(map(str, reversenf))
                    print('El numero:', ncopy, 'en base', base, 'es: ', nN)
