animales = ['gato', 'perro', 'loro', 'cocodrilo']
numeros = [52,16,14,72]

#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

#recorriendo la lista numeros y cada valor multiplicandolo por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

for numero, animal in zip(numeros, animales):
    print(f'Recorriendo la lista 1 {numero}')
    print(f'Recorriendo la lista 2 {animal}')

#PARA 'range' con dos parámetros EL PRIMER PARÁMETRO ES DESDE DONDE ARRANCA Y EL SEGUNDO ES DONDE TERMINA
for num in range(5,10):
    print(num)

#FORMA CORRECTA DE RECORRER UNA LISTA CON SU ÍNDICE
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El índice es: {indice} y el valor es: {valor}')

#USANDO EL 'else' EN UN for
for numero in numeros:
    print(f'Ejecutando el último bucle, valor actual: {numero}')
else:
    print('El bucle terminó.') #SIEMPRE SE VA A EJECUTAR COMO MÍNIMO UNA VEZ ESTE 'else'

###TODO EL CÓDIGO ANTERIOR PUEDE USARSE EXACTAMENTE IGUAL PARA LAS 'tuplas' Y TAMBIÉN PARA LOS 'conjuntos'