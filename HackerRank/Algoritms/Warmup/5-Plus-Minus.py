'''
Dada una matriz de números enteros,
calcula las proporciones de sus elementos que son:
* positivo
* negativo
* y cero

Imprime el valor decimal de cada fracción en una nueva línea con 6 decimales.

Nota: Este desafío presenta problemas de precisión.
Los casos de prueba se escalan a seis decimales, aunque se aceptan respuestas con un error absoluto de hasta 10⁻⁴.

Ejemplo:
arr = [1,1,0,-1,-1]

Hay elementos: dos positivos, dos negativos y uno cero.
Sus ratios son:
2/5 = 0.400000
2/5 = 0.400000
1/5 = 0.200000

Los resultados se imprimen como:
0.400000
0.400000
0.200000

--Descripción de la Función
Completa la función plusMinus con los siguientes parámetros:

* int arr[n] : una matriz de números enteros

--Imprimir
Imprime las proporciones de valores positivos, negativos y cero en la matriz. Cada valor debe imprimirse en una línea separada con dígitos después del decimal.
La función no debe devolver ningún valor.

--Formato de entrada
La primera línea contiene un número entero, n, el tamaño de la matriz.
La segunda línea contiene, n, enteros separados por espacios que describen arr[n]

--Restricciones
0 < n <= 100
-100 <= arr[i] <= 100

--Formato de entrada
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

--Formato de salida
0.500000
0.333333
0.166667

--Explicación
Hay 3 números positivos, 2 números negativos y 1 cero en la matriz.
Las proporciones de aparición son positivas:
3/6 = 0.500000
2/6 = 0.333333
1/6 = 0.166667
'''

arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr) :
    n = len(arr)
    pos_nums = 0
    neg_nums = 0
    cero_nums = 0

    for number in arr:
        if number > 0:
            pos_nums += 1
        elif number < 0:
            neg_nums += 1
        elif number == 0:
            cero_nums += 1

    return print("{:.6f}\n{:.6f}\n{:.6f}".format(pos_nums/n, neg_nums/n, cero_nums/n))


print(plusMinus(arr))
# Output
# 0.500000
# 0.333333
# 0.166667
# None --> Esto lo devuelve porque hay un doble print()
# Si quiesiera eliminar el None, solo debo eliminar el print() que retorna la función



