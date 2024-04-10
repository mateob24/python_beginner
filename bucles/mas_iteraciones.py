#CREANDO LAS LISTAS
frutas = ["banano", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "hola mundo"
numeros = [4, 5, 6, 7]

#evitando que se coma una 'granada' con la sentencia 'continue'
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f'La fruta es: {fruta}')

print('---------------------')

#evitar que el bucle se siga ejecutando antes de comer una 'pera' con la sentencia 'break'
for fruta in frutas:
    if fruta == "pera":
        break
    print(f'La fruta es: {fruta}')

#evitar que el bucle se siga ejecutando luego de comer una 'pera' con la sentencia 'break'
for fruta in frutas:
    if fruta == "pera":
        break
    print(f'La fruta es: {fruta}')

print('---------------------')

#recorrer una cadena de texto
for letra in cadena:
    print(letra)

print('---------------------')

# numeros_duplicados = list()
# for numero in numeros:
#     numeros_duplicados.append(numero*2)
# print(numeros_duplicados)

#el 'for' anterior en una sola linea de código (SOLO APLICA EN SITUACIONES RELATIVAMENTE SENCILLAS)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)