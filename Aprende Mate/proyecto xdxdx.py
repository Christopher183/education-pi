import os

print("Bienvenido a este programa donde le ayudare a aprender operaciones Matematicas basicas")
print("Tales como: suma, resta, multiplicacion y division")
print("¿Que deseas aprender?")
print("1. Sumas")
print("2. Restas")
print("3. Multiplicacion")
print("4. Division")
op=int(input(" "))
os.system('cls')

while op<1 or op>4:            
	print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
	print("¿Que deseas aprender?")
	print("1. Sumas")
	print("2. Restas")
	print("3.Multiplicacion")
	print("4.Division")
	op=int(input(" "))
	os.system('cls')
if op==2:
	op17=1
if op==3:
        op17=2
if op==1:
	print("Genial, selecionaste la opcion Suma, ahora Por favor elije una de las opciones")
	print("1.Ejemplos")
	print("2.Ejercicios Faciles")
	print("3.Problemas que se resuelven con la suma")
	
	op1=int(input(" "))
	os.system('cls')
	if op1==3:
		op2=3
		op3=3
		op4=2
		op10=1
		op17=1
	
	if op1==2:
		op2=2
		op3=2
		op4=1
	while op1<1 or op1>3:
		print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
		print("1. Ejemplos")
		print("2. Ejercicios Faciles")
		print("3.Problemas que se resuelven con la Suma")
		op1=int(input(" "))
		os.system('cls')
	if op1==1:
		print("Comencemos con los ejemplos")
		print("Ejemplo 1")
		print("5+3")
		print("Para resolver esta suma, usaremos una tecnica muy eficaz para aprender a sumar, es la tecnica de los palitos.")
		print("Respuesta")
		print(" ")
		print("Bueno, Como el primer Numero es 5, pues dibujaremos 5 palitos, asi de simple")
		print("!!!!!")
		print("Como el segundo numero es 3, pues haremos lo que hemos hecho antes, dibujaremos 3 palitos.")
		print("!!!")
		print("Ahora la suma se trata de añadir, o agregar, asi que a los primero palitos que dibujamos le agregaremos los otros palitos que dibujamos o mejor dicho juntarlos y contarlos")
		print("!!!!!+!!!=(!!!!!!!!) estos son los que se unieron")
		print("Al contar los palitos que se unieron y si los cuentas, te deras cuenta de que hay 8 palitos y 8 es el resultado de la suma de 5+3")
		print(" ")
		print("¿Deseas ver mas Ejemplos?")
		print("1. SI")
		print("2. NO,Ahora quiero hacer Ejercicios")

		#aqui empiezan las variable op2
		op2=int(input(" "))
		if op2==2:
			op3=2
			op4=2
			op10=1
			
		os.system('cls')

		while op2<1 or op2>2:
			print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
			print("1. SI")
			print("2. NO,Ahora quiero hacer Ejercicios")
			op2=int(input(" "))
			os.system('cls')

		if op2==1:
			print("Ejmplo de resolucion de Problemas")
			print("Juan Tiene 3 Manzanas y luego va con su mama al mercado, y la mama de Juan le compro 4 manzanas mas ¿Cuantas manzana tiene ahora Juan?")
			print("Respuesta")
			print(" ")
			print("Para resolver este problema hay que hacer la pregunta ¿Cuantas Manzanas tenia Juan?")
			print("El problema nos dice que Juan tenia 3 Manzanas")
			print("luego nos dice que fue con su mama y compraron 4 mas")
			print("Asi que ahora nos queda responder la ultima pregunta del problema ¿Cuantas Manzanas tenia Juan?")
			print("Ahora solo nos queda sumar")
			print("3 Manzanas + 4 Manzanas = 7 Manzanas")
			print("Si aun no le entinedes, te lo pongo de la siguiente forma, vamos a suponer que cada palito representa una manzana")
			print("! ! ! + ! ! ! !")
			print("si contamos todos los palitos veremos que son 5 palitos en total, esta es una buena tecnica para que empieces a sumar")
			print("")
			print ("¿Deseas ver un ejemplo mas?")
			print("1. SI")
			print("2. NO,Ahora quiero hacer Ejercicios")
			op3=int(input(" "))
			os.system('cls')
			if op3==2:
				op4=1
				op10=1
			
			#empiezan las variable op3
		while op3<1 or op3>2:
			print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
			print("¿Deseas ver un ejemplo mas?")
			print("1. SI")
			print("2. NO, Ahora quiero hacer Ejercicios")
			op3=int(input(" "))
			os.system('cls')
		if op3==1:
			print("El granjero, Pedro tiene 2 vacas en su granja, pero llega un granjero a venderle 5 vacas mas ¿Cuantas vacas tiene ahora Pedro?")
			print("Respuesta")
			print(" ")
			print("El problema nos dice que Pedro tenia 2 vacas")
			print("luego nuos dice que le vendieron 5 vacas mas")
			print("ahora para resolver el problema, tenemos que leer la pregunta hecha en el problema,¿Cuantas vacas tiene ahora Pedro?")
			print("ahora solo nos queda sumar")
			print("2 vacas + 5 vacas = 7 vacas")
			print("si no lo entinedes aun, te lo pongo de la siguiente forma, vamos a suponer que cada palito representa una vaca")
			print("!! +  !!!!! ")
			print("si contamos todos los palitos veremos que son 7 palitos en total, esta es una buena tecnica para que empieces a sumar")
			print("")
			print("Ahora que vimos los ejemplos, ya estas listo para relizar los ejercicios.... Vamos!! ")
			print("Presiona la tecla '1' para ir a los ejercicios")
			#empieza op4
			op4=int(input(" "))
			os.system('cls')
			while op4!=1:
				print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
				print("Presiona la tecla '1' para ir a los ejercicios")
				op4=int(input(" "))
				os.system('cls')
	if op1==2 or op2==2 or op3==2 or op4==1:
		print("Vamos a ver los Ejercicios faciles, recuerde que debe completar todos los ejercicicios propuestos")
		print("Las Respuestas seran de opcion multiple puedes seleccionar la que consideres correcta")
		print(" ")
		print("Ejercicio 1.")
		print("¿Cuanto da la suma de 5+6?")
		print("a) la respuesta es 4")
		print("b) la respuesta es 8")
		print("c) la respuesta es 11")
		print("d) la respuesta es 13")
		op5=str(input(" "))
		
		while op5!='C' and op5!='c':
			if op5!= 'a' and op5!='b' and op5!='c' and op5!='d' and op5!='A' and op5!='C' and op5!='B' and op5!='C' and op5!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op5=str(input(" "))

			if op5!= 'c' or op5!='C':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto es la suma de 5+6?")
				print("a) la respuesta es 4")
				print("b) la respuesta es 8")
				print("c) la respuesta es 11")
				print("d) la respuesta es 13")
				op5=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")

		print("Ejercicio 2.")
		print("¿Cuanto es la suma de 3+4+5?")
		print("a) la respuesta es 10")
		print("b) la respuesta es 12")
		print("c) la respuesta es 17")
		print("d) la respuesta es 8")
		op6=str(input(" "))
		while op6!='B' and op6!='b':
			if op6!= 'a' and op6!='b' and op6!='c' and op6!='d' and op6!='A' and op6!='C' and op6!='B' and op6!='C' and op6!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op6=str(input(" "))
				
			if op6!= 'B' or op6!= 'b':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto es la suma de 3+4+5")
				print("a) la respuesta es 10")
				print("b) la respuesta es 12")
				print("c) la respuesta es 17")
				print("d) la respuesta es 8")
				op6=str(input(" "))
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print ("")
		print("Ejercicio 3.")
		print("¿Cuanto es la suma de 4+8+9?")
		print("a) la respuesta es 3")
		print("b) la respuesta es 34")
		print("c) la respuesta es 9")
		print("d) la respuesta es 21")
		op7=str(input(" "))
		while op7!='D' and op7!='d':
			if op7!= 'a' and op7!='b' and op7!='c' and op7!='d' and op7!='A' and op7!='C' and op7!='B' and op7!='C' and op7!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op7=str(input(" "))
			
			if op7!= 'D' or op7!= 'd':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto es la suma de 4+8+9?")
				print("a) la respuesta es 3")
				print("b) la respuesta es 34")
				print("c) la respuesta es 9")
				print("d) la respuesta es 21")
				op7=str(input(" "))
				os.system('cls')

				
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print ("")
		print("Ejercicio 4.")
		print("¿Cuanto es la suma de 1+2+3+4+5?")
		print("a) la respuesta es 15")
		print("b) la respuesta es 9")
		print("c) la respuesta es 14")
		print("d) la respuesta es 16")
		op8=str(input(" "))
		
		while op8!='A' and op8!='a':
			if op8!= 'a' and op8!='b' and op8!='c' and op8!='d' and op8!='A' and op8!='C' and op8!='B' and op8!='C' and op8!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op8=str(input(" "))
				
			if op8!= 'A' or op8!= 'a':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto es la suma de 1+2+3+4+5")
				print("a) la respuesta es 15")
				print("b) la respuesta es 9")
				print("c) la respuesta es 14")
				print("d) la respuesta es 16")
				op8=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print ("")
		print("Ejercicio 5.")
		print("¿Cuanto es la suma de 2+4+6+1?")
		print("a) la respuesta es 39")
		print("b) la respuesta es 78")
		print("c) la respuesta es 13")
		print("d) la respuesta es 19")
		op9=str(input(" "))
		while op9!='C' and op9!='c':
			if op9!= 'a' and op9!='b' and op9!='c' and op9!='d' and op9!='A' and op9!='C' and op9!='B' and op9!='C' and op9!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op9=str(input(" "))
				
			if op9!= 'C' or op9!= 'c':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto es la suma de 2+4+6+1")
				print("a) la respuesta es 39")
				print("b) la respuesta es 78")
				print("c) la respuesta es 13")
				print("d) la respuesta es 19")
				op9=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades... Has terminado con los ejercicios faciles Ahora iremos de una con la resolucion de problemas")
		print("Presione la tecla 1 para continuar")
		op10=int(input(" "))
		while op10!=1:
			print("Error, Presione la tecla 1 para continuar")
			op10=int(input(" "))
	if op1==3 or op10==1:
		print("Vamos a resolver problemas, recuerde que debe completar todos los ejercicicios propuestos")
		print("Las Respuestas seran de opcion multiple puedes seleccionar la que consideres correcta")
		print(" ")
		print("Ejercicio 1.")
		print("Alejandro tiene 2 perritos, pero su tia le regalo 5 perritos mas, ¿Cuantos perros tiene alejandro?")
		print("a) la respuesta es 3")
		print("b) la respuesta es 2")
		print("c) la respuesta es 7")
		print("d) la respuesta es 11")
		op11=str(input(" "))
		while op11!='C' and op11!='c':
			if op11!= 'a' and op11!='b' and op11!='c' and op11!='d' and op11!='A' and op11!='C' and op11!='B' and op11!='C' and op11!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op11=str(input(" "))
			if op11!= 'c' or op11!='C':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("Alejandro tiene 2 perritos, pero su tia le regalo 5 perritos mas, ¿Cuantos perros tiene alejandro?")
				print("a) la respuesta es 3")
				print("b) la respuesta es 2")
				print("c) la respuesta es 7")
				print("d) la respuesta es 11")
				op11=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")
		print("Ejercicio 2.")
		print("La prima de jose tiene 8 bolsas de caramelo y luego fue a al supermercado a comprar 7 bolsas de caramelo, ¿Cuantas bolsas de caramelos tiene ahora la prima de jose? ")
		print("a) la respuesta es 15")
		print("b) la respuesta es 4")
		print("c) la respuesta es 56")
		print("d) la respuesta es 16")
		op12=str(input(" "))
		while op12!='A' and op12!='a':
			if op12!= 'a' and op12!='b' and op12!='c' and op12!='d' and op12!='A' and op12!='C' and op12!='B' and op12!='C' and op12!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op12=str(input(" "))
			if op12!= 'a' or op12!='A':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("La prima de jose tiene 8 bolsas de caramelo y luego fue a al supermercado a comprar 7 bolsas de caramelo, ¿Cuantas bolsas de caramelos tiene ahora la prima de jose?")
				print("a) la respuesta es 15")
				print("b) la respuesta es 4")
				print("c) la respuesta es 56")
				print("d) la respuesta es 16")
				op12=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")
		print("Ejercicio 3.")
		print("Hector le regalo a Lester 5 tortillas, luego vino su mama y le dio 9 a Lester ¿Cuantas tortillas tiene ahora Lester? ")
		print("a) la respuesta es 9")
		print("b) la respuesta es 5")
		print("c) la respuesta es 14")
		print("d) la respuesta es 15")
		op13=str(input(" "))
		while op13!='c' and op13!='C':
			if op13!= 'a' and op13!='b' and op13!='c' and op13!='d' and op13!='A' and op13!='C' and op13!='B' and op13!='C' and op13!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op13=str(input(" "))
			if op13!= 'C' or op13!='c':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("Hector le regalo a Lester 5 tortillas, luego vino su mama y le dio 9 a Lester ¿Cuantas tortillas tiene ahora Lester? ")
				print("a) la respuesta es 9")
				print("b) la respuesta es 5")
				print("c) la respuesta es 14")
				print("d) la respuesta es 15")
				op13=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")
		print("Ejercicio 4.")
		print("La prima de jose tiene 8 bolsas de caramelo y luego fue a al supermercado a comprar 7 bolsas de caramelo, ¿Cuantas bolsas de caramelos tiene ahora la prima de jose? ")
		print("a) la respuesta es 15")
		print("b) la respuesta es 4")
		print("c) la respuesta es 56")
		print("d) la respuesta es 16")
		op14=str(input(" "))
		while op14!='A' and op14!='a':
			if op14!= 'a' and op14!='b' and op14!='c' and op14!='d' and op14!='A' and op14!='C' and op14!='B' and op14!='C' and op14!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op14=str(input(" "))
			if op14!= 'a' or op14!='A':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("La prima de jose tiene 8 bolsas de caramelo y luego fue a al supermercado a comprar 7 bolsas de caramelo, ¿Cuantas bolsas de caramelos tiene ahora la prima de jose?")
				print("a) la respuesta es 15")
				print("b) la respuesta es 4")
				print("c) la respuesta es 56")
				print("d) la respuesta es 16")
				op14=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")
		print("Ejercicio 5.")
		print("Maria tiene 4 monedas, luego de camino al colegio se encuentra por la calle 5 monedas, de regreso a casa su mama le regala 9 monedas mas, ¿Cuantas monedas tiene Maria?")
		print("a) la respuesta es 18")
		print("b) la respuesta es 9")
		print("c) la respuesta es 14")
		print("d) la respuesta es 3")
		op15=str(input(" "))
		while op15!='a' and op15!='A':
			if op15!= 'a' and op15!='b' and op15!='c' and op15!='d' and op15!='A' and op15!='C' and op15!='B' and op15!='C' and op15!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op15=str(input(" "))
			if op15!= 'A' or op15!='a':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("Maria tiene 4 monedas, luego de camino al colegio se encuentra por la calle 5 monedas, de regreso a casa su mama le regala 9 monedas mas, ¿Cuantas monedas tiene Maria?")
				print("a) la respuesta es 18")
				print("b) la respuesta es 9")
				print("c) la respuesta es 514")
				print("d) la respuesta es 3")
				op15=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades... Has terminado con los ejercicios de la resolucion de problemas")
		print("Presione la tecla 1 para continuar")
		op16=int(input(" "))
		while op16!=1:
			print("Error, Presione la tecla 1 para continuar")
			op16=int(input(" "))
		print("Se aconseja ir a las restas, pero si ya dominas este tema puedes escojer el que mas te convenga en las opciones que te presentamos ")
		print("1.Restas")
		print("2.Multiplicacion")
		print("3.Division")
		print("4.Salir del programa")
		#hay que poner op17 en las otras sentencias if
		op17=int(input(" "))
		while op17<1 or op17>4:
			print("Error, Por favor ingrese una de las opciones nostradas en el menu de opciones")
			print("1.Restas")
			print("2.Multiplicacion")
			print("3.Division")
			print("4.Salir del programa")
			op17=int(input(" "))

