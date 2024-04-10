#Creando un función que devuelva los números primos entre 0 y el argumento que ingresemos (número)

#Crear una función que verifique si un número es primo
def es_primo(num):
    #Verificamos que el número ingresado no pueda dividirse por ningún
    #número entre 2 y el mismo número ingresado pero -1
    for i in range(2, num-1):
        #Si es divisible por alguno retornamos 'false' y termina el bucle
        if num%i==0: return False
    #Si termina el bucle, significa que no fue divisible entonces es primo
    return True

#Creando función que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos = []
    for i in range(3, num+1): #EL '+1' ES PARA QUE INCLUYA EL NÚMERO INGRESADO
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de ser primo lo agregamos a la lista
        if resultado == True: primos.append(i)
    #se devuelve o retorna la lista
    return primos

#Creamos el resultado llamando a la función y lo mostramos 
resultado = primos_hasta(22)
print(resultado)


