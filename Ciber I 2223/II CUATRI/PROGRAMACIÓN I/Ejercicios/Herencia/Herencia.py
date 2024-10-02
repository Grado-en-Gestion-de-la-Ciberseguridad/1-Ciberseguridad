#1. Crear la clase Persona, con dos atributos nombre y apellidos.
# 2. Crear un constructor que reciba dos parámetros, el nombre y los apellidos.
# 3. Crear un método ImprimirNombre, que muestre por pantalla el nombre y los apellidos.
# 4. Instancia la clase Persona, con tú nombre y apellidos.

class Persona: 
    def __init__ (self, nom, ape): 
        self. nombre = nom
        self. apellido = ape
    
    def imprimirnombre (self,don=""): 
        print (don + "" + self.nombre + "apellidos:" + self.apellido)

per = Persona ("pepe", "lucas")
per.imprimirnombre ("don")

class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        
    def ImprimirNombre(self):
        print(self.nombre + " " + self.apellidos)

# Instanciando la clase Persona con mi nombre y apellidos
yo = Persona("ChatGPT", "Modelo de lenguaje")

# Llamando al método ImprimirNombre para mostrar mi nombre y apellidos
yo.ImprimirNombre()

#1. Partiendo de la clase Persona anterior, crear la clase Alumno que herede de la clase padre Persona.
# 2. Dentro de la clase Alumno pondremos sólo la palabra pass.
# 3. Instanciar un objeto de tipo alumno.


#1. Crear una variable a = 1 e imprime isinstance(a,int)

# 2. Crear una variable b = “Hola” e imprime isinstance(b,str)
# 3. Crear una variable obj = Persona(“Nombre”, “Apellidos”) e imprime
# isinstance(obj, Persona)
# 4. Crear una variable al = Alumno(“Nombre”, “Apellidos”, “2019-20”) e imprime si
# es una instancia de Persona. Comprueba si es una instancia de Alumno.

class clase1:


