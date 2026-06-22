# Trabajo Práctico Integrador - Gestión de Países

Trabajo Práctico Integrador para la materia Programación 1 (Tecnicatura Universitaria en Programación). Desarrollamos una aplicación de consola en Python que gestiona datos de países guardados en un archivo CSV. El sistema permite agregar registros, actualizar información, filtrar por criterios, ordenar y ver datos estadísticos del dataset.

## Video de la Demostración
Link al video: https://www.youtube.com/watch?v=w3d34zo2gyk

## Integrantes
* Lucas lautaro jerez condori
* Elias Vargas

## Funcionalidades del programa

El código está dividido en módulos para separar la interfaz de usuario, las funciones de procesamiento y la lectura del archivo. Desde el menú principal se puede:

1. Ver la lista completa de países en formato de tabla.
2. Cargar un país nuevo validando que no queden datos vacíos ni duplicados.
3. Actualizar la población y superficie de un país ya existente.
4. Buscar países por coincidencia de texto en el nombre.
5. Filtrar la lista por continente, rango de población o rango de superficie.
6. Ordenar el dataset por nombre, población o superficie (de forma ascendente o descendente) usando el método de selección.
7. Ver estadísticas detalladas: máximos y mínimos de población, promedios y total de países por continente.
8. Borrar un país: Elimina un registro completo del sistema por su nombre.
9. Salir del programa: cierra la aplicación de forma segura.

## Cómo correr el programa

Para ejecutar la aplicación hay que clonar el repositorio, asegurarse de que el archivo `paises.csv` esté en la misma carpeta que los scripts de Python y correr el archivo principal desde la terminal:

```bash
python TP.py
```

### Ejemplo:
```text
=== SISTEMA DE GESTIÓN DE PAÍSES ===
1. Mostrar todos los países
2. Agregar país
3. Actualizar datos de un país
...
Seleccione una opción: 7

Mayor Población: Brasil (213993437)
Menor Población: Alemania (83149300)
Promedio Población: 132145322.00
Promedio Superficie: 3004902.50 km²
```
