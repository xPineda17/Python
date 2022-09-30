def suma(a,b):
    total = a + b
    print("El resultado de la suma es:",total)
def resta(a,b):
    total = a - b
    print("El resultado de la resta es:",total)
def multiplicacion(a,b):
    total = a * b
    print("El resultado de la multiplicacion es:",total)
def division(a,b):
    total = a / b
    print("El resultado de la division es:",total)

op = input("¿Que tipo de operación necesita(suma,resta,multiplicacion,division)?:")
if op == "suma":
    dato1 = int(input("Ingrese el primer dato: "))
    dato2 = int(input("Ingrese el segundo dato: "))
    suma(dato1, dato2)
elif op == "resta":
    dato1 = int(input("Ingrese el primer dato: "))
    dato2 = int(input("Ingrese el segundo dato: "))
    resta(dato1, dato2)
elif op == "multiplicacion":
    dato1 = int(input("Ingrese el primer dato: "))
    dato2 = int(input("Ingrese el segundo dato: "))
    multiplicacion(dato1, dato2)
elif op == "division":
    dato1 = int(input("Ingrese el primer dato: "))
    dato2 = int(input("Ingrese el segundo dato: "))
    division(dato1, dato2)
else:
    print("Error, verifique la información")