# Calculadora de Divisores de Números Naturales

Este proyecto consiste en una aplicación que permite al usuario ingresar un número natural y, a partir de ese número, calcula todos sus divisores. Si el usuario ingresa un valor que no es un número natural (como un número negativo, cero o un valor no numérico), se manejará el error mediante excepciones, y se solicitará un nuevo ingreso hasta que el dato sea válido.

## Explicación del Código

### 1. `leer_numero_natural()`
Esta función se encarga de leer un número natural desde la entrada estándar (el teclado). Utiliza un bucle `while` para seguir pidiendo al usuario que ingrese un número válido hasta que el ingreso cumpla con las condiciones necesarias:
- Debe ser un número entero.
- Debe ser mayor que cero.

El manejo de excepciones se realiza con un bloque `try-except`, en el cual si el valor ingresado no es un entero o no cumple con las condiciones, se lanza una excepción `ValueError`, la cual se captura para mostrar un mensaje de error al usuario.

### 2. `calcular_divisores(numero)`
Esta función recibe un número natural como parámetro y se encarga de calcular todos sus divisores. Utiliza un bucle `for` para iterar sobre todos los números desde `1` hasta el número ingresado (inclusive). Cada vez que encuentra un divisor (es decir, un número que divide exactamente al número ingresado sin dejar residuo), lo agrega a una lista que se devolverá al final.

### 3. `main()`
Es la función principal del programa, encargada de controlar el flujo de la aplicación. Primero, llama a `leer_numero_natural()` para obtener el número válido del usuario. Luego, llama a `calcular_divisores()` para obtener los divisores de ese número, y finalmente imprime los divisores en la consola.

### 4. Bloque `if __name__ == "__main__":`
Este bloque se asegura de que la función `main()` solo se ejecute si el archivo es ejecutado directamente, y no cuando es importado como un módulo en otro archivo. Este es un patrón común en Python para definir el punto de entrada de la ejecución del programa.

## Ejemplo de ejecución
Ingrese un número natural: -5 Error: El número debe ser natural (mayor que 0). Inténtelo de nuevo. Ingrese un número natural: abc Error: invalid literal for int() with base 10: 'abc'. Inténtelo de nuevo. Ingrese un número natural: 12 Los divisores de 12 son: [1, 2, 3, 4, 6, 12]

En este ejemplo, el programa sigue solicitando el número hasta que el usuario ingrese un valor válido.
