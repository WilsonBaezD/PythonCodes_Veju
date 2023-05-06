import tkinter as tk
import numpy as np
import sympy as sym

ventana = tk.Tk()
ventana.title('Calculadora Algebra II')

etiqueta_titulo = tk.Label(ventana, text='''
CALCULADORA ALGEBRA LINEAL II
Juan david Vega
''', font=("Helvetica", 24))
etiqueta_titulo.pack()

etiqueta_cuerpo = tk.Label(ventana, text='''
1. Suma de matrices *definido sin función
2. Multiplicacion escalar de matrices *definido sin funcion
3. Transponer una matriz * definido parcialmente 
4. Producto de matrices 
5. Reduccion de una matriz a su forma escalonada
6. Traza de una matriz 
7. Determinante de una matriz 
8. Inversa de una matriz 
9. Hallar rango de una matriz 
10. Hallar la nulidad de una matriz
11. Resolver un sistema de ecuaciones lineales
12. Dado un conjunto de vectores en R^N determinar si son linealmente independientes * dado con tecnica
13. Hallar el polinomio característico de una matriz 
14. Calcular los valores propios de una matriz
15. Ortogonalizar una base de R^n, conjunto de vectores cualquier de R^n * definido sin funcion
15.1 Ortonormalizar un conjunto de vectores de R^n * definido sin funcion
16. Diagonalizar una matriz     


''')
etiqueta_cuerpo.pack()
ventana.mainloop()

funcion = int(input("Introduzca la función que desea realizar, utilice el número de la función: "))


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


#MATRIZ SYMPY
def getmatrixSYMPY(m, n):
    A = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(int(input(f"Introducir el valor de la posición ({i + 1},{j + 1}): ")))
        A.append(fila)

    return sym.Matrix(A)

#suma de matrices
if 1 == funcion: 
    A = []
    #definir el tamaño de la matriz, estará solo definido para matrices n x n 
    n = int(input('Introduzca el tamaño de la matriz: '))
    #introducir los elementos en una lista temporal que luego será clasificada
    print('Introduzca los elementos de la matriz N X N: ')
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(int(input()))
        A.append(fila)
    print('La matriz A es:', A)
    B = []
    n = int(input('Introduzca el tamaño de la matriz N x N: '))
    print('Introduzca los valores de la matriz: ')
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(int(input()))
        B.append(fila)
    print('La matriz B es:', B)
    #Ahora, para la suma se debe iterar a traves de las filas y de las columnas
    print(A[0], A[1])
    print(len(A[0]))
    #matriz de 0 para poder almacenar el resultado 
    ans = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(int(0))
        ans.append(fila)
    print(ans)
    #Iterar a traves de las filas
    for i in range(n):
    #iterar a traves de las columnas
        for j in range(len(A[0])): 
            ans[i][j] = A[i][j] + B[i][j]
    print('La matriz suma es:', ans)
    
#multiplicacion por escalar
if 2 == funcion: 
    A = []
    n = int(input('Introduzca el tamaño de la matriz: '))
    print('Introduzca los elementos de la matriz: ')
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(int(input()))
        A.append(fila)
    print('La matriz es:', A)
    a = float(input('Introduzca el escalar a multiplicar: '))
    ans = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(int(0))
        ans.append(fila)
    for i in range(n):
        for j in range(len(A[0])): 
            ans[i][j] = (A[i][j])*a
    print('La matriz suma es:', ans)

#matriz transpuesta
if 3 == funcion:
    A = []
    #definir el tamaño de la matriz m columnas
    m = int(input('Introduzca la cantidad m de columnas: '))
    #definir el tamaño de la matriz n filas
    n = int(input('Introduzca la cantidad n de filas: '))


    #introducir los elementos en una lista temporal que luego será clasificada
    print('Introduzca los elementos de la matriz: ')
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(int(input()))
        A.append(fila)
    print('La matriz es:', A)

    #convertir la matriz en una matrix de numpy

    mtx1 = np.asarray(A)
    confirm = str(('La matriz a transponer es: ', mtx1, 'Si es así, introduzca [y]: '))
    if 'y' in confirm:
        mtx1transpose = mtx1.transpose()
        print('La matriz transpuesta es: ', mtx1transpose)


