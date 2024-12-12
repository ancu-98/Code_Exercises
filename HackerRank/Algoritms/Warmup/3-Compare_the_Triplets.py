'''
Alice y Bob crearon cada uno un problema para HackerRank. Un revisor califica los dos retos, otorgando puntos en una escala de 1 a 100 para tres categorías: claridad del problema, originalidad y dificultad.

La puntuación del reto de Alice es el triplete a = (a[0], a[1], a[2]), y la del reto de Bob es el triplete b = (b[0], b[1], b[2]).

La tarea consiste en encontrar sus puntos de comparación comparando a[0] con b[0], a[1] con b[1] y a[2] con b[2].
Si a[i] > b[i], Alice recibe 1 punto.
Si a[i] < b[i], Bob recibe 1 punto.
Si a[i] = b[i], ninguna de las dos personas recibe un punto.
Puntos de comparación es el total de puntos que ha ganado una persona.

Dados a y b, determina sus respectivos puntos de comparación.

--Ejemplo

a = [1, 2, 3]
b = [3, 2, 1]

* Para los elementos *0*, Bob obtiene un punto porque a[0] .
* Para los elementos iguales a[1] y b[1], no se obtiene ningún punto.
* Finalmente, para los elementos 2, a[2] > b[2] por lo que Alice recibe un punto.
El array de retorno es [1, 1] con la puntuación de Alicia en primer lugar y la de Bob en segundo.

--Descripción de la función

Completa la función compareTriplets en el editor de abajo.

compareTriplets tiene los siguientes parámetros:
* int a[3]: Puntuación del reto de Alice
* int b[3]: La puntuación de Bob

--Devuelve
* int[2]: La puntuación de Alice está en la primera posición y la de Bob en la segunda.

--Formato de entrada
La primera línea contiene 3 enteros separados por espacios, a[0], a[1] y a[2], los valores respectivos del triplete a.
La segunda línea contiene 3 enteros separados por espacios, b[0], b[1] y b[2], los valores respectivos del triplete b.

--Restricciones
* 1 ≤ a[i] ≤ 100
* 1 ≤ b[i] ≤ 100

--Entrada de muestra 0
5 6 7
3 6 10

--Salida de muestra 0
1 1

--Explicación 0
En este ejemplo:
- a = (a[0],a[1],a[2]) = (5,6,7)
- b = (b[0],b[1],b[2]) = (3,6,10)

Ahora, comparemos cada puntuación individual:
a[0] > b[0], por lo que Alice recibe punto.
a[1] = b[1], por lo que nadie recibe punto.
a[2] < b[2], por lo que Bob recibe punto.
La puntuación de comparación de Alice es , y la puntuación de comparación de Bob es 1.
Por lo tanto, devolvemos la matriz [1,1].

--Ejemplo Entrada 1
17 28 30
99 16 8

--Ejemplo de salida 1
2 1

--Explicación 1

Al comparar los ar[0] elementos, 17 < 99 Bob recibe un punto.
Comparando los ar[1] y a[2] elementos, 28 > 16 y 30 > 8 entonces Alice recibe dos puntos.
La matriz de retorno es [2,1].
'''

# -------PRIMER INTENTO
# def compareTriplets(a,b):
#     alicePoints = 0 # a
#     bobPoints = 0   # b
#     comparisonPoints = []

#     for i in a:
#         for j in b:
#             # Sí cada elemento de la lista a y b, son mayores que 1 y menores que 100
#             if(1 <= i <= 100) & (1 <= j <= 100):
#                 # Procedemos a comparar los puntos
#                 # Si a[i] > b[i], Alice recibe 1 punto.
#                 if (i > j):
#                     alicePoints += 1
#                 # Si a[i] < b[i], Bob recibe 1 punto.
#                 elif (i < j):
#                     bobPoints += 1
#                 # Si a[i] = b[i], ninguna de las dos personas recibe un punto.
#                 elif (i == j):
#                     alicePoints += 0
#                     bobPoints += 0
#             else:
#                 print('Los elementos del arreglo deben estar en un rango entre 0 a 100')

#     comparisonPoints.append(alicePoints)
#     comparisonPoints.append(bobPoints)

#     return comparisonPoints

# print(compareTriplets([5,6,7],[3,6,10]))


# -------SEGUNDO INTENTO
# def compareTriplets1(a,b):
#     alicePoints = 0 # a
#     bobPoints = 0   # b
#     comparisonPoints = []

#     for i in a:
#         for j in b:
#             # Sí cada elemento de la lista a y b, son mayores que 1 y menores que 100
#             if(1 <= i <= 100) & (1 <= j <= 100):
#                 # Procedemos a comparar los puntos
#                 # Si a[i] > b[i], Alice recibe 1 punto.
#                 if (i > j):
#                     alicePoints += 1
#                     print(i,j,alicePoints)
#                 # Si a[i] < b[i], Bob recibe 1 punto.
#                 if (i < j):
#                     bobPoints += 1
#                     print(i,j,bobPoints)
#                 # Si a[i] = b[i], ninguna de las dos personas recibe un punto.
#                 if (i == j):
#                     print(i,j)
#                     alicePoints += 0
#                     bobPoints += 0
#             else:
#                 print('Los elementos del arreglo deben estar en un rango entre 0 a 100')

#     comparisonPoints.append(alicePoints)
#     comparisonPoints.append(bobPoints)

#     return comparisonPoints

# print(compareTriplets1([5,6,7],[3,6,10]))

'''
EL error está en que esta comparando un elemento de la lista a con todos los demás elementos de la lista b:
* a[0] lo compara con b[0],b[1] y b[2]
Solo necesito que compare el primer elemento de la lista a[0] con el primer elemento de la lista b[0] y así sucesivamente
Esto lo puedo lograr solo comparando los indices con un if:
>>> if (a.index(i) == b.index(j))
'''

# SOLUCIÓN
def compareTriplets2(a,b):
    alicePoints = 0 # a
    bobPoints = 0   # b
    comparisonPoints = []

    for i in a:
        for j in b:
            # Sí cada elemento de la lista a y b, son mayores que 1 y menores que 100
            if(1 <= i <= 100) & (1 <= j <= 100):
            # Procedemos a comparar los puntos
                # Sí el indice de la lista a es igual al indice de la lista b
                if (a.index(i) == b.index(j)):
                    # Si a[i] > b[i], Alice recibe 1 punto.
                    if (i > j):
                        alicePoints += 1
                    # Si a[i] < b[i], Bob recibe 1 punto.
                    if (i < j):
                        bobPoints += 1
            else:
                print('Los elementos del arreglo deben estar en un rango entre 0 a 100')

    comparisonPoints.append(alicePoints)
    comparisonPoints.append(bobPoints)

    return comparisonPoints

print(compareTriplets2([5,6,7],[3,6,10]))

'''
Encontre una solucion más optima haciendo uso de la función zip:

    a_points = 0
    b_points = 0
    for i,j in zip(a, b):
        if i > j:
            a_points += 1
        elif j > i:
            b_points += 1
        else:
            pass
    return [a_points, b_points]

La función incorporada (no necesita importarse) zip() toma como argumento dos o más objetos iterables
(idealmente cada uno de ellos con la misma cantidad de elementos)
y retorna un nuevo iterable cuyos elementos son tuplas que contienen un elemento de cada uno de los iteradores originales.
'''