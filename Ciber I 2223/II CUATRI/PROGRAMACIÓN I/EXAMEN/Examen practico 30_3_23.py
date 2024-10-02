#EJER 1
#FUNCIÓN ValidarUser
def validarUser (nombreusuario): #primera función
    if len (nombreusuario)< 6 or len (nombreusuario)>12: #len para contar los caracteres de nombreusuario. 
#aqui ya hemos comprobado si tiene un tamaño entre 6 y 12 caracteres.         
        return False
# ¿Hay comas en nombreusuario? (",") 
    # Si se cumple esta condición, se devuelve FALSE, = nombre de usuario no es válido.
    if "," in (nombreusuario): 
        return False
    if nombreusuario != nombreusuario.lower(): #comprobación si está todo en minúscula. 
        return False
    return True    #si se cumplen las tres reglas se devuelve TRUE, en caso contrario FALSE.

#También se debe crear la función llamada ValidarPass que recibirá una contraseña, deberá comprobar que 
# la contraseña recibida cumple con los siguiente criterios:
# a) Tiene al menos 6 caracteres.
# b) Dispone de al menos un carácter en minúscula, otro en mayúscula y un número. 
# c) Si cumple las dos reglas devolverá True, en caso contrario devolverá False.
def ValidarPass(contraseña):
    #Se verifica si el largo de la contraseña es menor a 6.
    # Se cumple esta condición = False, = contraseña que no es VALIDA !!!
    if len(contraseña) < 6:
        return False
    #Estas variables se utilizarán para verificar si la contraseña 
    # contiene al menos una letra minúscula, una letra mayúscula y un número.
    minuscula= False
    mayuscula = False
    numero = False
    #Si el caracter es una letra minúscula, se cambia el valor de la variable "minuscula" a True.
    # Si el caracter es una letra mayúscula, se cambia el valor de la variable "mayuscula" a True.
    # Si el caracter es un número, se cambia el valor de la variable "numero" a True.
    for caracter in contraseña: #recorremos para verificar si esta en la contraseña con FOR. 
        if caracter.islower():
            minuscula = True
        elif caracter.isupper():
            mayuscula = True
        elif caracter.isnumeric():
            numero = True
    #Se verifica que la contraseña tenga al 
    if not (minuscula and mayuscula and numero):
        return False
    return True    #si no se han cumplido ninguna de las condiciones de antes, se muestra TRUE, CONTRASEÑA VALIDA !!


#EJER 2 
#Crear otra función que se llamará ComprobarUsuarios, que recibirá un diccionario de usuarios (al menos 5). 
# Esta función deberá calcular si el usuario y la contraseña son válidos (ambos), deberá comprobar que recibe un diccionario, en caso contrario deberá lanzar una excepción indicando la problemática. 
# Si ambos son válidos, deberá añadir al diccionario dentro del usuario la clave "success" con True si ambos son válidos o con False si alguno de los dos no lo es. 
# La función devolverá el diccionario resultante. 
usuariosejemplo = {      #
    "mafalda": {"password": "DDDAA21"},
    "manolito": {"password": "EEEEERRRRR"},
    "pepito": {"password": "EOJERJEE"},
    "jamon": {"password": "JAhJ23"},
    "croquetas": {"password": "ajsh23"}       #entrada 
}
fff ="hola que eee"
#la función COMPRUEBA si cada elemento recibido es un diccionario o no. 
#no es = TypeError. 
def ComprobarUsuarios(diccionario):
    if len(diccionario)<5:
      raise ValueError("Se necesitan al menos 5 usuarios en el diccionario")# por que poner raise en vez de print, porque asi salta la excepcion y no continuaa con el programa y te obliga a poner 5 usuarios  en el diccionario
    if not isinstance(diccionario, dict): # isinstance comprueba si los parametros introducidos son en este caso de  tipo diccionario, por eso pone dict
        raise ValueError("El argumento debe ser un diccionario") #en caso de que (en este caso diccionario) no sea un diccionario, nos imprimirá una excepción para controlarlo
    return diccionario 

ComprobarUsuarios(usuariosejemplo)

#EJER 3: Dado el diccionario resultante del ejercicio 2, debe contabilizar cuantos usuarios- passwords no son válidas y mostrarlo por pantalla con este formato
#validos 2 #nº usuarios 5 #no validos 3 
def contabilizarUsuarios(diccionario):   #se define la función que recibe como argumento un dict de usuarios. 
    # Inicializamos contadores
    num_usuarios = 0
    num_validos = 0
    num_no_validos = 0        #para recorrerlo, ponemos los contadores a 0. 
    # Recorremos el diccionario de usuarios y comprobamos si las contraseñas son VALIDAS. 
    for usuario, datos in diccionario.items():  #con item () se obtiene tanto el valor como la clave y valor de cada elemento del dict en el bucle for. 
        #por cada usuario, comprobamos si su contraseña es valida con las condiciones del 2 si era mayuscula, minuscula o un numero. 
        if len(datos['password']) >= 8 and (caracter.isupper() for caracter in datos['password']) and any(caracter.isdigit() for caracter in datos['password']):
            # Si la contraseña es válida, aumentamos el contador de usuarios válidos
            num_validos += 1
        else:
            # Si la contraseña no es válida, aumentamos el contador de usuarios no válidos
            num_no_validos += 1
    







    














def ValidarUser(username):
    if len(username) < 6 or len(username) > 12:
        return False
    if ',' in username:
        return False
    if username != username.lower():
        return False
    return True