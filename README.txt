Tarea 1 Lenguajes de Programación
Integrantes:
  - Joaquín Castillo Tapia	Rol:201773520-1	
  - María Paz Morales Llopis	Rol:201773505-8 
Paralelo: 200

Para correr el codigo es necesario:
	- Python 3.5.2 o superior
	- Archivo .txt con el codigo LOLCODE a analizar debe estar en la misma carpeta que el archivo checker.py
	- El programa, al ejecutarse, preguntará el nombre del archivo. Se debe colocar el nombre.txt 
	
Supuestos:
  - Consideramos como válidos los siguientes tipos de variable:
	-> Número entero.
	-> Número decimal (float): contiene un punto entre los enteros y los decimales. 
	-> String: conjunto de caracteres encerrado por comillas dobles. 
  - Las variables no necesariamente debe estar declarada y/o inicializadas para ser utilizadas. Es decir, si se utiliza una variable que, por ejemplo, no está declarada antes, no necesariamente la línea se marcará como errónea. 
  - Estructura Básica:
	-> En caso de que haya más de una pareja de HAI-KTHXBYE correcta, consideramos sólo la primera como válida para analizar. 
	-> El código a ejecutar entre la pareja HAI-KTHXBYE no necesariamente debe estar correcto, para que ambas palabras estén correctas.
  - Declaración e Inicialización de variables:
	-> <expresion> puede ser el nombre de una variable, un número, un string, un operador u otra declaración o inicialización, o entrada o salida. 
  - Operadores: 
	-> Se considera como operador unario sólo el NOT. 
	-> <expression> puede ser número, string, nombre de variable, un operador, o una inicialización o declaración, o entrada o salida. 
	-> Si es que alguna de las expresiones dentro del operador resulta inválida, la línea completa es inválida. 
  - Condicionales:
	-> <Expresion> puede ser un operador, entrada o salida, o declaración o inicialización.
	-> Si la expresión no es válida, y todas las palabras claves existen, entonces se marca como error el O RLY?
	-> Si es que no hay código entre el YA RLY y el NO WAY, o entre el NO WAY y el OIC, se marcan como error sólo las palabras claves involucradas. No es necesario que el código esté correcto para que las palabras clave estén correctas. 
	-> Si es que hay código entre el O RLY? y el YA RLY, sólo este último se marca como error.  
	-> Si es que existe el O RLY? y una o más palabras clave no existe, entonces todas las palabras claves que sí existen se marcan como error. 
	-> Emparejamos siempre de adentro hacia afuera, vale decir, emparejamos el primer OIC con el últmo O RLY? antes del OIC. 
  - Loops:
	-> <nombre del loop> debe seguir las mismas reglas que el nombre de una variable. 
	-> <expression> puede ser sólo un operador, salida o entrada, o inicialización o declaración.
	-> <variable> puede ser sólo el nombre de una variable. 
	-> <bloque de codigo que se ejecuta en el loop> no necesariamente debe estar correcto para que el loop esté correcto, pero sí o sí debe existir. 
  - Entrada y Salida:
	-> <expresion> puede ser número, operador, string, una variable, entrada o salida, o inicialización o declaración. 





