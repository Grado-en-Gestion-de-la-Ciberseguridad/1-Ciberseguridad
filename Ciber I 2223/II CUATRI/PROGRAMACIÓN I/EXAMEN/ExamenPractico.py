#1. Clase Guybrush (1 punto)
#Atributos:
#	- respuestas: list
#Métodos:
#	- Constructor: recibirá la siguiente lista de respuestas:

respuestas = ["¿Por qué? ¿Acaso querías pedir uno prestado?","Sí que las hay, sólo que nunca las has aprendido.","Me alegra que asistieras a tu reunión familiar diaria.",
"Primero deberías dejar de usarla como un plumero.","Qué apropiado, tú peleas como una vaca.","Ya te están fastidiando otra vez las almorranas, ¿Eh?",
"Ah, ¿Ya has obtenido ese trabajo de barrendero?"]

#  	- AddRepuesta: recibirá el texto de una respuesta y lo añadirá a la lista de respuestas siempre que no exista ya.
#  	- MostrarOpciones: no recibirá nada y debe mostrar todas las posibles respuestas de Guybrush de la siguiente manera:
#		1 - ¿Por qué? ¿Acaso querías pedir uno prestado?
#		2 - Sí que las hay, sólo que nunca las has aprendido.
#		3 - Me alegra que asistieras a tu reunión familiar diaria.


#2. Clase Pirata (1 punto)  
#Atributos:
#	- insultos: list
#Métodos:
#	- Constructor: recibirá la lista de insultos de los piratas:

insultos = ["¿Has dejado ya de usar pañales?", "¡No hay palabras para describir lo asqueroso que eres!", "¡He hablado con simios más educados que tu!",
"¡Llevarás mi espada como si fueras un pincho moruno!","¡Luchas como un ganadero!","¡No pienso aguantar tu insolencia aquí sentado!",
"¡Mi pañuelo limpiará tu sangre!"]

#	- GetInsulto: no recibirá nada y devolverá el índice de un insulto de la lista.
#	- MostrarInsulto: recibirá el índice del insulto en la lista y mostrará ese insulto por pantalla. 


#3. Clase Duelos (4 puntos) 
#Atributos:
#	- duelos: dict (vacío de inicio)
#   - numDuelo: int (inicialmente con el valor 1)
#	- player: Objeto de tipo Guybrush
#	- pirate: Objeto de tipo Pirata
#Métodos:
#	- Constructor: recibirá el objeto de tipo Guybrush y el de tipo Pirata, el resto de atributos los inicializará con los valores por defecto indicados 
#	anteriormente. 
#	- RegistrarDuelo: recibirá el índice la respuesta del player y el índice del insulto del pirata, debe incluir un registro en el diccionario de 
#	duelos con la clave el numDuelo y los valores con el siguiente formato:
#				duelos = { "1": {"Pirata": indice_pirata, "Guybrush": indice_guybrush, "Resultado": resultado_del_duelo} }
#	Donde el indice_pirata es el numero del índice del insulto del pirata, indice_guybrush es el índice de la respuesta seleccionada 
#	por el player y el resultado_del_duelo deberá obtenerse del método ComprobarResultado de esta misma clase. 
#	Cada vez que registre un duelo aumentará en 1 el numDuelo.
#	- ComprobarResultados: recibirá el índice del insulto del pirata y el índice de la respuesta de Guybrush, si son iguales devolverá "Gana Guybrush", 
#	si no devolverá "Gana Pirata".
#	- Duelo: no recibirá nada y deberá realizar duelos hasta que el player consiga 3 victorias seguidas. La dinámica del duelo será, el pirata muestra
#	un insulto, al player se le mostrarán las posibles respuestas de Guybrush, el player deberá seleccionar una de ellas (se debe usar input), si es una 
#	respuesta válida entre las opciones ofrecidas,  registrará el duelo con el método adecuado, comprobará el resultado, si gana Guybrush, suma 
#	una victoria, si pierde resta una victoria. 
#	Deberá mostrar cuantas victorias lleva el player en cada duelo. Ejemplo:
#			Pirata --> ¿Has dejado ya de usar pañales?"
#			Guybrush --> 
#				1 - ¿Por qué? ¿Acaso querías pedir uno prestado?
#				2 - Sí que las hay, sólo que nunca las has aprendido.
#				3 - Me alegra que asistieras a tu reunión familiar diaria.
#				Selecciona una: 

