"""Antes de iniciar el codigo, se que no lo requiria, pero al indicar una opcion
del menu, se seguía mostrando por pantalla lo anterior, es deir que se acumulaba.
Para ello he usado el modulo os, que ha permitido borrar la pantalla antes de imprimir
nueva informacion por pantalla. Es una posible mejora de mi codigo."""
import os

class Almacen:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cantidad = 0

    def porcentaje_carga(self):
        return self.cantidad / self.capacidad * 100

    def agregar_cantidad(self, cantidad):
        if self.cantidad + cantidad <= self.capacidad:
            self.cantidad += cantidad
            return cantidad
        else:
            espacio_disponible = self.capacidad - self.cantidad
            cantidad_almacenada = min(cantidad, espacio_disponible)
            cantidad_desechada = cantidad - cantidad_almacenada
            self.cantidad += cantidad_almacenada
            return cantidad_almacenada, cantidad_desechada


class Cargamento:
    def __init__(self, tipo, mineral=0, gas=0):
        self.tipo = tipo
        self.mineral = mineral
        self.gas = gas

    def __str__(self):
        if self.tipo == 'envio':
            return f"Cargamento enviado: {self.mineral} unidades de mineral y {self.gas} unidades de gas"
        elif self.tipo == 'recepcion':
            return f"Cargamento recibido: {self.mineral} unidades de mineral y {self.gas} unidades de gas"


class Historico:
    def __init__(self):
        self.cargamentos = []

    def agregar_cargamento(self, cargamento):
        self.cargamentos.append(cargamento)

    def mostrar_cargamentos(self):
        for cargamento in self.cargamentos:
            print(cargamento)


capacidad_gas = 120000
capacidad_minerales = 200000
almacen_gas = Almacen(capacidad_gas)
almacen_minerales = Almacen(capacidad_minerales)
historico_cargamentos = Historico()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""¡Bienvenido al planeta Umoja! En este programa puedes gestionar los recursos disponibles en el planeta.
Aquí va el menú de opciones:
1 - Ver Estado de Almacenes
2 - Añadir mineral
3 - Añadir gas
4 - Enviar cargamento
5 - Recibir cargamento
6 - Histórico de cargamentos""")
    respuesta = input("Ingresa el número del menú:")

    # Opcion 1 - Estado almacenes
    if int(respuesta) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Estado de Almacenes")
        print("Gas:", almacen_gas.porcentaje_carga(), "%")
        print("Minerales:", almacen_minerales.porcentaje_carga(), "%")
        input("Presiona Enter para continuar...")

    # Opcion 2 - Añadir mineral
    elif int(respuesta) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        cantidad = int(input("Ingresa la cantidad de mineral que deseas agregar: "))
        cantidad_almacenada, cantidad_desechada = almacen_minerales.agregar_cantidad(cantidad)
        print("Se agregaron", cantidad_almacenada, "unidades")
        print("Se desecharon", cantidad_desechada, "unidades")
        input("Presiona Enter para continuar...")

    # Opcion 3 - Añadir gas
    elif int(respuesta) == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        cantidad = int(input("Ingresa la cantidad de gas que deseas agregar: "))
        cantidad_almacenada, cantidad_desechada = almacen_gas.agregar_cantidad(cantidad)
        print("Se agregaron", cantidad_almacenada, "unidades")
        print("Se desecharon", cantidad_desechada, "unidades")
        input("Presiona Enter para continuar...")

    # Opcion 4 - Enviar cargamento
    elif int(respuesta) == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        confirmacion = input("¿Estás seguro de que quieres enviar el cargamento? (s/n): ")
        if confirmacion.lower() == "s":
            if almacen_minerales.cantidad >= 150000 and almacen_gas.cantidad >= 60000:
                almacen_minerales.cantidad -= 150000
                almacen_gas.cantidad -= 60000
                cargamento = Cargamento('envio', 150000, 60000)
                historico_cargamentos.agregar_cargamento(cargamento)
                print("Se ha enviado el cargamento.")
            else:
                print("No hay suficientes recursos para enviar el cargamento.")

    # Opción 5 - Recibir cargamento
    elif int(respuesta) == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        satelite_origen = input("Ingresa el nombre del satélite de origen: ")
        fecha = input("Ingresa la fecha de recepción(d/m/año): ")
        cantidad_mineral = int(input("Ingresa la cantidad de mineral recibido: "))
        cantidad_gas_recibido = int(input("Ingresa la cantidad de gas recibido: "))
        cantidad_mineral *= 0.9  # Se reduce un 10% por los contenedores
        cantidad_gas_recibido *= 0.9  # Se reduce un 10% por los contenedores
        cantidad_gas_almacenado, cantidad_gas_desechado = almacen_gas.agregar_cantidad(cantidad_gas_recibido)
        cantidad_mineral_almacenado, cantidad_mineral_desechado = almacen_minerales.agregar_cantidad(cantidad_mineral)
        cargamento = Cargamento('recepcion', cantidad_mineral_almacenado, cantidad_gas_almacenado)
        historico_cargamentos.agregar_cargamento(cargamento)
        print("Cargamento recibido correctamente.")
        input("Presiona Enter para continuar...")

    # Opción 6 - Histórico de cargamentos
    elif int(respuesta) == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Histórico de Cargamentos")
        historico_cargamentos.mostrar_cargamentos()
        input("Presiona Enter para continuar...")




    

 









