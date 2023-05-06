import socket
import struct
import numpy as np
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange
from itertools import count
from matplotlib.animation import FuncAnimation

# Dirección IP y puerto para recibir la lista
localIP = "192.168.0.14"
localPort = 5005

#Confirmación

print('El dispositivo se encuentra en escucha: ') 

# Crear un objeto socket y enlazarlo a la dirección IP y puerto
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((localIP, localPort))

#crear lista para almacenar los datos recibidos
data_accelerometer = []

 # Bucle para recibir la lista

while True:

    data, addr = sock.recvfrom(1024)

    numbers = []

    if len(data) % 4 == 0:  # Comprobar si la longitud es un múltiplo de 4 (tamaño de un entero)

        for i in range(len(data) // 4):

                number = struct.unpack("f", data[4*i:4*(i+1)])[0]

                numbers.append(number)

                #Vamos llenando una lista vacía con los datos obtenidos

        data_accelerometer.append(numbers)


#Rompro el ciclo cuando la cantidad de datos sea mayor o igual a 1024 datos.
    if len(data_accelerometer) >= 1024:
     break

    print(numbers)

c = input('Introduzca: [y] para almacenar los datos: ')
if 'y' in c:
    print('Los datos han sido almacenados')


data_accelerometer_numpy = np.asarray(data_accelerometer)

#Con los datos almacenados en la lista, creamos un archivo excel
data_book = openpyxl.Workbook()
sheet = data_book.active

for i, fila in enumerate(data_accelerometer):

    data_accelerometer_split = [int(valor) for valor in fila]
    for j, dato in enumerate(data_accelerometer_split):
        sheet.cell(row=i+1, column=j+1, value=dato)

#Guadar el archivo de excel
data_book.save('C:/Users/juand/Documents/Proyecto/datosgrupo/datos_11.xlsx')
print('El archivo se ha guardado!')


#Leer los datos del archivo 
confirm = input("Desea leer los datos obtenidos?: [y]: ")
if 'y' in confirm:
    df = pd.read_excel('C:/Users/juand/Documents/Proyecto/datosgrupo/datos_11.xlsx')
    matriz_datos = df.values
    print(matriz_datos)
    #Quitamos el dato de la aceleracion en y
    matriz_x_t = []
    for fila in matriz_datos: 
        matriz_fila = [fila[0], fila[2]]
        matriz_x_t.append(matriz_fila)

    #Quitamos el dato de aceleracion en x
    matriz_y_t = []
    for fila1 in matriz_datos:
        matriz_fila1 = fila1[:2]
        matriz_y_t.append(matriz_fila1)


    #Convierto las matrices en matrices de numpy

    matriz_x_t_numpy = np.asarray(matriz_x_t)
    matriz_y_t_numpy = np.asarray(matriz_y_t)

    #Graficas 

    #FILTRO DE LOS DATOS, SOLO TENDREMOS POSITIVOS 
    mask = matriz_x_t_numpy[:,0] >= 0 #Vamos a tomar todas filas de la columna 1, es decir, los valores x

    #aplicamos la mascara a una nueva matriz positiva

    matriz_x_t_numpy_positive = matriz_x_t_numpy[mask]
    #Eliminamos los datos negativos y dejamos solo los positivos


    #Grafica x/t 
    x = matriz_x_t_numpy_positive[:,0]
    y = matriz_x_t_numpy_positive[:,1]



    # Añadir los datos de cada columna al eje x, y
    xn = x.tolist()
    yn = y.tolist()
    x1 = []
    y1 = []

    fig, ax = plt.subplots()
    ax.plot(y1, x1)
    counter = count(0,1)
    def update(i):
        idx = next(counter)
        while idx < len(xn):
            x1.append(xn[idx])
            y1.append(yn[idx])
            plt.cla()
            plt.title('Velocidad Angular en el eje X')
            plt.xlabel('t')
            plt.ylabel('v')
            ax.plot(y1,x1)


    anim = FuncAnimation(fig=fig, func=update, interval=0.00001)
    plt.show()


    plt.scatter(y1,x1)
    plt.title('Velocidad Angular en el eje X')
    plt.xlabel('t')
    plt.ylabel('v')
    #Guadarmos el grafico en imagen 
    fecha_hora = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    nombre_archivo = f'C:/Users/juand/Documents/Proyecto/graficas/grafica_{fecha_hora}.jpg'
    plt.savefig(nombre_archivo)


    #Interpolacion de lagrange

    # Obtenemos los índices de los elementos únicos en cada columna
    unique_indices = np.unique(matriz_x_t_numpy, axis=0, return_index=True)[1]
    # Creamos una nueva matriz con los datos únicos
    new_data = matriz_x_t_numpy[unique_indices]


    #Grafica x/t 
    print(new_data)
    def interpolar(new_data, x):
        x_datos = new_data[:,0]
        y_datos = new_data[:,1]
        polinomio = lagrange(x_datos, y_datos)
        return polinomio(x)
    # Creamos un conjunto de valores de x a lo largo del rango de los datos
    x_vals = np.linspace(new_data[:,0].min(), new_data[:,0].max(), 1000)
    y_vals = interpolar(new_data, x_vals)
    plt.plot(y_vals, x_vals)
    plt.scatter(new_data[:,0], new_data[:,1], c='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación de Lagrange')

    #Guardar la grafica 
    #Guadarmos el grafico en imagen 
    fecha_hora = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    nombre_archivo = f'C:/Users/juand/Documents/Proyecto/graficas/grafica_{fecha_hora}.jpg'
    plt.savefig(nombre_archivo)
    plt.show()

    '''
    #Polinomio hallado 

    # Ajustamos un polinomio a los datos
    grado = len(new_data) - 1
    coeficientes = np.polyfit(new_data[:, 0], new_data[:, 1], grado)

    # Construimos el polinomio a partir de los coeficientes
    polinomio = np.poly1d(coeficientes)

    # Derivamos el polinomio
    derivada = polinomio.deriv()

    # Imprimimos la derivada
    print("La derivada del polinomio interpolante es: \n", derivada)'
    '''