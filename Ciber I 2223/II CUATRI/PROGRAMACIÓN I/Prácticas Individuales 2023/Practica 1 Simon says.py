import os
import random
import time

print("Bienvenid@ al juego de Simón dice, espero que tengas buena memoria")
print("Acuerdate de esto que te estoy diciendo! ;)")
print("Estas preparado?, si lo estás escribe START.")

respuesta = input()

if respuesta == "START":
    print("Comenzamos!")
    print ("Estate muyyy atento!!!!")
    print ("Suerte!")

    # INSTRUCCIONES Y CONFIGURACIÓN...
    print("Antes de todo te voy a explicar las instrucciones del juego")  
    print ("INSTRUCCIONES")
    print("1. Se mostrarán 4 colores básicos, green, red, yellow y blue.")
    print("2. Debes recordar esa secuencia y escribirla.")    
    print("4. En cada ronda se muestra una combinación de colores de forma aleatoria, por cada ronda 1 color, a la 2da ronda serán 2 colores, a la 3era 3...")
    print("3. Puedes jugar tantas rondas como quieras, por defecto son 10, pero puedes modificarlas antes de empezar a jugar o dejar las que están por defecto.")
    print("OJO!, que solo estará el color durante 5 segundos, después se borrará así que estate atent@!")

    # CONFIGURACIÓN
    def configuracion():
        rondas = 10
        while True:
            print(f"El número de rondas por defecto es {rondas}.")
            respuesta = input("¿Desea cambiar el número de rondas? Escriba 'Si' o 'No': ")
            if respuesta.lower() == 'si':
                while True:
                    try:
                        rondas = int(input("Ingrese el número de rondas que desea jugar: "))
                        if rondas > 0:
                            break
                        else:
                            print("El número de rondas debe ser mayor que cero.")
                    except ValueError:
                        print("El número de rondas debe ser un número entero.")
            elif respuesta.lower() == 'no':
                break
            else:
                print("La respuesta debe ser 'Si' o 'No'.")
        return rondas

    print("Comienza el juego...!! Suerteeee")

    colores = ['green', 'red', 'yellow', 'blue']
    rondas = configuracion()
    acierto = True

    for ronda in range(1, rondas+1):
        print(f"Ronda {ronda}")
        secuencia = random.choices(colores, k=ronda)
        print(secuencia)
        time.sleep(5)  # Aquí el número es el tiempo que se muestra por pantalla los colores. 
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
        respuesta = input("Escribe los colores separados por comas: ").split(",")
        respuesta = [r.strip() for r in respuesta]  # Elimina los espacios al inicio y al final de cada color
        if respuesta != secuencia:
            acierto = False
            break

    if acierto:
        print("Genial, eres un crack, has ganado jejejeje!!")
    else:
        print("Lo siento, has perdido. Vuelve a intentarlo.")

while True:
        print("¿Qué quieres hacer ahora?")
        print("1. Ver puntuación")
        print("2. Volver a jugar")
        print("3. Salir del juego")
        respuesta = input()
        if respuesta == "1":
            print(f"Tu puntuación es de {ronda-1} ronda(s) completadas.")
        elif respuesta == "2":
            print("Comenzamos de nuevo!")
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla según el sistema operativo
            break  # Vuelve a jugar
        elif respuesta == "3":
            print("Gracias por jugar, ¡hasta la próxima!")
            exit()  # Sale del juego
        else:
            print("Por favor, elige una opción válida.")
