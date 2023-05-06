from logging import critical
import numpy as np
import matplotlib.pyplot as plt
import math 
from sympy import * 


funcion = input("Introduzca la funcion, recuerde el formato: ")

def f(x): 
    funcion1 = eval(funcion)
    return funcion1

x,y = symbols("x y")
derivative = diff(f(x),x)
derivative = str(derivative)
print(type(derivative))

def df(x):
    derivative1 = eval(derivative)
    return derivative1

a = float(input("Introduzca el [a] invervalo donde se encuentran las raices: "))
b = float(input("Introduzca el valor [b]: "))
#por derecha obligatoriamente
x0 = float(input("Introduzca el valor arbitrario para iniciar el método: "))
#error = float(input("Introduzca el error, el formato es [1e-10]: "))
error = 1e-10

#grafica
"""
Una grafica con dos barreras de color rojo que delimiten el intervalo 
mencionar que las barreras son los intervalos a analizar
"""
#confirmacion del usuario para iniciar el proceso#
#mencione que tiene q cerrar la grafica
#ha visualizado las raices? [y][n]

#meta todo en un if que confirme todo

n = 40
criticsdots = solve(Eq(df(x),0))
print("Los puntos críticos generales son:", criticsdots)
#se crea una lista vacía que almacenará los puntos críticos que pertenecen al intervalo
criticsdotsininterval = []
#ANALIZA LOS PUNTOS CRITICOS QUE PERTENECEN AL INTERVALO

for i in criticsdots:
    if i>= a and i<= b: #si el valor i es mayor o igual a a y a su vez es menor o igual a b entonces 
        criticsdotsininterval+= [i] #la lista que estaba vacia  se va llenando con los valores i de la lista de puntos criticos
                                        #con forme recorre los valores  

#SI NO HAY PUNTOS CRITICOS

if len(criticsdotsininterval) == 0:
    for i in range(n):
        x1 = x0 - ((f(x0)/df(x0)))
        if abs(x1 - x0) < error:
            if x1>=a and x1<=b:
             print(round(x1, 3), "es la raiz")
             break
            else:
                print("No se ha encontrado la raiz en este intervalo.")
        x0 = x1

    #graficar las raices con un punto de otro color y mantener el intervalo, o sea las lineas

    
#ANALIZA LOS PUNTOS CRITICOS QUE PERTENECEN AL INTERVALO

#ANALIZA CUANDO HAY UN UNICO PUNTO CRITICO       
if len(criticsdotsininterval) == 1:
    for i in range(n):
        x1 = x0 - ((f(x0)/df(x0)))
        if abs(x1 - x0) < error:
            if x1>=a and x1<=b:
             print(round(x1, 3), "es la raiz")
             break
            else:
             print("No se ha encontrado la raiz 1 en este intervalo.")
        x0 = x1           
    x01 = criticsdotsininterval[0]       
    x02 = float(x01) - 0.00000001
    for i in range(n):
        x2 = x02 - ((f(x02)/df(x02)))
        if abs(x2 - x02) < error:
            break
        x02 = x2   
        if x2 >= a and x2<= b and x1>=a and x1<=b:
         print("Las raices encontradas son: ", x1, " y ",x2)
        elif x2>=a and x2<=b:
            print("La primer raiz no se ha encontrado. La raiz encontrada es: ", x2)
    #graficar las raices con un punto de otro color y mantener el intervalo, o sea las lineas
    



#DETERMINAR MAXIMOS Y MINIMOS 
"""
Como se hace esto?
#1. Se toma el intervalo y la raiz o las raices que se encuentren en el intervalo. 
Se evaluan en la función original. El mayor valor será el máximo absoluto y el menor será el minimo absoluto. 
"""  
print("El intervalo introducido y analizado es: ", a," ",b,)

if len(criticsdotsininterval) == 0:
    for i in range(n):
        x1 = x0 - ((f(x0)/df(x0)))
        if abs(x1 - x0) < error:
            if x1>=a and x1<=b:
            
             #maximos y minimos
             val1 = f(x1)
             val2 = f(a)
             val3 = f(b)
             values =[val1, val2, val3]
             mayor = values[0]
             menor = values[0]
             for i in range(len(values)):
                if values[i] > mayor:
                    mayor = values[i]
                
             for i in range(len(values)):
                if values[i] < menor:
                    menor = values[i]
            else:
                print("No se ha encontrado la raiz en este intervalo.")
        x0 = x1      
    print("La raiz es: ", x1, "El valor maximo es: ", mayor, "El valor minimo es: ", menor)


if len(criticsdotsininterval) == 1:
    for i in range(n):
        x1 = x0 - ((f(x0)/df(x0)))
        if abs(x1 - x0) < error:
            if x1>=a and x1<=b:
             print(round(x1, 3), "es la raiz")
             break
