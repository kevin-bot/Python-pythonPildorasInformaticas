
def divide():
    try:
        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))
        print("la division es: "+ str(op1/op2))
    #en caso de que sean muchos errores posemos solo poner except: sin decirle que error es
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("Error no se puede devidir entre cero")
    finally:
        print("Calculofinalizado")#esta instruccion siempre se va a ejecutar


divide()