# Rects in a Grid 0.1.0
![Tests](https://github.com/sertemo/DesafioAidTecSolutions/actions/workflows/tests.yml/badge.svg)

## ¿ Cuántos rectángulos caben en una cuadrícula de 5 x 5 ?

## Recursos
Se usa **pygame 2.5.2** para la visualización

Se usa [Nuitka](https://pypi.org/project/Nuitka/) para la compilación. En Windows:

```sh
$ python -m nuitka --standalone --onefile --mingw64 main.py
```

## Descripción
Dada una cuadrícula de 5 x 5, el programa crea todos los posibles rectángulos permutando un rango de números de 1 a 5 en combinaciones de 2.

Cada rectángulo se posiciona en la casilla superior izquierda y se va desplazando de 1 en 1 casilla hasta completar todo el recorrido por la cuadrícula.

Cada movimiento es registrado en un contador.

Al final de todos los recorridos el contador devolverá el número de rectángulos posibles dentro de la cuadrícula.

![alt text](images/image-1.png)

## Uso
Descarga de la carpeta **data** el archivo `rectsingrid.exe`.

Ejecuta el archivo haciendo doble clic. Esto abrirá una cuadrícula por defecto de 5x5.

Si quieres personalizar la cuadrícula, abre una consola y ejecuta el archivo pasándole el argumento **size**.

Si quieres personalizar la velocidad, utiliza el argumento **speed**.

Si quieres personalizar el color, utiliza el argumento **color**.

Ejemplo en **bash**:

```bash
$ ./rectsingrid.exe --size 8 --color verde --speed 7
```

Ejemplo en **PowerShell**:

```powershell
> ./rectsingrid.exe --size 8 --color verde --speed 7
```

Para ver la ayuda:
```bash
$ ./rectsingrid.exe --help
```

De momento el tamaño está limitado entre 2 y 10. Obviamente una cuadrícula de 1 no tiene rectángulos posibles.

## Updates
- 26/04/2024
    - Se añade la posibilidad de adaptar la cuadrícula a la dimensión que se quiera (cuadrada)
    - Se ha empaquetado la aplicación para que pueda recibir argumentos con consola al ejecutar el archivo principal

- 27/04/2024
    - Se implementa posibilidad de utilizar flag **--color** para personalizar el color de los rectángulos. Los colores permitidos son: **verde**, **naranja**, **azul**, **rojo**, **verde**.
    - Se implementa la flag **--speed** para personalizar la velocidad de los rectángulos

- 29/04/2024
    - Intento de agregar un icono al programa compilado con nuitka: https://nuitka.net/user-documentation/user-manual.html#icons pero no se ejecuta. No sé si es error de Nuitka o de mi ordenador.

## Posibles mejoras
Poner contador de tiempo tardado

Poner contador de tipos de rectángulos estáticos distintos (permutaciones)