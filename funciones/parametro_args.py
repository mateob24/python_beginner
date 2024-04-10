#FORMA NO OPTIMA DE SUMAR VALORES
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados = numeros_sumados + numero
#     return numeros_sumados

# resultado = suma([5,7,8,20])
# print(resultado)

#FORMA ÓPTIMA DE SUMAR VALORES
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,6,7,8,9])
print(resultado2)
print("--------------------")
#LO MISMO DE ARRIBA PERO UTILIZANDO EL OPERADOR '*' COMO ARGUMENTO (*args)
def suma(nombre, *numeros): #EL SIGNO '*' SIRVE PARA que el parámetro ingresado en caso de ser una 'lista' tome cada valor por individual
    return f"{nombre}, la suma de sus números es: {sum(numeros)}"

resultado = suma("Mateo", 5,7,8,9)
print(resultado)