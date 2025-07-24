'''
En este reto, se le pide que calcule e imprima la suma de los elementos de una matriz,
teniendo en cuenta que algunos de esos enteros pueden ser bastante grandes.

--Descripción de la función
Complete la función aVeryBigSum en el editor de abajo. Debe devolver la suma de todos los elementos del array.

aVeryBigSum tiene los siguientes parámetros:
* int ar[n]: un array de enteros .

--Devuelve
* long: la suma de todos los elementos del array

--Formato de entrada
La primera línea de la entrada consiste en un entero .
La siguiente línea contiene enteros separados por espacios contenidos en la matriz.

--Formato de salida
Devuelve la suma entera de los elementos de la matriz.

--Restricciones
1 <= n <= 10
0 <= ar[i] <= 10^10

--Entrada de ejemplo
5
1000000001 1000000002 1000000003 1000000004 1000000005

--Salida
5000000015

--Nota:

El rango de los enteros de 32 bits es:
(-2^31) a (2^31 -1) or
[-2147483648,2147483647]

Cuando sumamos varios valores enteros, la suma resultante puede exceder el rango anterior.
Puede que necesites usar long int C/C++/Java para almacenar dichas sumas.
'''

def aVeryBigSum(ar):
    n = len(ar)
    big_sum = 0
    # Sí la longitud del arreglo es menor o igual a 10
    if(n <= 10):
        for i in ar:
            # Sí cada uno de los elementos del arreglo se encuentra en el rango de los enteros de 32 bits.
            if(-2**31 < i < 2**31 -1):
                big_sum += i

    return big_sum


print(aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005]))
