dic_personas = {}

while True:
	nombre = input['Introduce un nombre o @ para salir:']
	if nombre == '@':
		break
	else:
		apellidos = input['Introduce los apellidos: ']
		edad = input['Indica la edad']
		if edad.isdigit():
			if nombre + " " + apellidos not in dic_personas:
				dic_personas[nombre + " " + apellidos] = edad
			else:
				print('Esa persona ya fue introducida...')
		else:
			print('Edad tiene que se un entero => 0')

print(dic_personas)