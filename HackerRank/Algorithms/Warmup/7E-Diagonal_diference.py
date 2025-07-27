'''
Dada una matriz cuadrada, calcula la diferencia absoluta entre las sumas de sus diagonales.

Por ejemplo, la matriz cuadrada arr se muestra a continuación:

1 2 3
4 5 6
9 8 9

La diagonal de izquierda a derecha = 1 + 5 + 9 = 15.

La diagonal de derecha a izquierda = 3 + 5 + 9 = 17.

Su diferencia absoluta es:
|15 - 17| = 2

-- Descripción de la función

Complete la función con el siguiente parámetro:

* int arr[n][m]: una matriz bidimensional de números enteros

-- Devuele
* int n: la diferencia absoluta entre las sumas a lo largo de las diagonales

-- Formato de entrada

La primera línea contiene un único entero, n, el número de filas y columnas de la matriz cuadrada arr.

Cada una de las siguientes, n líneas, describe una fila, arr[i], y consta de n enteros separados por espacios arr[i][j].

-- Restricciones
* -100 <= arr[i][j] <=100

-- Entrada de muestra
STDIN      Function
-----      --------
3           arr[][] sizes n = 3, m = 3
11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
4 5 6
10 8 -12

-- Ejemplo de Salida
15

-- Explicación
La diagonal primaria es:
11
   5
     -12
Suma a lo largo de la diagonal primaria: 11 + 5 - 12 = 4.

La diagonal secundaria es:
     4
   5
10
Suma a lo largo de la diagonal secundaria: 4 + 5 + 10 = 19.

Diferencia: |4 - 19| = 15
'''

def diagonalDifference(arr):

    primary_diagonal_sum = 0
    secundary_diagonal_sum = 0
    n = len(arr)

    for i in range(n):
        primary_diagonal_sum += arr[i][i]
        secundary_diagonal_sum += arr[i][n - 1 - i]

    return abs(primary_diagonal_sum - secundary_diagonal_sum)

matriz = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(diagonalDifference(matriz))

'''
SOLUCIÓN 3: La más optimizada - BigO = O(n) --> Con un solo ciclo

primary_diagonal_sum = 0
secundary_diagonal_sum = 0
n = len(arr)

for i in range(n):
    primary_diagonal_sum += arr[i][i]
    secundary_diagonal_sum += arr[i][n - 1 - i]

return abs(primary_diagonal_sum - secundary_diagonal_sum)

EJECUIÓN DEL CÓDIGO

n = len(arr)
n = 3

Iteración-1
            [0,1,2] --> Fila 0
for 0 in range(3):
                                      index->0,0
    primary_diagonal_sum += arr[0][0] -----> [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    primary_diagonal_sum = 0 + 11 = 11

    secundary_diagonal_sum += arr[0][3 - 1 - 0]
                                        index-------->0,2
    secundary_diagonal_sum += arr[0][2] -----> [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    secundary_diagonal_sum = 0 + 4 = 4

Iteración-2
            [0,1,2] --> Fila 1
for 1 in range(3):
                                      index--------------->1,1
    primary_diagonal_sum += arr[1][1] -----> [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    primary_diagonal_sum = 11 + 5 = 16

    secundary_diagonal_sum += arr[1][3 - 1 - 1]
    secundary_diagonal_sum += arr[1][3 - 2]
                                        index--------------->1,1
    secundary_diagonal_sum += arr[1][1] -----> [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    secundary_diagonal_sum = 4 + 5 = 9

Iteración-3
            [0,1,2] --> Fila 2
for 2 in range(3):
                                      index------------------------------>2,2
    primary_diagonal_sum += arr[2][2] -----> [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    primary_diagonal_sum = 16 + (-12) = 4

    secundary_diagonal_sum += arr[2][3 - 1 - 2]
    secundary_diagonal_sum += arr[2][3 - 2]
                                        index---------------------->2,1
    secundary_diagonal_sum += arr[2][1] -----> [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    secundary_diagonal_sum = 9 + 10 = 19

return abs(primary_diagonal_sum - secundary_diagonal_sum)
        |4 - 19 |
        |-15| = 15
'''

'''
SOLUCIÓN 2: Tampoco sirvio para todos los casos de uso. BigO = O(n) -> con dos ciclos 2n

def diagonalDifference(arr):

    primary_diagonal_sum = 0
    secundary_diagonal_sum = 0
    n = len(arr)

    for i in range(n):
       primary_diagonal_sum += arr[i][i]


    for i in range(n):
        secundary_diagonal_sum  += arr[i][n - 1 - i]

    return abs(suma_principal - suma_secundaria)
'''

