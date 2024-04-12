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

#Obteniendo data estadística del dataframe:
df_info = df.describe()

#Accediendo al elemento edad en su fila '1' -> uso de 'loc'
elemento_especifico_loc = df.loc[1,"edad"]

#Accediendo al elemento edad en su fila '2' -> uso de 'iloc'
elemento_especifico_iloc = df.iloc[2,2]

#Accediendo a todas las filas de una columna -> uso de 'iloc'
apellidos = df.iloc[:,1]

#Accediendo a toda la fila 3 -> uso de 'loc'
fila_3_loc = df.loc[2,:]

#Accediendo a toda la fila 3 -> uso de 'iloc'
fila_3 = df.loc[2,:]


print(fila_3)

#--------------------------

# cadena = "0123456789"
# print(cadena[:4]) #izq = posicion de inicio (se incluye) --- der = posicion de final (NO se incluye)