if op==2 or op17==1:
	print("Genial, selecionaste la opcion Resta, ahora Por favor elije una de las opciones")
	print("1.Ejemplos")
	print("2.Ejercicios Faciles")
	print("3.Problemas que se resuelven con la Resta")
	op18=int(input(" "))
	os.system('cls')

	if op18==3:
		op19=3
		op20=3
		op21=2
		op27=1
	if op18==2:
		op19=2
		op20=2




	while op18<1 or op18>3:
		print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
		print("1. Ejemplos")
		print("2. Ejercicios Faciles")
		print("3.Problemas que se resuelven con la resta")
		op18=int(input(" "))
		os.system('cls')
	if op18==1:
		print("Comencemos con los ejemplos")
		print("Ejemplo 1")
		print("7-5")
		print("Para resolver esta resta, usaremos una tecnica muy eficaz y algo parecida a la tecnica de la suma, es la tecnica de los palitos.")
		print("Respuesta")
		print(" ")
		print("Bueno, Como el primer Numero es 7, pues dibujaremos 7 palitos, asi de simple")
		print("!!!!!!!")
		print("Como el segundo numero es 5, pues haremos lo que hemos hecho antes, dibujaremos 5 palitos.")
		print("!!!!!")
		print("Ahora la resta se trata de quitar, asi que a los primero palitos que dibujamos le quitaremos los otros palitos que dibujamos o mejor dicho tacharlos")
		print("!*!*!*!*!*!!-!*!*!*!*!*=(!!) esto es lo que queda de tachar los segundos palitos dibujados")
		print("Al al tachar el primer grupo de palitos con el numero del segundo grupo de palitos, los que nos quedan sin tachar al final es la respuesta de la resta")
		print(" ")
		print("¿Deseas ver mas Ejemplos?")
		print("1. SI")
		print("2. NO,Ahora quiero hacer Ejercicios")
		
		op19=int(input(" "))
		os.system('cls')

		while op19<1 or op19>2:
			print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
			print("1. SI")
			print("2. NO,Ahora quiero hacer Ejercicios")
			op19=int(input(" "))
			os.system('cls')
		if op19==1:
			print("Ejmplo de resolucion de Problemas")
			print("Jose y Marcelo compraron una pizza que trae 12 pedazos y Marcelo se comio 5 pedazos ¿Cuantos pedazos de pizza le quedarin a Jose?")
			print("Respuesta")
			print(" ")
			print("Para resolver este problema hay que hacer la pregunta ¿Cuantos pedazos de pizza habiam en un principio?")
			print("El problema nos dice que habian 12 pedazos de pizza en un principio")
			print("luego nos dice que Marcelo se comio 5 pedazos ")
			print("Asi que ahora nos queda responder la ultima pregunta ¿Cuantos pedazos de pizza le quedarin a Jose? ")
			print("Ahora solo nos queda restar o quitar los trozos de pizza que se comio Marcelo que son 5 pedazos")
			print("A 12 pedazos le quitaremos o restaremos los 5 pedazos que Marcelo se comio")
			print("12 pedazos - 5 pedazos = 7 pedazos")
			print("Si aun no le entinedes, te lo pongo de la siguiente forma, vamos a suponer que cada palito representa un pedazo de pizza y los tachados son los pedazos que Marcelo se comio")
			print("!*!*!*!*!*!!!!!!!-!*!*!*!*!*=!!!!!!!")
			print("si contamos los palitos que no fueron tachados veremos que son 5 palitos y este es el resultado de la respuesta333333 ")
			print("")
			print ("¿Deseas ver un ejemplo mas?")
			print("1. SI")
			print("2. NO,Ahora quiero hacer Ejercicios")
			#incluir en sentencia if
			op20=int(input(" "))
			os.system('cls')
			#falta if
		if op19==2:
			op20=2
			op21=1

			#empiezan las variable op3
		while op20<1 or op20>2:
			print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
			print("¿Deseas ver un ejemplo mas?")
			print("1. SI")
			print("2. NO, Ahora quiero hacer Ejercicios")
			op20=int(input(" "))
			os.system('cls') #copia de la suma
		if op20==1:
			print("Martha tiene 9 dolares, pero de camino a su trabajo se compro un helado que costo 3 dolares, ¿Cuanto dinero le quedo a Martha?")
			print("Respuesta")
			print(" ")
			print("El problema nos dice que Martha tenia 9 dolares")
			print("luego nuos dice que se compro un helado que le costo tres dolares")
			print("ahora para resolver el problema, tenemos que leer la pregunta hecha en el problema,¿Cuanto dinero le quedo a Martha?")
			print("ahora solo nos queda quitar o restar lo que gasto con lo que tenia")
			print("9 dolares - 3 dolares")
			print("si no lo entinedes aun, te lo pongo de la siguiente forma, vamos a suponer que cada palito representa un dolar, y que cada palito tachado representa cada dolar que Martha pago por su helado")
			print("!*!*!*!!!!!!-!*!*!*")
			print("si contamos los palitos que no fueron tachados veremos que solamente nos quedan 6 palitos sin tachar, pues sencillamente esta es la respuesta del problema esto es lo que le queda a Martha")
			print("")
			print("Ahora que vimos los ejemplos, ya estas listo para relizar los ejercicios.... Vamos!! ")
			print("Presiona la tecla '1' para ir a los ejercicios")
			#empieza op4
			op21=int(input(" "))
			os.system('cls')
			while op21!=1:
				print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
				print("Presiona la tecla '1' para ir a los ejercicios")
				op21=int(input(" "))
				os.system('cls')
	if op18==2 or op19==2 or op20==2 or op21==1:
		print("Vamos a ver los Ejercicios faciles, recuerde que debe completar todos los ejercicicios propuestos")
		print("Las Respuestas seran de opcion multiple puedes seleccionar la que consideres correcta")
		print(" ")
		print("Ejercicio 1.")
		print("¿Cuanto la resta de 7-4?")
		print("a) la respuesta es 4")
		print("b) la respuesta es 7")
		print("c) la respuesta es 3")
		print("d) la respuesta es 58")
		op22=str(input(" "))
		
		while op22!='C' and op22!='c':
			if op22!= 'a' and op22!='b' and op22!='c' and op22!='d' and op22!='A' and op22!='C' and op22!='B' and op22!='C' and op22!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op22=str(input(" "))

			if op22!= 'c' or op22!='C':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto es la resta de 7-4?")
				print("a) la respuesta es 4")
				print("b) la respuesta es 7")
				print("c) la respuesta es 3")
				print("d) la respuesta es 58")
				op22=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")

		print("Ejercicio 2.")
		print("¿Cuanto es la resta de 10-3-2?")
		print("a) la respuesta es 3")
		print("b) la respuesta es 5")
		print("c) la respuesta es 4")
		print("d) la respuesta es 8")
		op23=str(input(" "))
		while op23!='B' and op23!='b':
			if op23!= 'a' and op23!='b' and op23!='c' and op23!='d' and op23!='A' and op23!='C' and op23!='B' and op23!='C' and op23!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op23=str(input(" "))
				
			if op23!= 'B' or op23!= 'b':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto es la resta de 10-3-2")
				print("a) la respuesta es 3")
				print("b) la respuesta es 5")
				print("c) la respuesta es 4")
				print("d) la respuesta es 8")
				op23=str(input(" "))
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print ("")
		print("Ejercicio 3.")
		print("¿Cuanto es la resta de 13-4?")
		print("a) la respuesta es 32")
		print("b) la respuesta es 4")
		print("c) la respuesta es 9")
		print("d) la respuesta es 2")
		op24=str(input(" "))
		while op24!='c' and op24!='C':
			if op24!= 'a' and op24!='b' and op24!='c' and op24!='d' and op24!='A' and op24!='C' and op24!='B' and op24!='C' and op24!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op24=str(input(" "))
				
			if op24!= 'C' or op24!= 'c':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto es la resta de 13-4?")
				print("a) la respuesta es 32")
				print("b) la respuesta es 4")
				print("c) la respuesta es 9")
				print("d) la respuesta es 2")
				op24=str(input(" "))
				os.system('cls')

				
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print ("")
		print("Ejercicio 4.")
		print("¿Cuanto es la resta de 17-2?")
		print("a) la respuesta es 15")
		print("b) la respuesta es 4")
		print("c) la respuesta es 17")
		print("d) la respuesta es 2")
		op25=str(input(" "))
		
		while op25!='A' and op25!='a':
			if op25!= 'a' and op25!='b' and op25!='c' and op25!='d' and op25!='A' and op25!='C' and op25!='B' and op25!='C' and op25!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op25=str(input(" "))
				
			if op25!= 'A' or op25!= 'a':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto es la resta de 17-2?")
				print("a) la respuesta es 15")
				print("b) la respuesta es 4")
				print("c) la respuesta es 17")
				print("d) la respuesta es 2")
				op25=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print ("")
		print("Ejercicio 5.")
		print("¿Cuanto es la resta de 18-5?")
		print("a) la respuesta es 3")
		print("b) la respuesta es 8")
		print("c) la respuesta es 13")
		print("d) la respuesta es 22")
		op26=str(input(" "))
		while op26!='C' and op26!='c':
			if op26!= 'a' and op26!='b' and op26!='c' and op26!='d' and op26!='A' and op26!='C' and op26!='B' and op26!='C' and op26!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op26=str(input(" "))
				
			if op26!= 'C' or op26!= 'c':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿¿Cuanto es la resta de 18-5?")
				print("a) la respuesta es 3")
				print("b) la respuesta es 8")
				print("c) la respuesta es 13")
				print("d) la respuesta es 22")
				op26=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades... Has terminado con los ejercicios faciles Ahora iremos de una con la resolucion de problemas")
		print("Presione la tecla 1 para continuar")
		op27=int(input(" "))
		while op27!=1:
			print("Error, Presione la tecla 1 para continuar")
			op27=int(input(" "))
	if op18==3 or op27==1:
		print("Vamos a resolver problemas, recuerde que debe completar todos los ejercicicios propuestos")
		print("Las Respuestas seran de opcion multiple puedes seleccionar la que consideres correcta")
		print(" ")
		print("Ejercicio 1.")
		print("La tia de mi amigo tenia 4 gatitos pero regalo 2 ¿Cuantos gatitos le quedaron a la tia de mi amigo?")
		print("a) la respuesta es 4")
		print("b) la respuesta es 5")
		print("c) la respuesta es 2")
		print("d) la respuesta es 9")
		op28=str(input(" "))
		while op28!='C' and op28!='c':
			if op28!= 'a' and op28!='b' and op28!='c' and op28!='d' and op28!='A' and op28!='C' and op28!='B' and op28!='C' and op28!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op28=str(input(" "))
			if op28!= 'c' or op28!='C':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("La tia de mi amigo tenia 4 gatitos pero regalo 2 ¿Cuantos gatitos le quedaron a la tia de mi amigo?")
				print("a) la respuesta es 4")
				print("b) la respuesta es 5")
				print("c) la respuesta es 2")
				print("d) la respuesta es 9")
				op28=str(input(" "))
				os.system('cls')
				#hasta aqui git hub
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")
		print("Ejercicio 2.")
		print("Marcos tiene 5 pares de zapatos, pero Marcos le regalo un par de zapatos su amigo, ¿Con cuantos zapatos se quedo Marcos? ")
		print("a) la respuesta es 1")
		print("b) la respuesta es 4")
		print("c) la respuesta es 5")
		print("d) la respuesta es 6")
		op29=str(input(" "))
		while op29!='b' and op29!='B':
			if op29!= 'a' and op29!='b' and op29!='c' and op29!='d' and op29!='A' and op29!='C' and op29!='B' and op29!='C' and op29!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op29=str(input(" "))
			if op29!= 'B' or op129!='b':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("Marcos tiene 5 pares de zapatos, pero Marcos le regalo un par de zapatos su amigo, ¿Con cuantos zapatos se quedo Marcos?")
				print("a) la respuesta es 1")
				print("b) la respuesta es 4")
				print("c) la respuesta es 5")
				print("d) la respuesta es 6")
				op29=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")
		print("Ejercicio 3.")
		print("	Miguel compro 8 manzanas  y le dio una a su hermana y otra a su primo")
		print("a) la respuesta es 9")
		print("b) la respuesta es 5")
		print("c) la respuesta es 6")
		print("d) la respuesta es 8")
		op30=str(input(" "))
		while op30!='c' and op30!='C':
			if op30!= 'a' and op30!='b' and op30!='c' and op30!='d' and op30!='A' and op30!='C' and op30!='B' and op30!='C' and op30!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op30=str(input(" "))
			if op30!= 'C' or op30!='c':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("Miguel compro 8 manzanas  y le dio una a su hermana y otra a su primo")
				print("a) la respuesta es 9")
				print("b) la respuesta es 5")
				print("c) la respuesta es 6")
				print("d) la respuesta es 8")
				op30=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades... Has terminado con los ejercicios de la resolucion de problemas")
		print("Presione la tecla 1 para continuar")
		op31=int(input(" "))
		while op31!=1:
			print("Error, Presione la tecla 1 para continuar")
			op31=int(input(" "))
		print("Se aconseja ir a la Multiplicacion, pero si ya dominas este tema puedes escojer el que mas te convenga en las opciones que te presentamos ")
		print("1.Multiplicacion")
		print("2.Division")
		print("3.Salir del programa")
		#hay que poner op17 en las otras sentencias if
		op32=int(input(" "))
		while op32<1 or op32>3:
			print("Error, Por favor ingrese una de las opciones nostradas en el menu de opciones")
			print("1.Multiplicacion")
			print("2.Division")
			print("3.Salir del programa")
			op32=int(input(" "))