#producto de matrices

if 4 == funcion: 

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

        if m == n1:
            mtxproduct = np.matmul(mtx1, mtx2)
            print('La matriz resultante es: ', mtxproduct)

        else: 
            print('La dimensión de las matrices es incorrecta')

    
#matriz reducida a su forma escalonada por renglones
if 5 == funcion: 
        confirm2 = str(input('''Las matrices se introducen dentro el código.
    Para confirmar, introduzca [y]: 
    '''))
        if 'y' in confirm2:
            ###mtx1 = sp.Matrix([[1,2,3],[4,2,6],[7,4,3]])
            n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
            m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
            mtx1 = getmatrixSYMPY(m,n)
            #Tener en cuenta que cada corchete de valores es la columna de la matriz
            mtx1R= mtx1.rref()
            print('La matriz reducida por renglones es: ', mtx1R)

#traza de una matriz
if 6 == funcion:
    n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
    m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
    mtx1 = getmatrix(m,n)
    mtx1trace = np.trace(mtx1)
    print('La traza de la matriz es: ', mtx1trace)

#determinante de una matriz 
if 7 == funcion:
        n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
        m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
        if n == m:
         mtx1 = getmatrix(m,n)
         mtx1det = np.linalg.det(mtx1)
         print('El determinante de la matriz es: ', mtx1det)
        else: 
            print('Solo es posible obtener el determinante de matrices cuadradas')

#Inversa de una matriz
if 8 == funcion:
            n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
            m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
            mtx1 = getmatrix(m,n)
            mtx1det = np.linalg.det(mtx1)
            detvalue = mtx1det.astype(int)
           # print(type(detvalue)) Para saber que tipo de dato me ofrecia el numpy 
            if detvalue != 0:
                mtx1inverse = np.linalg.inv(mtx1)
                print('La inversa de la matriz es: ', mtx1inverse)
            else: 
             print('La matriz no tiene inversa. ')

#Rango de una matriz 
if 9 == funcion: 
            n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
            m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
            mtx1 = getmatrix(m,n)
            mtx1rank = np.linalg.matrix_rank(mtx1)
            print('El rango de la matriz es: ', mtx1rank)

#Hallar la nulidad de la matriz, numero de columnas para que cumpla el teorema 

#Para esta función, utilizaremos el rango de la matriz y el teorema que el rango de la matriz + la nulidad =
# cantidad de columnas de la matriz. 

if 10 == funcion: 
            n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
            m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
            mtx1 = getmatrix(m,n)
            nxm = mtx1.shape
            #print(nxm[0]) ----> fila
            #print(nxm[1]) ----> columna
            #print(mtx1) -----> Matriz

            #Primero, hallar el rango: 
            mtx1rank = np.linalg.matrix_rank(mtx1)
            rank_value = mtx1rank.astype(int)
            nul_value = nxm[1] - rank_value
            print('El espacio nulo de la matriz es: ', nul_value)


