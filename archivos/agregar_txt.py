with open('archivos\\txt_prueba.txt', 'w', encoding="UTF-8") as archivo:
    #agregando texto y/o oraciones al archivo .txt
    # archivo.write("Primer línea del archivo")

    #Usando un bucle para agregar varias lineas 
    for i in range(5):
        archivo.write(f'Línea #{i+1} agregada.\n')
