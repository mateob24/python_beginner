#Creando una lista (SE PUEDEN MODIFICAR)
lista = ["Mateo Bernal", "Pasante", True, 1.71]

#LAS TUPLAS NO SE PUEDEN MODIFICAR NUNCA
tupla = ("Mateo Bernal", "Pasante", True, 1.71)

#esto es válido:
lista[3] = "Python"

#ESTO NO ES VÁLIDO:
# tupla[3] = "Python"

#Creando un conjunto (set)(NO PERMITE ACCEDER NI CAMBIAR SUS ELEMENTOS POR MEDIO DEL ÍNDICE, NO ALMACENA DATOS DUPLICADOS)
conjunto = {"Mateo Bernal", "Pasante", True, 1.71}

# print(conjunto[3]) -> NO SE PUEDE ACCEDER AL ELEMENTO DEL CONJUNTO

#Creando un diccionario (se hace entre llaves y su estructura es 'key : value' y se separan con comas)
diccionario = {
    'nombre': "Mateo",
    'apellido': "Bernal",
    'edad': 22,
    'estado': True,
    'dato_duplicado': "Mateo"
}

print(diccionario['nombre'])