#Resolver sistema de ecuaciones
#El sistema va a verificar todos los requisitos necesarios para poder resolver el sistema
if 11 == funcion: 
            n = int(input('Introduzca la cantidad n de filas MATRIZ COEFICIENTES: '))
            m = int(input('Introduzca la cantidad m de columnas MATRIZ COEFICIENTES: '))
            mtx1 = getmatrix(m,n)
            print('Se ha introducido la matriz de coeficientes: ', mtx1)
            n1 = int(input('Introduzca la cantidad n de filas MATRIZ SOLUCION: '))
            m1 = int(input('Introduzca la cantidad m de columnas MATRIZ SOLUCION: '))
            bT = getmatrix(m1,n1)
            print(bT) 
            print('''Se ha introducido la matriz de coeficientes, se hallará la solución
            de un sistema de la forma Ax = b
            ''')
            
            ##bT = np.transpose(b) ----> No era necesario transponerla

            #verificar que cumplan el tamaño, es decir, m x n y n x p = m x p. 
            #Debe coincidir el numero de columnas de la A con el numero de filas de b. 

            mtx1MXN = mtx1.shape
            mtx1C = mtx1MXN[1] #----> columna
            print('El numero de columnas de A es: ', mtx1C)
            bMXN = bT.shape
            bF = bMXN[0] # -----> fila 
            print('El numero de filas de b es: ', bF)

            if mtx1C == bF:
                print('El tamaño es válido')
                answS = np.linalg.solve(mtx1,bT)
                print('La solución del sistema de ecuaciónes es: ', answS)
            else: 
                print('Las matrices no son de la forma m x n y n x p = m x p. No se pueden operar!')

#Determinar si un conjunto de vectores de R^n son linealmente independientes
if 12 == funcion:
        print('Verificar si un conjunto de vectores en R^n son linealmente independientes')
        print('El vector será la fila de la matriz')
        n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
        m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
        print('Cada fila será cada vector')
        mtx1trans = getmatrix(m,n)
        ##mtx1trans = np.transpose(mtx1) # ---> cada componente será un vector columna
        mtx1rank = np.linalg.matrix_rank(mtx1trans)
        mtxMXN = mtx1trans.shape
        mtxC = mtxMXN[1] #---> numero de columnas

        if mtxC == mtx1rank:
            print('Los vectores son linealmente independientes.')

        else: 
            print('Existe al menos un vector que es linealmente dependiente de los demás. ')


        print('El rango de la matriz es: ', mtx1rank)


    #Podemos usar el metodo del rango de una matriz, si creamos una matriz de n columnas con vectores n de R^n
    #es posible determinar si son o no linealmente dependientes usando el rango. Si la dimensión del espacio
    #columna de la matriz es igual al numero de columnas quiere decir que la dimension del espacion nulo es 0. 
    #por lo tanto, todas las columnas contienen pivote, en conclusión, son linealmente independientes. 


#Polinomio característico 
if 13 == funcion: 
        #creamos una matriz de sympy 
        n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
        m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
        mtx1 = getmatrixSYMPY(m,n)
        
        #------------------------------------------------
        #mtx1 = sym.Matrix([[1,2,3],[4,2,6],[7,4,3]])
        #PurePoly(x**3 - 6*x**2 - 42*x - 48, x, domain='ZZ')
        #------------------------------------------------

        #creamos un simbolo como 'x', sympy permite hacer operaciones como simbolos en vez de números
        value = sym.Symbol('x')

        #polinomio caracterísico
        polcha = mtx1.charpoly(value)
        print(polcha)

#Calcular los valores propios
if 14 == funcion: 
        n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
        m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
        mtx1 = getmatrix(m,n)

        #----------------------------------------------------------
        #mtx1 = np.array([[1,3,5], [4,8,6], [8,16,12]])
        #[[22.427],[-1.427], [-0.   ]]
        #-----------------------------------------------------------

        eigenvalues = np.linalg.eigvals(mtx1)
        eigmxn = eigenvalues.shape
        eigfil = eigmxn[0]
        #print(eigenvalues)
        REeigenvalues = np.zeros((eigfil, 1))
        #print(REeigenvalues)
        
        for i in range(0, eigfil):
            REeigenvalues[i] = np.round(eigenvalues[i], decimals = 7)
        print('Los valores propios de la matriz son:', REeigenvalues)

