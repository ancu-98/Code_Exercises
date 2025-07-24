'''
Completa la función solveMeFirst para calcular la suma de dos enteros.

Ejemplo
a = 7
b = 3

Devuelve 10.

--Descripción de la función

Complete la función solveMeFirst en el editor de abajo.

solveMeFirst tiene los siguientes parámetros

- int a: el primer valor
- int b: el segundo valor

Devuelve
- int: la suma de y

--Restricciones
1 <= a,b <= 1000


--Ejemplo de entrada
a = 2
b = 3

--Muestra de salida
5

--Explicación
2+3=5
'''

def solveMeFirst(a,b):
    # Sí a y b son números mayores que 1 y menores que 1000
    if (1 <= a <= 1000) & (1 <= b <= 1000):
        return a+b
    else:
        return 'Los numeros a y b deben estar en un rango entre 1 a 1000'


print(solveMeFirst(1,999))