if op==3 or op17==2 or op32==1:
	print("Genial, selecionaste la opcion Multiplicacion, ahora Por favor elije una de las opciones")
	print("1.Ejemplos")
	print("2.Ejercicios Faciles")
	print("3.Problemas que se resuelven con la Multiplicacion")
	op33=int(input(" "))
	os.system('cls')
	#op34==2 or op35==2 or op36==2 or op37==1:

	#op34==2 or op35==2 or op36==2 or op37==1:
	if op33==2:
		op34=2
		op35=2
		op36=2
		op37=1
	if op33==3:
		op42=1
		op34=0
		op35=0
		op36=0
		op37=0
	while op33<1 or op33>3:
		print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
		print("1. Ejemplos")
		print("2. Ejercicios Faciles")
		print("3.Problemas que se resuelven con la Suma")
		op33=int(input(" "))
		os.system('cls')
	if op33==1:
		print("Comencemos con los ejemplos")
		print("Esta tecnica no es muy recomendada para Multiplicar, es solamente para que entiendas como funciona la multiplicacion y que necesita de la suma para poder operar con ella, luego de que entiendas esto te recomiendo ver las tablas de multiplicacion desde el 1 hasta 12, y que te las aprendas")
		print("Ejemplo 1")
		print("4*5")
		print("Para resolver esta multiplicacion, nos apoyaremos en la Suma, ya que la multiplicacion es sumar el mismo numero una cierta cantidad de veces, aunque hay tablas de multiplicacion que tendras que aprendertelas, esto te ayudara enormemente ")
		print("Respuesta")
		print(" ")
		print("Bueno, Como el primer Numero es 4, pues este sera nuestro numero a sumar una cierta cantidad de veces")
		print("Como el segundo numero es 5, este nos indica la cantidad de veces que tenemos que sumar el 4.")
		print("Ahora que sabemos esto podemos usar la misma tecnica de la suma, en este caso seria sumar el numero 4, 5 veces")
		print("4+4+4+4+, como vez estamos sumando el mismo numero 5 veces ya que la expresion es 4*5")
		print("al usar la tecnica de la suma, los palitos ")
		print("!!!!+!!!!+!!!!+!!!!+!!!!=!!!!!!!!!!!!!!!!!!!! ")
		print("Si unimos todos los palitos y los contamos nos daremos cuenta de que hay 20 palitos, asi de simple eso es 4*5=20")
		print("¿Deseas ver mas Ejemplos?")
		print("1. SI")
		print("2. NO,Ahora quiero hacer Ejercicios")
		op34=int(input(" "))
		if op34==2:
			op35=2
			op36=2
			#hay que correjir esta variable
			op10=1
			
		os.system('cls')

		while op34<1 or op34>2:
			print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
			print("1. SI")
			print("2. NO,Ahora quiero hacer Ejercicios")
			op34=int(input(" "))
			os.system('cls')

		if op34==1:
			print("Ejmplo de resolucion de Problemas")
			print("Una señora compró 8 paquetes con seis sodas cada uno, para llevar a una fiesta, ¿Cuántas sodas llevará a la fiesta?")
			print("Respuesta")
			print(" ")
			print("Para resolver este problema hay que hacer la pregunta ¿Cuántas sodas traia cada paquete? ")
			print("El problema nos dice que 6 sodas")
			print("luego nos dice que compro 8 paquetes")
			print("Asi que ahora nos queda responder la ultima pregunta del problema ¿Cuántas sodas llevará a la fiesta?")
			print("Ahora solo nos queda Multiplicar")
			print("6*8 ¿Porque?, Bueno pues porque por cada paquete de sodas hay 6 cada uno y habian 6, la forma de resolverlo seria sumando 6, 8 veces")
			print("!!!!!!+!!!!!!+!!!!!!+!!!!!!+!!!!!!+!!!!!!+!!!!!!+!!!!!!=!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			print("si contamos todos los palitos veremos que son 48 palitos en total, y ahi tenemos la respuesta")
			print("")
			print ("¿Deseas ver un ejemplo mas?")
			print("1. SI")
			print("2. NO,Ahora quiero hacer Ejercicios")
			op35=int(input(" "))
			os.system('cls')
			if op35==2:
				op36=2
				op37=1
			
			#empiezan las variable op3
		while op35<1 or op35>2:
			print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
			print("¿Deseas ver un ejemplo mas?")
			print("1. SI")
			print("2. NO, Ahora quiero hacer Ejercicios")
			op35=int(input(" "))
			os.system('cls')
		if op35==1:
			print("Don Beto lleva en su camión 7 cajas con 5 melones cada una. ¿Cuántos melones llevará en total?")
			print("Respuesta")
			print(" ")
			print("Para resolver este problema hay que hacer la pregunta ¿Cuántos melones trae la caja?")
			print("El problema nos dice que 5")
			print("Asi que ahora nos queda responder la ultima pregunta del problema ¿Cuántas cajas lleva en su camión?")
			print("El problema nos dice que 7")
			print("ahora solo nos queda Multiplicar")
			print("5*7 ¿Porque?, Bueno pues porque por cada caja tiene 5 melones cada uno y hay 7 cajas, la forma de resolverlo seria sumando 5, 6 veces ")
			print("!!!!!+!!!!!+!!!!!+!!!!!+!!!!!+!!!!!+=!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
			print("si contamos todos los palitos veremos que son 30 palitos en total, y ahi tenemos la respuesta")
			print("")
			print("Ahora que vimos los ejemplos, ya estas listo para relizar los ejercicios.... Vamos!! ")
			print("Presiona la tecla '1' para ir a los ejercicios")
			op37=int(input(" "))
			os.system('cls')
			while op37!=1:
				print("Error, No seleccionaste una de las opciones del menu, Por favor ingresa una de las opciones mostradas en el menu")
				print("Presiona la tecla '1' para ir a los ejercicios")
				op37=int(input(" "))
				os.system('cls')
				#copy de resolucion de problemas
	if op34==2 or op35==2 or op36==2 or op37==1:
		print("Vamos a ver los Ejercicios faciles, recuerde que debe completar todos los ejercicicios propuestos")
		print("Las Respuestas seran de opcion multiple puedes seleccionar la que consideres correcta")
		print(" ")
		print("Ejercicio 1.")
		print("¿Cuanto da 4*3?")
		print("a) la respuesta es 12")
		print("b) la respuesta es 8")
		print("c) la respuesta es 15")
		print("d) la respuesta es 13")
		op38=str(input(" "))
		
		while op38!='a' and op38!='A':
			if op38!= 'a' and op38!='b' and op38!= 'c' and op38!='d' and op38!='A' and op38!='C' and op38!='B' and op38!='C' and op38!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op38=str(input(" "))

			if op38!= 'a' or op38!='A':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto da 4*3?")
				print("a) la respuesta es 4")
				print("b) la respuesta es 8")
				print("c) la respuesta es 11")
				print("d) la respuesta es 13")
				op38=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")

		print("Ejercicio 2.")
		print("¿Cuanto da 5*3?")
		print("a) la respuesta es 5")
		print("b) la respuesta es 15")
		print("c) la respuesta es 17")
		print("d) la respuesta es 16")
		op39=str(input(" "))
		while op39!='B' and op39!='b':
			if op39!= 'a' and op39!='b' and op39!='c' and op39!='d' and op39!='A' and op39!='C' and op39!='B' and op39!='C' and op39!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op39=str(input(" "))
				
			if op39!= 'B' or op39!= 'b':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto es da 5*3?")
				print("a) la respuesta es 5")
				print("b) la respuesta es 15")
				print("c) la respuesta es 17")
				print("d) la respuesta es 16")
				op39=str(input(" "))
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print ("")
		print("Ejercicio 3.")
		print("¿Cuanto da 9*3?")
		print("a) la respuesta es 27")
		print("b) la respuesta es 34")
		print("c) la respuesta es 9")
		print("d) la respuesta es 21")
		op40=str(input(" "))
		while op40!='a' and op40!='A':
			if op40!= 'a' and op40!='b' and op40!='c' and op40!='d' and op40!='A' and op40!='C' and op40!='B' and op40!='C' and op40!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op40=str(input(" "))
				
			if op40!= 'A' or op7!= 'a':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿Cuanto da 9*3?")
				print("a) la respuesta es 27")
				print("b) la respuesta es 34")
				print("c) la respuesta es 9")
				print("d) la respuesta es 21")
				op40=str(input(" "))
				os.system('cls')
				#FIN DE DONDE LO DEJE MAMON..................................................................................................................................................................
				
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print ("")
		print("Ejercicio 4.")
		print("¿cuanto es 6*2?")
		print("a) la respuesta es 12")
		print("b) la respuesta es 4")
		print("c) la respuesta es 35")
		print("d) la respuesta es 13")
		op41=str(input(" "))
		
		while op41!='A' and op41!='a':
			if op41!= 'a' and op41!='b' and op41!='c' and op41!='d' and op41!='A' and op41!='C' and op41!='B' and op41!='C' and op41!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op41=str(input(" "))
				
			if op41!= 'A' or op41!= 'a':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("¿cuanto es 6*2?")
				print("a) la respuesta es 12")
				print("b) la respuesta es 4")
				print("c) la respuesta es 35")
				print("d) la respuesta es 13")
				op41=str(input(" "))
				os.system('cls')
		os.system('cls')
		
		print("Felicidades... Has terminado con los ejercicios faciles Ahora iremos de una con la resolucion de problemas")
		print("Presione la tecla 1 para continuar")
		op142=int(input(" "))
		while op42!=1:
			print("Error, Presione la tecla 1 para continuar")
			op42=int(input(" "))
	if op42==1 or op33==3:
		print("Vamos a resolver problemas, recuerde que debe completar todos los ejercicicios propuestos")
		print("Las Respuestas seran de opcion multiple puedes seleccionar la que consideres correcta")
		print(" ")
		print("Ejercicio 1.")
		print("En un estacionamiento hay 10 carros, si cada carro tiene 4 llantas, ¿Cuántas llantas hay por todas?")
		print("a) la respuesta es 3")
		print("b) la respuesta es 40")
		print("c) la respuesta es 31")
		print("d) la respuesta es 41")
		op43=str(input(" "))
		while op43!='b' and op43!='B':
			if op43!= 'a' and op43!='b' and op43!='c' and op43!='d' and op43!='A' and op43!='C' and op43!='B' and op43!='C' and op43!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op43=str(input(" "))
			if op43!= 'b' or op43!='B':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("En un estacionamiento hay 10 carros, si cada carro tiene 4 llantas, ¿Cuántas llantas hay por todas?")
				print("a) la respuesta es 3")
				print("b) la respuesta es 40")
				print("c) la respuesta es 31")
				print("d) la respuesta es 41")
				op43=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")
		print("Ejercicio 2.")
		print("A una caja de colores le caben 12, si hay en la tienda 9 cajas. ¿Cuántos colores serán por todos?")
		print("a) la respuesta es 108")
		print("b) la respuesta es 90")
		print("c) la respuesta es 54")
		print("d) la respuesta es 67")
		op44=str(input(" "))
		while op44!='A' and op44!='a':
			if op44!= 'a' and op44!='b' and op44!='c' and op44!='d' and op44!='A' and op44!='C' and op44!='B' and op44!='C' and op44!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op44=str(input(" "))
			if op44!= 'a' or op44!='A':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("A una caja de colores le caben 12, si hay en la tienda 9 cajas. ¿Cuántos colores serán por todos?")
				print("a) la respuesta es 108")
				print("b) la respuesta es 90")
				print("c) la respuesta es 54")
				print("d) la respuesta es 67")
				op44=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")
		print("Ejercicio 3.")
		print("Miguel gasta $12.00 todos los días en el camión que lo lleva a la escuela y lo trae a la casa, ¿Cuánto gasta a la semana? ")
		print("a) la respuesta es 95")
		print("b) la respuesta es 84")
		print("c) la respuesta es 85")
		print("d) la respuesta es 67")
		op45=str(input(" "))
		while op45!='b' and op45!='B':
			if op45!= 'a' and op45!='b' and op45!='c' and op45!='d' and op45!='A' and op45!='C' and op45!='B' and op45!='C' and op45!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op45=str(input(" "))
			if op45!= 'b' or op45!='B':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("Miguel gasta $12.00 todos los días en el camión que lo lleva a la escuela y lo trae a la casa, ¿Cuánto gasta a la semana? ")
				print("a) la respuesta es 95")
				print("b) la respuesta es 84")
				print("c) la respuesta es 85")
				print("d) la respuesta es 67")
				op45=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print(" ")
		print("Ejercicio 4.")
		print("LUna pelota cuesta $4 . ¿Cuánto cuestan 9 pelotas iguales?")
		print("a) la respuesta es 35")
		print("b) la respuesta es 56")
		print("c) la respuesta es 36")
		print("d) la respuesta es 34")
		op46=str(input(" "))
		while op46!='c' and op46!='C':
			if op46!= 'a' and op46!='b' and op46!='c' and op46!='d' and op46!='A' and op46!='C' and op46!='B' and op46!='C' and op46!='D':
				print("Por favor seleccione una de las opciones mostradas en el menu")
				op46=str(input(" "))
			if op46!= 'c' or op46!='C':
				print("Ops!! esa no es la opcion correcta, vuelve a intentarlo")
				print("Una pelota cuesta 4 €. ¿Cuánto cuestan 9 pelotas iguales??")
				print("a) la respuesta es 35")
				print("b) la respuesta es 56")
				print("c) la respuesta es 36")
				print("d) la respuesta es 34")
				op46=str(input(" "))
				os.system('cls')
		os.system('cls')
		print("Felicidades esa es la respuesta correcta")
		print("Felicidades... Has terminado con los ejercicios de la resolucion de problemas")
		print("Presione la tecla 1 para continuar")
		op16=int(input(" "))


		

