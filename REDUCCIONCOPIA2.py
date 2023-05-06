import math
import numpy as np
import pandas as pd
import sympy as sym 
from sympy import symbols
import random
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym 
from sympy import plot_implicit, symbols, Eq, And
from sympy import *
from sympy.plotting import plot_implicit, PlotGrid
import matplotlib.pyplot as plt
import pandas
import random
import time 

# Derechos de autor (c) 2023 [Juan David Vega Jurado].
# Todos los derechos reservados.
# VERSION = 1.1.0

# Este programa es un software de código abierto.
# No obstante, el uso no autorizado de este software está prohibido.
# Este programa solo puede ser utilizado con autorización explícita del propietario y para fines educativos.

# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; incluso sin la garantía implícita de
# COMERCIABILIDAD o APTITUD PARA UN PROPÓSITO PARTICULAR. 

# [Juan David Vega Jurado] no será responsable de los daños
# que se puedan derivar del uso de este software.

# Contacto:
# [Celular: +57 3014688564]
# [Mail: vegajuancho112@gmail.com]

# Fecha de creación: [5/06/2023]
# Última actualización: [5/06/2023]

# Descripción:
# Este programa resuelve sistemas de ecuaciones utilizando [gauss] y grafica las soluciones infinitas con [sympy].

# Nota:
# Este programa está protegido por las leyes de derechos de autor. 
# Queda prohibida la distribución y reproducción no autorizadas del programa.


# Nota código:
# Variedad de funciones están comentadas ya que son utilizadas para comprobaciones rápidas 
# o modificaciones instantáneas en casos particulares, se dejan comentadas con el fin de 
# poder encontrar solución a posibles eventualidades que se puedan presentar. Es importante
# mantener estas líneas para el entendimiento general del código.  


#--- AQUI EMPIEZA EL CODIGO ----

#EJERCICIO NUMERO #2

#Definir la entrada de las matrices
def getmatrix(m, n):
        A = []
        for i in range(n):
            fila = []
            for j in range(m):
                fila.append(float(input(f"Introducir el valor de la posición ({i + 1},{j + 1}): ")))
            A.append(fila)
        return np.asarray(A)

#Definimos la matriz Ac como la matriz de coeficientes y definimos el tamaño de la matriz que el usuario introduce


n = int(input('Introduzca el numero de filas de la matriz de coeficientes: '))
m = int(input('Introduzca el numero de columnas de la matriz de coeficientes: '))
#n = 3
#m = 3

#n= fila
#m = columna --------> Matriz n x m. 

A = getmatrix(m,n)

#A = np.array([[1,2,8], [5,4,7], [3,4,6]]) #--->Ejemplo
C = np.copy(A)
print('Introduzca la matriz de soluciones')
b = getmatrix(1,n)
#b = np.array([[2],[3],[7]]) #---->Ejemplo

B = np.copy(b)
#Concatenamos las variables 
Ab = np.hstack((A, b))
reduct_case = True

#Definir gauss para n x n, definir la reduccion 

def partialgauss(Ab):
    #n = (sym.shape(A[0])) #---> Definimos el tamaño 
    n = len(Ab)
    condition = False
    reduct_case = True

    #Eliminación 
    for i in range(0,n):
        pivote = Ab[i,i] #---> Obtener la componente 1,1 de la matriz. 
        Ab[i, :] = Ab[i,: ] / pivote #---> Dividir toda la fila i por el valor del pivote  

        for k in range(i+1, n): #-->Tomamos la siguiente fila, la fila i ya ha sido reducida
            #print('El value es: ', A[k, i] * A[i, :])
            Ab[k, :] -= Ab[k, i] * Ab[i, :] #--->Restarle la fila i completa
            #print(A[k]) #---> Mostramos en pantalla la fila reducida
            val = 0 #---> Inicializamos variable
            count = 0 #--->Inicializamos contador
            for j in Ab[k]: #--->Vamos a recorrer cada valor de la fila actual
                val = val + j #--->Sumamos todos los valores de la fila
                count += 1 # ---> Aumenta el contador 
                #print('The value is: ', val)
                if count == m: #--->Si el for termina y recorre todos los valores
                    if val == 0: # ---> Y la suma da 0, la fila es de zeros.
                        #print('Se ha encontrado una fila de ceros')
                        condition = True
                        row = k 
                        break
            if condition:
                 break
        if condition:
             break
#Si se encontró una fila de ceros y esta fila no es la ultima, permutar con la fila n

    if condition and row != n-1: #---Si condicion es verdadera y la fila no es la ultima
        Ab[[row, n-1],:] = Ab[[n-1, row], :]
    
    for z in range(1,n-1):
        rowfil = Ab[z]
        val = 0
        count2 = 0
        for u in rowfil:
            val = val + u
            #print('Los values son: ', val)
            count2 += 1
            #print(count)
            if count2 == m:
                if val != 0:
                    print('Se ha encontrado otra fila sin reducir, fila', z)
                    reduct_case = True
                else: 
                    reduct_case = False
                   
    return Ab

count12 = 0
def gauss(Ab): #Se llama la funcion nuevamente y se reduce la matriz. 
    count12 = 0
    n = len(Ab)
    while reduct_case != False and count12 < n - 1:
     A1 = partialgauss(Ab)
     count12 += 1
    return(A1)

if n == 0 or m == 0:
    print('Se han introducido parametros ilegales, el programa se cerrará')
    exit()


if len(A) > 1: #--->Len para filas de la matriz
    V = gauss(Ab)
    print('La matriz original es: ', C )
    print('La matriz de soluciones es: ', B )
    print('La matriz ampliada reducida es: ', V)
else: 
    print('La matriz no se puede reducir, solamente tiene una fila')
    print('La matriz introducida fue ', C)

# Ahora, todo lo construido anteriormente tiene como fin permitirme obtener una reducción 
# como ninguna librería permite, y es obtener la fila o las filas de ceros. Ahora, con esto, convierto en texto
# y obtengo las ecuaciones del sistema infinito o con una solución. 


# Condiciones suficientes para que el codigo tenga solución. ---> Esto va arriba

# Vamos utilizar la reducción que hemos obtenido anteriormente, es decir, se va a comprobar:
# Si en la reducción se encuentra que la suma de los componentes de una fila  z es cero (nxm), y esa suma 
# es igual a un valor diferente de cero que se encuentra en la fila z pero en la columna m + 1, el sistema 
# no tiene solución. 

#LA MATRIZ TIENE QUE SER MAYOR A 1 
if len(A) > 1 and m != 0 and n !=0:

    #Reiniciamos las variables
    row = 0
    val = 0
    count = 0
    not_solution = False


    for z in range(n): #---->En las filas de la matriz
        val = 0
        row = V[z,:m] #---> Toma la fila z y las columnas desde la 0 hasta la m, pero la cuenta inicia desde 1???
        #print('Fila', row)
        bval = V[z,m] #Toma el valor m de la fila z, es raro porque aqui cuando digo m, la cuenta empieza desde 0. 
        #print('Valor b', bval)
                        #Sin embargo, m es el numero de columnas de la matriz de coeficientes, la matriz de solución está 
                        #En la columna m + 1
        count = 0
        for j in row: 
            val = val + j
            #print('Suma', val)
            count += 1
            #print('Contador', count)
            if count == m: #Si completa la suma 
                if val == 0:
                    if bval == 0:
                        #print('CONTIDION ACTIVE')
                        not_solution = False
                    if bval != 0:
                        print('El sistema no tiene solución, la fila ',z, row, 'No es igual a: ', bval)
                        not_solution = True
        if not_solution:
            break     
        
    # Aquí se activa la funcion que detecta si la matriz no tiene solución, entonces, ahi no tiene caso
