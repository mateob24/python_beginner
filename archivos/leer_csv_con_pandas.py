import pandas as pd

#Usando la función read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv") #df = data-frame
df2 = pd.read_csv("archivos\\datos.csv")

#Obteniendo los datos de la columna nombres
nombres = df["nombre"]

#Ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values('edad')

#Ordenandolo de forma descendente
df_orden_descendente = df.sort_values('edad', ascending=False)

#Concantenando los 2 DATAFRAMES
df_concatenado = pd.concat([df,df2])

#Accediendo a las 3 primeras filas con head()
primeras_filas = df.head(3)

#Accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(2)

#Accediendo a la cantidad de filas y columnas con 'shape'
#aplicando el desempaquetar
filas_y_columnas_totales = df.shape

print(filas_y_columnas_totales)

#--------------------------

# cadena = "0123456789"
# print(cadena[:4]) #izq = posicion de inicio (se incluye) --- der = posicion de final (NO se incluye)

