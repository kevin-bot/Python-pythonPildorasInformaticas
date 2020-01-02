'''Es un error en tiempo de ejecucion, la sintaxis del codigo es correcta pero durante la ejecucion ha ocurrido "algo inseperado " '''

'''El problema es que en los lenguajes que ejecutan el codigo asia abajo, una vez que el rpgrama nos da error el resto de lineas no se ejecutan  '''

def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def divide(num1,num2):
    try:
        return  num1/num2
    except ZeroDivisionError:
        print("No se puede vividir entre 0")
        return "Operacion erronea"

while(True):
    try:
        op1=(int(input("introduce el primer valor: ")))
        op2=(int(input("introduce el segundo valor: ")))
        break
    except ValueError:
        print("Los valores intorducidos no  son correctos ")

operacion=input("introduce la operacion a realizar(suma, resta, multiplicacion, divide)")

if operacion =="suma":
    print(suma(op1,op2))
elif operacion == "resta":
    print(resta(op1,op2))
elif operacion == "multiplicacion":
    print(multiplicacion(op1,op2))
elif operacion == "divide":
    print(divide(op1,op2))
else :
    print(f"Operacion no contemplada ")

print("Ejecucion del programa finalizada : continua con el progra")