#ortogonalizar una base de R^n
if 15 == funcion: 
    print('Se introducirá un conjunto de vectores que representan una base y serán ortogonalizados')
    
    #n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
    #m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
    #vectors_transposed = getmatrix(m,n)
    
    #-----------------------------------------------------------
    vectors_non_ort = np.array([[1,1,1], [1,0,2], [-1,1,0]])
    #[[ 1.          1.          0.        ] [ 0.         -4.         -1.        ]
    #[-0.27777778  0.11111111  0.72222222]]
    #-----------------------------------------------------------


    vectors_transposed = np.transpose(vectors_non_ort)
    w1 = vectors_transposed[:,0]
    mxn = vectors_transposed.shape 
    m = mxn[0]
    print('La matriz tiene', m, 'filas')
    n = mxn[1]
    print('La matriz tiene', n, 'Columnas')
    matrix = np.zeros((m,n))
    matrix[0] = vectors_transposed[:,0]
    print(matrix)
    mxn = vectors_transposed.shape 
    m = mxn[0]
    print('La matriz tiene', m, 'filas')
    n = mxn[1]
    print('La matriz tiene', n, 'Columnas')
    for i in range(1,n):
        matrix[i] = vectors_transposed[:,i]
        for j in range(i):
            matrix[i] = matrix[i] - ((np.dot(vectors_transposed[:,i], matrix[:,j]))/(np.dot(matrix[:,i], matrix[:,j]))) * matrix[:,j]

    print('Los vectores ortogonales de la matriz original son:', matrix)


    confirm = str(input('Desea ortonormalizar la base hallada? [y]: '))

    if 'y' in confirm: 
        ortonormal_matrix = []
        ortonormal_matrix.append(w1/np.linalg.norm(w1))
        for i in range(1,n):
            wi = matrix[i]/np.linalg.norm(matrix[i])
            ortonormal_matrix.append(wi)
    print('Los vectores ortonormales son:', ortonormal_matrix)     
       
#Diagonalizar una matriz 
if 16 == funcion: 
    confirm2 = str(input('''Las matrices se introducen dentro el código.
    Para confirmar, introduzca [y]: 
    '''))
    if 'y' in confirm2:

        n = int(input('Introduzca la cantidad n de filas MATRIZ (1): '))
        m = int(input('Introduzca la cantidad m de columnas MATRIZ (1): '))
        mtx1 = getmatrixSYMPY(m,n)
        #mtx1 = sym.Matrix([[3, -2,  4, -2],
        #                            [5,  3, -3, -2],
        #                        [5, -2,  2, -2],
        #                        [5, -2, -3,  3]])
        mtx1diag = mtx1.diagonalize()
        print(mtx1diag)

        #---------------------------------------------
        #mtx1 = sym.Matrix([[3, -2,  4, -2],
        #                            [5,  3, -3, -2],
        #                        [5, -2,  2, -2],
        #                        [5, -2, -3,  3]])

        #[0, 1, 1,  0],
        #[1, 1, 1, -1],
        #[1, 1, 1,  0],
        #[1, 1, 0,  1]]), Matrix([
        #[-2, 0, 0, 0],
        #[ 0, 3, 0, 0],
        #[ 0, 0, 5, 0],
        #[ 0, 0, 0, 5]]))
        #----------------------------------------------

#Hallar nucleo e imagen de una transformación lineal  

#NO ME ALCANZÓ EL TIEMPO 
if 17 == funcion:
    n = int(input('Introduzca la cantidad n de filas MATRIZ ASOCIADA: '))
    m = int(input('Introduzca la cantidad m de columnas MATRIZ ASOCIADA: '))
    mtx1 = getmatrix(m,n)

    #Hallar el espacio columna de la matriz:  
    mtx1rank = np.linalg.matrix_rank(mtx1)

    print('La imagen de la transformación de la matriz asociada a la T.L: ', mtx1rank)

    #Restar con el numero de columnas de la matriz asociada para hallar la nulidad
    rank_value = mtx1rank.astype(int)
    nul_value = nxm[1] - rank_value

    print('El espacio nulo de la matriz asociada a la T.L es: ', nul_value)
#NO ME ALCANZÓ EL TIEMPO PARA HACERLO :c

            