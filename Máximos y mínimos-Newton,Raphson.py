from logging import critical
import numpy as np
import matplotlib.pyplot as plt
import math 
from sympy import * 
import symbol

funcion = input("Introduzca la funcion, recuerde el formato: ")

a = float(input("Introduzca el [a] invervalo donde se encuentran las raices: "))
b = float(input("Introduzca el valor [b]: "))
#por derecha obligatoriamente
x0 = float(input("Introduzca el valor arbitrario para iniciar el método: "))
#error = float(input("Introduzca el error, el formato es [1e-10]: "))
error = 1e-10

#Gráfica

x = np.linspace(-5, 5, 1500)
xes =  np.linspace(a, a, 1500)
xes2 = np.linspace(b, b, 1500)

de1 = np.linspace(-10, 10, 1500)
de2 = np.linspace(-10, 10, 1500)

plt.plot(x, eval(funcion), '-', label='funcion', linewidth=1.5,color=(0.2,0.1,0.4))
plt.plot(xes, de1,'-',linewidth=1, label='Intervalo delimitador', color=("red"))
plt.plot(xes2, de2, '-',linewidth=1, color=("red"))
plt.legend(shadow=True)
plt.grid()
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafica de la función dada')
plt.show()




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


#confirmacion del usuario para iniciar el proceso#
#mencione que tiene q cerrar la grafica
#ha visualizado las raices? [y][n]

#meta todo en un if que confirme todo

n = 20
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

r = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#ANALIZA CUANDO HAY UN UNICO PUNTO CRITICO    
if len(criticsdotsininterval) == 1:
    x = np.linspace(-5, 5, 1500)
    xes =  np.linspace(a, a, 1500)
    xes2 = np.linspace(b, b, 1500)

    de1 = np.linspace(-10, 10, 1500)
    de2 = np.linspace(-10, 10, 1500)
    for i in range(n):
        x = np.linspace(-5, 5, 1500)
        x1 = x0 - ((f(x0)/df(x0)))
        if abs(x1 - x0) < error:
            if x1>=a and x1<=b:
             print(round(x1, 3), "es la raiz")
             break
            else:
             print("No se ha encontrado la raiz 1 en este intervalo.")

        recta = "{0}*{1} -({0}*{2}) + {3}" #Ecuación de la recta secante al los dos puntos dados
        arg0 = df(x0) #argumento 0
        arg1 = "x" #argumento 1
        arg2 = x0 #argumento 2
        arg3 = f(x0) #argumento 3
        r[i]= recta.format(arg0, arg1, arg2, arg3) 
        plt.plot(x,eval(r[i]), '-',linewidth=1.5,color=("g"))  
        x0 = x1  

    plt.plot(xes, de1,'-',linewidth=1, label='Intervalo delimitador', color=("red"))
    plt.plot(xes2, de2, '-',linewidth=1, color=("red"))
    plt.plot(x, eval(funcion), '-', label = 'Funcion', linewidth=1.5,color=(0.2,0.1,0.4))
    plt.legend(shadow=True)  
    plt.grid()
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Grafica de la función dada')
    plt.show()
        
    x01 = criticsdotsininterval[0]       
    x02 = float(x01) - 0.00000001
    for i in range(n):
        x2 = x02 - ((f(x02)/df(x02)))
        if abs(x2 - x02) < error:
            break
        x02 = x2   
        if x2 >= a and x2<= b and x1>=a and x1<=b:
         print("Las raices encontradas son: ", round(x1,1), " y ", round(x2,1))
        elif x2>=a and x2<=b:
            print("La primer raiz no se ha encontrado. La raiz encontrada es: ", x2)
    #graficar las raices con un punto de otro color y mantener el intervalo, o sea las lineas
    

    
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


