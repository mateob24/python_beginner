#pedir el nombre y la edad de los estudiantes que asistieron el día de hoy a clases

#Función para obtener el asistente y el profesor según la edad
def obtener_estudiantes(cantidad_de_estudiantes):
    #Creando la lista de estudiantes
    estudiantes = []

    #Ejecución del 'for' para pedir información de cada estudiante
    for i in range(cantidad_de_estudiantes):
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        estudiante = (nombre, edad) #ESTO ES UNA TUPLA QUE SE IDENTIFICA POR LOS PARÉNTESIS 

        #Agregando la información a la lista
        estudiantes.append(estudiante)

        #Ordenándolos de menor a mayor según su edad
    estudiantes.sort(key=lambda x:x[1])

    #estudiantes[x] devuelve una tupla con (nombre, edad) y después accedemos al nombre para definir al asistente y al profesor
    asistente = estudiantes[0][0]
    profesor = estudiantes[-1][0]

    #retornamos una tupla (TAMBIÉN PUEDEN IR SIN SUS PARÉNTESIS AL RETORNARLA)
    return asistente, profesor

#desempaquetado de lo que retorna la función (LA TUPLA RETORNADA POR LA FUNCIÓN)
asistente, profesor = obtener_estudiantes(5)

#mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}") #El profesor es quien tiene la mayor edad y su asistente es quien tiene la menor de las edades

