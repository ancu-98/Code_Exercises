'''
Dada una matriz de enteros, hallar la suma de sus elementos.

Por ejemplo
si la matriz, ar = [1,2,3] , 1+2+3 = 6
entonces devuelve 6

--Descripción de la función

Complete la función simpleArraySum en el editor de abajo.
Debe devolver la suma de los elementos del array como un entero.

simpleArraySum tiene los siguientes parámetros:

ar: un array de enteros

--Formato de entrada

La primera línea contiene un número entero, n, que indica el tamaño de la matriz.
La segunda línea contiene enteros separados por espacios que representan los elementos de la matriz.

--Restricciones
0<n,ar[i]<=1000

--Formato de salida

Imprime la suma de los elementos de la matriz como un único número entero.

-Ejemplo de entrada
6
1 2 3 4 10 11

-Ejemplo de salida
31

--Explicación

Imprimimos la suma de los elementos del array:
1+2+3+4+10+11 = 31
'''

def simpleArraySum(ar):
    #Longitud de la lista
    n = len(ar)
    sum = 0

    for i in ar:
        # Sí n y cada elemento de la lista(i), son mayores que 0 y menores que 1000
        if(0 < n <= 1000) & (0 < i <= 1000):
            sum += i
        else:
            print('Los elementos del arreglo deben estar en un rango entre 0 a 1000')

    return sum

print('La suma del arreglo es:',simpleArraySum([1,2,3,1001,-1,9]))