# Intentar graficar, el codigo se detiene. 

    if not_solution == False: 


        #Separar las variables concatenadas

        #----Definimos que la matriz A tiene tamaño n x m, y la matriz b tiene tamaño n x 1
        #----Entonces, es facil saber que la matriz b estará en la columna m y tendrá n filas
        #----Separarlo no será dificil 

        #Separamos en dos matrices 

        A, b = np.split(V, [m], axis=1) #----La matriz va desde 0 hasta la columna m-1, axis = 1, ya que definimos
                                        #--- Por columnas. 

        print('La matriz de coeficientes reducida es: ', A)
        print('La matriz de solución reducida es: ', b)

        # Imprimir ecuaciones del sistema
        for i in range(len(A)):
            eq = ""
            for j in range(len(A[i])):
                if A[i,j] != 0:
                    eq += f"{A[i,j]}x{j} + "
            eq = eq[:-3]  # Eliminar el último "+ "
            if b[i][0] != 0:
                eq += f"= {b[i][0]}"
            if b[i][0] == 0 and A[i,j] == 1:
                eq += f"= {b[i][0]}"
            print(eq)

        #AREA DE GRAFICAS 

        #MATRICES 2 X 2
        if len(C) == 2:
            #Creamos el sistema de ecuaciones sin el termino lineal. 
            eq_non_b_list = []
            for i in range(len(A)):
                eq_non_b = ""
                const = b[i][0]
                for j in range(len(A[i])):
                    if A[i,j] != 0:
                        eq_non_b += f"{A[i,j]}*x{j} + "
                eq_non_b = eq_non_b[:-3]  # Eliminar el último "+ "
                eq_non_b_list.append(eq_non_b)

            print(eq_non_b_list)

            #Import sympy symbols 
            x0, x1 = sym.symbols('x0 x1')
            #Defino este orden ya que al código se le deben introducir 
            #los datos de esta forma 


            #Equation #1 
            eq1 = eq_non_b_list[0] #----> Ecuacion sin b
            b1eq = b[0][0]
            #Concatenamos las variables de forma negativa para el termino lineal 
            #Es como pasarlo a restar al otro lado 
            eq1full = eq1 + ' ' + str((-1)*(b1eq))
            print(eq1full)

            #Convertir la ecuacion completa str a expresión de sympy
            eq1sym = sym.sympify(eq1full)
            print(eq1sym)
            eq1plot = Eq(eq1sym,0)

            #Se hace necesario definir limites del plot para la grafica de la primera ecuación, asi como 
            #para la segunda, asi que simplemente los añadimos y definimos. 

            #Definimos los limites para la primera ecuacion

            xmin1 = -5
            xmax1 = 5
            ymin1 = -5
            ymax1 = 5

            p1 = plot_implicit(eq1plot, (x0,xmin1,xmax1),  (x1, ymin1, ymax1),show=False, line_color='r')

            #p1 = plot_implicit(eq1plot, show=False, line_color='r')

            #Equation #2

            eq2 = eq_non_b_list[1] #----> Ecuacion sin b
            b2eq = b[1][0]
            #Concatenamos las variables de forma negativa para el termino lineal 
            #Es como pasarlo a restar al otro lado 
            eq2full = eq2 + ' ' + str((-1)*(b2eq))
            print('La segunda ecuacion es: ', eq2full)

            #Convertir la ecuacion completa str a expresión de sympy
            eq2sym = sym.sympify(eq2full)
            print(eq2sym)
            eq2plot = Eq(eq2sym ,0)

            # Definimos los límites de los ejes
            xmin2 = -10
            xmax2 = 10
            ymin2 = -10
            ymax2 = 10

            # Creamos la figura y los ejes
            #fig, ax = plt.subplots()
            # Graficamos la ecuación usando plot_implicit
            #plot_implicit(eq2plot, (x0, xmin, xmax), (x1, ymin, ymax), ax=ax)
            # Mostramos la figura
            #p2 = plot_implicit(eq2plot)

            p1.extend(plot_implicit(eq2plot,(x0, xmin2, xmax2), (x1, ymin2, ymax2),  show=False)) #Exendemos la primer grafica a la segunda
            p1.show()
            #Y bloqueamos la grafica para que no salten dos ventanas


            #Equation 3 interseccion 

            print('Confirm eq1', eq1sym)
            print('Confirm eq2', eq2sym)

            inter = sym.solve((eq1sym,eq2sym), (x0,x1))
            print('sol =', inter)
            #Definimos las coordenadas
            x = inter[x0]
            y = inter[x1]

            print('La solución del sistema de ecuaciones es:', 'x = ',x, 'y = ', y )

    #Solamente se contempla la posibilidad de graficar los sistemas 
elif len(A) == 1 and m != 0 and n != 0: 
        for i in range(len(A)):
            eq = ""
            for j in range(len(A[i])):
                if A[i,j] != 0:
                    eq += f"{A[i,j]}x{j} + "
            eq = eq[:-3]  # Eliminar el último "+ "
            if b[i][0] != 0:
                eq += f"= {b[i][0]}"
            if b[i][0] == 0 and A[i,j] == 1:
                eq += f"= {b[i][0]}"
            print(eq)
        print('La ecuacion de la matriz unidimencional es, ', eq)
 

#quickshort, burbuja, insercion


# NOTA DE CAMBIOS PENDIENTES: 

# GRAFICO DE ECUACIONES CON 3 VARIABLES.