error = 1e-10

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
            #si las 2 raices están dentro del intervalo
            val11 = f(x1)
            val22 = f(x2)
            val33 = f(a)
            val44 = f(b)
            values1 = [val11, val22, val33, val44]
            mayor = values1[0]
            menor = values1[0]
            for i in range(len(values1)):
                if values1[i] > mayor:
                    mayor = values1[i]
                    print(mayor)
            for i in range(len(values1)):
                if values1[i] < menor:
                    menor = round(values1[i],1)
                    
        
    print("Las raices encontradas son: ", x1," y ", x2, "El mayor absoluto es: ", mayor, "El menor absoluto es: ", f(menor))
    """
        elif x2>=a and x2<=b:
            print("La primer raiz no se ha encontrado. La raiz encontrada es: ", x2)
            exit()
    """
        
        

    
    





































#ahora, si tenemos mas de 1 punto critico, vamos a pensar un poco mas a fondo en como resolver 
#el tema de si tenemos hasta 3 puntos criticos en un invervalo. asi que vamos a configurar 
#el codigo para trabajar asi
"""
if len(criticsdotsininterval) == 2:
    #1 hallar la primer raiz. esto ya se hace desde arriba
    #2 comparar los 2 valores de los puntos criticos

    if float(criticsdotsininterval[0]) == float(x1):
        x01 = criticsdotsininterval[1]
        x02 = float(x01) - 0.00000001
        for i in range(n):
            x2 = x02 - ((f(x02)/df(x02)))

            if abs(x2 - x02) < error:
                print(round(x2, 3), "es la raiz")
                break
            x02 = x2
        print(x02)
        print("Las raices son: ", x2)

    elif float(criticsdotsininterval[1]) == float(x1):
        x01 = criticsdotsininterval[0]
        x02 = float(x01) - 0.00000001
        for i in range(n):
            x2 = x02 - ((f(x02)/df(x02)))

            if abs(x2 - x02) < error:
                print(round(x2, 3), "es la raiz")
                break
            x02 = x2
        print(x02)
        print("Las raices son: ", x1,x2)


    if abs(criticsdotsininterval[0] - x1) < abs(criticsdotsininterval[1] - x1 ):
        x01 = criticsdotsininterval[0]
        x02 = float(x01) - 0.00000001
        for i in range(n):
            x2 = x02 - ((f(x02)/df(x02)))

            if abs(x2 - x02) < error:
                print(round(x2, 3), "es la raiz")
                break
            x02 = x2
        print(x02)      
        

        #ya tenemos la segunda raiz. como son 2 puntos criticos y ya hallamos el primero, necesariamente el segundo es el que 
        # buscamos para hallar la tercera raiz
        x011 = criticsdotsininterval[1]
        x022 = float(x01) - 0.00000001
        for i in range(n):
            x22 = x02 - ((f(x022)/df(x022)))
            if abs(x22 - x022) < error:
                print(round(x22, 3), "es la raiz")
                break
            x022 = x22
        print("Las raices encontradas son: ", x1, x2, x22)          
        #ahora simplemente introducimos un else que explique que ocurre si el primero es mayor al segundo

    if abs(criticsdotsininterval[0] - x1) > abs(criticsdotsininterval[1] - x1 ):
        x01 = criticsdotsininterval[1]
        x02 = float(x01) - 0.00000001
        for i in range(n):
            x2 = x02 - ((f(x02)/df(x02)))

            if abs(x2 - x02) < error:
                print(round(x2, 3), "es la raiz")
                break
        x02 = x2
        x011 = criticsdotsininterval[0]
        x022 = float(x01) - 0.00000001
        for i in range(n):
            x22 = x02 - ((f(x022)/df(x022)))

            if abs(x22 - x022) < error:
                print(round(x22, 3), "es la raiz")
                break
            x022 = x22
        print("Las raices encontradas son: ", x1, x2, x22)
"""



"""
Que se va a hacer? Bueno, ya se tiene la primer raiz, entonces el plan es el siguiente. tomaremos 
el punto critico justo despues de la raiz, es decir, el punto crítico que se encuentra inmediatamente
despues a la izquierda de la raiz. Conociendo ya el punto critico que se encuentra mas cerca, le restamos
un valor en x de esa imagen, uno muy pequeño de manera en que se reescriba el nuevo x0. justo desde allí 
se inicia de nuevo el ciclo. 
"""