'''
SOLUCIÓN 1: No funcionó para los diferentes casos de uso, poco optimizada. BigO - O(n^2) --> Con 3 ciclos, dos anidados y uno aparte -> n^2 + 1n

def diagonalDifference(arr):

    primary_diagonal_sum = 0
    secundary_diagonal_sum = 0

    for row in arr:
        for element in row:
            if(arr.index(row) == row.index(element)):
                primary_diagonal_sum += element

    n = len(arr)
    for i in range(n):
        suma_secundaria += arr[i][n - 1 - i]

    return abs(primary_diagonal_sum - secundary_diagonal_sum)

EJECUCIÓN DEL CÓDIGO
Recorrido de la diagonal primaria:

for row in arr:
    for element in row:
        if(arr.index(row) == row.index(element)):
            primary_diagonal_sum += element

Iteración-1
index -------->0
for 0 in [[11, 2, 4],[4, 5, 6],[10, 8, -12]]:
index-->0    0,0
    for 11 in [11, 2, 4]:
        if(arr.index(0) == row.index(0)): ---> True
                     0  == 0
            primary_diagonal_sum = 0 + 11 = 11

Iteración-2
index -------->0
for 0 in [[11, 2, 4],[4, 5, 6],[10, 8, -12]]:
index-->1        0,1
    for 2 in [11, 2, 4]:
        if(arr.index(0) == row.index(1)): ---> False
                     0  == 1

Iteración-3
index -------->0
for 0 in [[11, 2, 4],[4, 5, 6],[10, 8, -12]]:
index-->2          0,2
    for 4 in [11, 2, 4]:
        if(arr.index(0) == row.index(2)): ---> False
                     0  == 2

Iteración-4
index ------------------>1
for 1 in [[11, 2, 4],[4, 5, 6],[10, 8, -12]]:
index-->0   1,0
    for 4 in [4, 5, 6]:
        if(arr.index(1) == row.index(0)): ---> False
                     1  == 0

Iteración-5
index ------------------>1
for 1 in [[11, 2, 4],[4, 5, 6],[10, 8, -12]]:
index-->1      1,1
    for 5 in [4, 5, 6]:
        if(arr.index(1) == row.index(1)): ---> True
                     1  == 1
            primary_diagonal_sum = 11 + 5 = 16

Iteración-6
index ------------------>1
for 1 in [[11, 2, 4],[4, 5, 6],[10, 8, -12]]:
index-->2         1,2
    for 6 in [4, 5, 6]:
        if(arr.index(1) == row.index(2)): ---> False
                     1  == 2

Iteración-7
index ----------------------------->2
for 1 in [[11, 2, 4],[4, 5, 6],[10, 8, -12]]:
index-->0    2,0
    for 10 in [10, 8, -12]:
        if(arr.index(2) == row.index(0)): ---> False
                     2  == 0

Iteración-8
index ----------------------------->2
for 1 in [[11, 2, 4],[4, 5, 6],[10, 8, -12]]:
index-->1       2,1
    for 8 in [10, 8, -12]:
        if(arr.index(2) == row.index(0)): ---> False
                     2  == 0

Iteración-9
index ----------------------------->2
for 1 in [[11, 2, 4],[4, 5, 6],[10, 8, -12]]:
index--->2            2,2
    for -12 in [10, 8, -12]:
        if(arr.index(2) == row.index(2)): ---> True
                     2  == 2
            primary_diagonal_sum = 16 + (-12) = 4

Recorrido de la diagonal secundaria:
n = len(matriz)
for row in range(n):
    col = n - 1 - row  #  columna = tamaño - 1 - fila
    secundary_diagonal_sum = matriz[row][col]

n = 3
Iteración-1
            [0,1,2]
for 0 in range(3)
    col = n - 1 - row
    col = 3 - 1 - 0
    col = 2
    secundary_diagonal_sum += matriz[row][col]  index->0,2
    secundary_diagonal_sum += matriz[0][2] -->  [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    secundary_diagonal_sum = 0 + 4 = 4

Iteración-2
            [0,1,2]
for 1 in range(3)
    col = n - 1 - row
    col = 3 - 1 - 1
    col = 3 - 2
    col = 1
    secundary_diagonal_sum += matriz[row][col]  index-------->1,1
    secundary_diagonal_sum += matriz[1][1] -->  [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    secundary_diagonal_sum = 4 + 5 = 9

Iteración-3
            [0,1,2]
for 2 in range(3)
    col = n - 1 - row
    col = 3 - 1 - 2
    col = 3 - 3
    col = 0
    secundary_diagonal_sum += matriz[row][col]  index--------------->2,0
    secundary_diagonal_sum += matriz[2][0] -->  [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
    secundary_diagonal_sum = 9 + 10 = 19

return abs(primary_diagonal_sum - secundary_diagonal_sum)
        |4 - 19 |
        |-15| = 15
'''