#Abriendo el archivo con 'with open'
with open("archivos\\txt_prueba.txt", encoding="UTF-8") as archivo:
    #Leemos el archivo
    contenido = archivo.read()

    #Mostramos
    print(contenido)

#NO ES NECESARIO CERRARLO (funcion .close) AL USAR 'with open'