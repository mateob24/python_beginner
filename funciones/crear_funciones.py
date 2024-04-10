# #creado una función simple
# def saludar():
#     print('Hola Mateo')

# #ejecutando la función simple
# saludar()

#crear una función con parámetros (variable, que es solo válida dentro de la función)
def saludar(nombre,sexo):
    sexo = sexo.lower() #convierte todo a minúsculas 
    if (sexo == 'mujer'):
        adjetivo = 'bella'
    elif (sexo == 'hombre'):
        adjetivo = 'mostro'
    else:
        adjetivo = 'amistad'

    print(f'Hola {nombre}, ¿cómo está {adjetivo}?')

saludar('Mateo', 'hombre')
saludar('Mari', 'NA')
print("----------------------")

#crear una función que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 4
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*3}"
    return contraseña, num #se puede retornar una tupla sin necesidad de los paréntesis

#Desempaquetando la función 
password, primer_numero = crear_contraseña_random(5)

#Mostrando los resultados obtenidos y los datos utilizados para obtenerlos
print(f"Tu contraseña nueva es: {password}")
print(f"El número utilizado para crear la nueva contraseña es: {primer_numero}")


