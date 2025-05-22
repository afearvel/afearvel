class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def mostrar_saldo(self):
        print(f"Saldo: {self.__saldo}")

    def depositar(self, cantidad):
        self.__saldo += cantidad

mi_cuenta = CuentaBancaria(100)
mi_cuenta.mostrar_saldo() 
