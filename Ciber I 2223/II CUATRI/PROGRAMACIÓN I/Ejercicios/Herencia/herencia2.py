##CLASE PADRE O BASE
#1. Creamos la clase Persona, con dos atributos; nombre y apellido. 
#2. Crea un constructor que reciba dos parámetros, el nombre y los apellidos. 
# __init__recibe dos parámetros, nombre y apellidos, 
#que se asignan a los atributos de instancia self.nombre y self.apellidos.
#3. Crea un método ImprimirNombre, que muestre por pantalla el nombre y apellidos.
#4. Instancia la clase Persona, con tu nombre y apellidos. 
class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def imprimir_nombre(self):
        print(f"{self.nombre} {self.apellidos}")

# Instanciación de la clase Persona con mi nombre y apellidos
yo = Persona("Xia", "Martinez")
yo.imprimir_nombre()

##CLASE HIJA O DERIVADA
#1. Partiendo de la clase Persona anterior, crear la clase Alumno que herede 
# de la clase padre Persona.
# 2. Dentro de la clase Alumno pondremos sólo la palabra pass.
# 3. Instanciar un objeto de tipo alumno.
class Alumno(Persona):
    pass
#1. Crear la clase Padre1, que tenga un método Imprimir1 que muestre el
# texto “Padre1 llamado”.
# 2. Crear la clase Padre2, que tenga también un método Imprimir2 que
# muestre el texto “Padre2 llamado”.
# 3. Crear una clase hija llamada Hija, que herede de Padre1 y de Padre2,
# esta clase debe tener un método Imprimir que llame a los métodos
# Imprimir1 e Imprimir2.
# 4. Instancia la clase y observa el resultado.

# Instanciación de la clase Alumno
alumno = Alumno("Juan", "Pérez")
alumno.imprimir_nombre()


class Padre1:
    def imprimir1(self):
        print("Padre1 llamado")

class Padre2:
    def imprimir2(self):
        print("Padre2 llamado")

class Hija(Padre1, Padre2):
    def imprimir(self):
        self.imprimir1()
        self.imprimir2()

# Instanciación de la clase Hija
hija = Hija()
hija.imprimir()

##¿Como se diferencia el comportamiento de una clase hija de su clase padre?
#1. Añade a la clase Hija él método Imprimir1 que imprima el texto “Método
# Imprimir1 sobrescrito”.
# 2. Añade una llamada al método Imprimir1 del objeto instanciado.
class Padre1:
    def imprimir1(self):
        print("Padre1 llamado")

class Padre2:
    def imprimir2(self):
        print("Padre2 llamado")

class Hija(Padre1, Padre2):
    def imprimir(self):
        self.imprimir1()
        self.imprimir2()

    def imprimir1(self):
        print("Método Imprimir1 sobrescrito")

# Instanciación de la clase Hija
hija = Hija()
hija.imprimir1()

