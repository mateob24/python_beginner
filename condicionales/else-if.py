ingreso_mensual = 50000
gasto_mensual = 20000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Hay pérdida de dinero")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Está bien económicamente")
    else:
        print("Gasta mucho")
        
elif ingreso_mensual > 5000:
    print("Ingreso mensual mínimo")

else:
    print('No tiene ingreso mensual')