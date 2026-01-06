Proyecto de algoritmo genético Mastermind
=========================================

# Indice

- Introducción
- Manual






# Introducción

El proyecto incluye codigo, para un programa que resuelve el juego de mastermind mediante un algoritmo genético.

Este proyecto esta hecho por:
- Gabriel Rodríguez Gil
- Miguel Gutierrez Pahino

# Manual

## Instalación

1. Descargar el proyecto de GitHub:
    
    ![alt text](assets/img_readme/image.png)

    Descargamos el zip, lo descomprimimos y abrimos la carpeta del proyecto con el editor de codigo que se use.

2. Descargamos las dependencias
    
    Como el proyecto esta configurado con uv, solo tendremos que ejecutar en nuestra terminal del proyecto, "uv sync". Con esto, se creará el entorno virtual y se descargaran las dependencias.

3. Activar el entorno virtual

    Para activar el entorno en Windows usaremos: `.\.venv\Scripts\activate.ps1`

    De otra manera para activar el entorno en Linux usaremos: `source .venv/bin/activate`

## Uso

Para su uso solo hay que abrir el directorio donde se encuentra el proyecto y ejecutar `python main.py`.
Tras ejecutarlo te pedirá una combinación con los colores posibles y te mostrará todos los intento y su puntuación.

## Metodología

La metodología empleada en este caso fue **TDD** , en los módulos que se utilizaban random hemos usado **Property-Based Testing** para controlar si el tipo de resultado que da es el adecuado

También hemos usado **Scrum** como marco de trabajo durante todo el proyecto.

## Historias de usuario

Para las historias de usuario hemos usado la herramienta que da GitHub de "Projects" para ver nuestras historias de usuarios y poder planificarlas apropiadamente. 
Las historias de usuarios son las siguientes:

- El jugador uno empieza eligiendo un código de colores para pasarlo por la terminal y que el jugador dos lo resuelva.

- Como jugador quiero ver una representación gráfica de los colores del código para identificar fácilmente cada ficha y entender el estado del juego.

- El jugador dos quiere crear una gran cantidad de posibles respuestas para poder calcular la mejor solución.

- El jugador dos calcula la puntuación del acierto de un intento comparado con la solución para poder luego comparar resultados en un futuro.

- El jugador dos seleccionará una lista de padres de manera estocástica según la probabilidad de ser más cercanos a la respuesta, todo para que puedan tener unos hijos con un resultado más cercano a la respuesta. 

- El jugador dos reproduce a los padres para generar nuevas combinaciones.
  
- El jugador dos crea una nueva generación eliminando de forma estocástica parte de las combinaciones para que la población se pueda parecer más al resultado.

- El jugador uno quiere que el jugador 2 calcule la solución del mastermind.

## Arquietectura

## Diseño

    
