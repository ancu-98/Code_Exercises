'''
Detalle de la escalera

Esta es una escalera de tamaño n = 4:

   #
  ##
 ###
####

Su base y su altura son iguales a: n.

Se dibuja utilizando símbolos # y espacios.
La última línea no va precedida de ningún espacio.

Escribe un programa que imprima una escalera de tamaño n.

--Descripción de la función

Complete la función staircase con los siguientes parámetros:

* int n: un número entero

--Imprimir
Imprima una escalera como se describe anteriormente.
No se debe devolver ningún valor.

Nota: La última línea no va precedida de espacios.
Todas las líneas están alineadas a la derecha.

--Formato de entrada
Un único entero, n, que indica el tamaño de la escalera.

-- Restricciones
0 < n <= 100

-- Ejemplo de Entrada
6

-- Ejemplo de Salida
     #
    ##
   ###
  ####
 #####
######

--Explicación
La escalera está alineada a la derecha, compuesta por símbolos # y espacios, y tiene una altura y anchura de n = 6.
'''

##PRIMER SOLUCIÓN
'''
--Diseño de solución
Si n = 6

Necesito que la matriz se vaya llenando:

matriz = [' ',' ',' ',' ',' ','#']
matriz = [' ',' ',' ',' ','#','#']
matriz = [' ',' ',' ','#','#','#']
matriz = [' ',' ','#','#','#','#']
matriz = [' ','#','#','#','#','#']
matriz = ['#','#','#','#','#','#']

Debo crear una sola matriz de tamaño n y en cada iteración solo imprimo esa línea de la matriz

¿Cómo calculo cuantos espacios ' ' y cuantos '#' debo meter en la matriz?
- En la primer iteracion 5 espacios y 1 # -> En la primer línea
- En la primer iteracion 4 espacios y 2 # -> En la segunda línea
Y así sucesivaamente hasta que la matriz se llene

Por cada iteración debo hacer dos inserciones una de espacios ' ' y otra de '#'.

PRIMER INSERCIÓN
Puedo contar el número de espacios la operación:
-Primer iteración
n = 6
n - 1 = 5
-Segunda iteración
n = 5
n - 1 = 4 -> Así puedo obtener el número de espacios ' ' que debo ingresar en cada línea de la matriz

SEGUNDA INSERCIÓN
Ahora para optener el número de '#'
contador = 0
-Primer iteración
contador + 1
contador = 1

-Segunda iteración
contador + 1
contador = 2

Lo puedo manejar simplemente con 2 contadores:
uno que decrece en 1 y es igual a n -> para los espacios
otro que aumenta en 1 -> para los #

Las inserciones las puedo concatenar en un string llamado línea, que se imprime en cada iteración

'''

def staircase(n):

    for i in range(1, n + 1):
        # Calcular espacios necesarios: n - i
        espacios = n - i
        # Calcular símbolos # necesarios: i
        simbolos = i

        # Crear la línea con espacios + símbolos #
        linea = ' ' * espacios + '#' * simbolos
        print(linea)

    return

staircase(6)

