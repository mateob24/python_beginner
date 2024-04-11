#Importando un modulo y asignándole un nombre con 'as' como 'm_saludar'
# import modulo_saludar as m_saludar

#Cuando el módulo está en otra carpeta pero en la misma ruta se importa así:
# import nombre_carpeta.modulo_saludar as m_saludar

#Desde ese módulo importamos directamente dos funciones
from modulo_saludar import saludar, saludar_ingles

#Creación de variables para almacenar los saludos con los nombres escritos
saludo = saludar("Mateo")
saludo_ingles = saludar_ingles("Max")

#Imprimimos o mostramos los resultados
# print(saludo)
# print(saludo_ingles)

#Para ver las propiedades y métodos de el namespaces
# print(dir(m_saludar))

#Accedemos al nombre del módulo importado o llamado
# print(m_saludar.__name__)

