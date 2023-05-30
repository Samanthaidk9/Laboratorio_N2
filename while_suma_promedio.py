
#se crea una lista vacia llamada numeros para almacenar los numeros enteros ingresados por el usuario
numeros = []

#se declara la variable suma y se le da el valor de cero.
suma = 0

#se crea un bucle while para solicitar valores enteros al usuario 
#de manera repetitiva hasta que se ingrese un valor no numérico.
while True:
    try:
        valor = int(input("Ingresa un número entero (o un valor no numérico para salir): "))
        numeros.append(valor)
        suma += valor
    except ValueError:
        break

promedio = suma / len(numeros)
#mostrar suma de los numeros enteros digitados por el usuario.
print("La sumatoria de los números digitados es:", suma)

#mostrar promedio de la suma de los enteros digitados.
print("El promedio de los números digitados es:", promedio)
