# Variables
entero = 10  # Variable entero de tipo int
flotante = 3.5  # Variable flotante de tipo float
cadena = "Hola, mundo!"  # Variable cadena de tipo str
verdadero = True  # Variable verdadero de tipo bool

# Operadores
suma = entero + flotante  # Suma de las variables entero y flotante
resta = entero - flotante  # Resta de las variables entero y flotante
multiplicacion = entero * flotante  # Multiplicación de las variables entero y flotante
division = entero / flotante  # División de las variables entero y flotante
modulo = entero % 3  # Cálculo del módulo de entero entre 3
comparacion = entero > flotante  # Comparación entre entero y flotante
logica = verdadero and (entero != 0)  # Operación lógica utilizando and

# Estructuras condicionales
if comparacion:
    print("El número entero es mayor que el número flotante.")
elif entero == flotante:
    print("Los números son iguales.")
else:
    print("El número flotante es mayor que el número entero.")

# Bucle while
contador = 0
while contador < 5:
    print("Iteración número:", contador)  # Imprime el número de iteración
    contador += 1  # Incrementa el contador en 1 en cada iteración

# Bucle for
for i in range(5):
    print("Iteración número:", i)  # Imprime el número de iteración

# Mostrar resultados
print("Suma:", suma)  # Imprime el resultado de la suma
print("Resta:", resta)  # Imprime el resultado de la resta
print("Multiplicación:", multiplicacion)  # Imprime el resultado de la multiplicación
print("División:", division)  # Imprime el resultado de la división
print("Módulo:", modulo)  # Imprime el resultado del cálculo del módulo
print("Comparación:", comparacion)  # Imprime el resultado de la comparación
print("Operación lógica:", logica)  # Imprime el resultado de la operación lógica
print(cadena)  # Imprime la cadena de texto almacenada en la variable
print("¿Es verdadero?", verdadero)  # Imprime el valor de la variable verdadero