#Creando una función que muestre la serie fibonacci entre 0 y el número a ingresar

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b,a+b 

    return fibonacci_lista

resultado = fibonacci(20)
print(resultado)

# ---------------------- CÓDIGO DE PÁGINA ---------------------------

# def fib(n):    # write Fibonacci series up to n
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# def fib2(n):   # return Fibonacci series up to n
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result

# fib(30)
# print("----------------------------")
# valor_fibo2 = fib2(30)
# print(valor_fibo2)