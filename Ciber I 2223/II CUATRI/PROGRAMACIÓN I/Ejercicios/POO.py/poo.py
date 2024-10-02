#¿como creamos una clase en python? 
class nombreclase:   #definimos la clase. 
    propiedad = 1

#ahora debemos crearla o instanciarla.
obj = nombreclase()
print (type(object))
    #se crea un objeto de tipo nombreclase con todos los datos y metodos definidos en la clase. 

#Generar nuestra primera clase!!!!!
class Saludo: 
    texto = "Hola"
    def saludar (self, name): 
        print (self.texto + " " + name + "!!!!")

p1 = Saludo ()
p1.saludar ("Clase")

class Saludo: 
    def __init__ (self,texto):
        self.texto = texto
    def saludar (self,name):
        print (self.tecto + " " + name + "!!!")
p1 = Saludo ("Hola")
p1.saludar ("Clase")

#modificar una propiedad 

class Saludo:
    def __init__ (self, nombre):
        self.texto = "Hola"