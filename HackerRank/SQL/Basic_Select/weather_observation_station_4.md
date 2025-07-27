Encuentre la diferencia entre el número total de entradas CITY en la tabla y el número de entradas CITY distintas en la tabla.

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

Por ejemplo, si hay tres registros en la tabla con valores:
* CITY «Nueva York»
* «Nueva York»
* «Bengalaru»

Hay dos nombres de ciudades diferentes: «Nueva York» y «Bengalaru».

La consulta devuelve 1 porque:

'total number of records - number of unique city names 3 - 2 = 1'

## Solution

```SQL
SELECT COUNT(city) - COUNT(DISTINCT(city)) AS 'duplicated_city_count' FROM STATION;
```
