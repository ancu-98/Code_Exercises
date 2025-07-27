Consulte las dos ciudades de STATION con los nombres CITY más cortos y más largos, así como sus respectivas longitudes (es decir, el número de caracteres del nombre). Si hay más de una ciudad más pequeña o más grande, elija la que aparezca primero en orden alfabético.

La tabla STATION se describe de la siguiente manera:

## TABLE

|--------------------------|
|        STATION           |
|--------------------------|
| Field    | Type          |
|----------|---------------|
| ID       | NUMBER        |
| CITY     | VARCHAR2(21)  |
| STATE    | VARCHAR2(2)   |
| LAT_N    | NUMBER        |
| LONG_W   | NUMBER        |

donde LAT_N es la latitud norte y LONG_W es la longitud oeste.

### Entrada de ejemplo

Por ejemplo, CITY tiene cuatro entradas: DEF, ABC, PQRS y WXY.

### Salida de ejemplo

```SQL
ABC 3
PQRS 4
```
### Explicación

Cuando se ordenan alfabéticamente, los nombres de las CIUDADES aparecen como: (city, longitud)

ABC 3
DEF 3
PQRS 4
WXY 3

El nombre más largo es PQRS, pero hay  opciones para la ciudad con el nombre más corto. Elija ABC, porque es la primera en orden alfabético.

'Nota'
Puede escribir dos consultas separadas para obtener el resultado deseado. No es necesario que sea una sola consulta.

## Solution

```SQL
-- Aquí me muestra todas las ciudades con su respectiva longitud en orden alfabético
SELECT city, LENGTH(city) AS 'total_character' FROM STATION
ORDER BY city ASC;

-- Estas son las consultas de la solución:

-- Para obtener la ciudad con el número de caracteres mas bajo
SELECT city, LENGTH(city) AS 'fewer_character_city' FROM STATION
WHERE LENGTH(city) = (
    SELECT MIN(LENGTH(city))
    FROM STATION
)
ORDER BY city
LIMIT 1;

-- Para obtener la ciudad con el número de caracteres más alto
SELECT city, LENGTH(city) AS 'more_character_city' FROM STATION
WHERE LENGTH(CITY) = (
    SELECT MAX(LENGTH(CITY))
    FROM STATION
)
ORDER BY CITY
LIMIT 1;
```
