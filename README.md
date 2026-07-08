# Instancias del Problema de la Mochila
## Análisis Masivo de Datos Biológicos
### Plaza de Ayudante Doctor cod. 7948
### Departamento de Biotecnología
### Universitat Politècnica de València UPV2026

Este repositorio contiene tests para el problema de la mochila (knapsack problem 0-1) seleccionados del repositorio de [KPlib](https://github.com/likr/kplib/tree/master), de Yosuke Onoue (Nihon University). 

Cada fichero contiene una instancia del problema en el siguiente formato:

```
n
c

p_1 w_1
p_2 w_2
…
p_n w_n
```

Donde n es el número de objetos a elegir, c es la capacidad de la mochila, p_1, p_2, etc son los precios de los objetos, y w_1, w_2, etc son sus pesos.

El problema consiste en seleccionar la combinación de objetos que maximizan el valor total, sin sobrepasar la capacidad de la mochila.