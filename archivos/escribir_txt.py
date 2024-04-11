with open('archivos\\txt_prueba.txt', 'w', encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo .txt
    # archivom.write("Texto prueba")

    #Para escribir en el .txt varias cadenas de texto se deben incluir dentro de una lista. Para permitir que divida 
    #las oraciones en distintas línas se usa '\n' al final de la cadena de texto anterior a la que deseamos bajar de línea

    #Agregar 2 líneas con writelines
    archivo.writelines(["Primer línea del archivo\n", "Segunda línea del archivo\n"])

    #Agregar otras 2 líneas con writelines

    archivo.writelines(["Tercer línea del archivo\n", "Cuarta línea del archivo\n"])
