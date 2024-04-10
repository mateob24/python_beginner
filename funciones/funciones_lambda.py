numeros = [1,2,3,4,5,6,7,8,9]

#creando una función lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

# #creando función común que diga si es par o no
# def es_par(num):
#     if(num%2==0):
#         return True
    
# #usando filter con una función común
# numeros_pares = filter(es_par, numeros)
# print(list(numeros_pares))

#CREANDO LO MISMO DE ANTES (ARRIBA) PERO CON FUNCIONES 'lambda'
numeros_pares = filter(lambda numero:numero%2==0, numeros)
print(list(numeros_pares))
