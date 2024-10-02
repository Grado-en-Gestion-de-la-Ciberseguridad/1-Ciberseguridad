#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!
print ("¡Hola Mundo!")

#Escribir un programa que almacene la cadena "¡Hola Mundo! en una variable"
# y luego muestre por pantalla el contenido de la variable

variable = "¡Hola mundo!"
print (variable)
#Escribir un programa que pregunte el nombre del usuario en
#  la consola y después de que el usuario lo introduzca muestre por pantalla 
# la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre = input ("Introduce tu nombre:")
print ("¡Hola" + nombre + "!")

#Escribe un programa que muestre por pantalla el resultado de la siguiente
#operación aritmética ((3+2)/(2*5)**2)

print(((3 + 2) / (2 * 5)) ** 2)

#Escribe un programa que pregunte al usuario por el numero de horas trabajadas
#y el coste por hora. Debe mostrar por pantalla la paga que le corresponde. 
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
print("Tu paga es", paga)

