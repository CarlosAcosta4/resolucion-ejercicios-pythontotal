class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    

class Cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta,balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Nombre\t\t\t:{self.nombre}\nApellido\t\t:{self.apellido}\nNúmero de cuenta\t:{self.numero_cuenta}\nBalance\t\t\t:{self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("*********Monto depositado*********\n")

    def retirar(self, monto_retiro):
        if self.balance < monto_retiro:
            print("*******Fondos Insuficientes*******\n")
        else:   
            self.balance -= monto_retiro
            print("*********Monto retirado***********\n")
       

def clearCliente():
    nombre = input("Ingrese su nombre\t: ")
    apellido = input("Ingrese su apellido\t: ")
    numCuenta = input("Ingrese su numero cuenta: ")
    persona1 = Cliente(nombre, apellido, numCuenta)
    return persona1

def inicio():
    mi_cliente = clearCliente()
    opc = " "
    while opc != "S":
        print("----------------------------------")
        print("""Elige:
            Depositar\t(D)
            Retirar\t(R)
            Salir\t(S)""")
        print("----------------------------------")
        opc = input("---->").upper()
        print("----------------------------------")
        if opc == "D":
            montoDep = int(input("Ingrese el monto para depositar: "))
            print("----------------------------------")
            os.system("cls")
            mi_cliente.depositar(montoDep)
            print(mi_cliente)
        elif opc == "R":
            montoRet = int(input("Ingrese el monto para retirar: "))
            print("----------------------------------")
            os.system("cls")
            mi_cliente.retirar(montoRet)
            print(mi_cliente)
    print("----------------------------------")
    print("Gracias por operar en Banco Python")
            




import os
os.system("cls")

inicio() 
    



