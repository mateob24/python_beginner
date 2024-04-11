#Usando 'open' para abrir un archivo con una codificación universal (UTF-8)
archivo = open("archivos\\txt_prueba.txt", encoding="UTF-8") #-> 'encoding="UTF-8" para reconocer caracteres especiales

#Lectura del archivo completo
archivo = archivo.read() #LA FUNCIÓN BUILD-IN 'read()' PERMITE LA LECTURA DEL CONTENIDO DEL TEXTO '.txt'

#Leer linea por linea
# lineas = archivo.readlines()
# print(lineas)

#Leer una sola línea
# linea = archivo.readline() #Si esto no lee una línea lo que hace es leer la cantidad de caracteres que se ingresen y se indiquen
# print(linea)

#Cerrar el archivo
archivo.close()

print(archivo)