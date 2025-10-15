#QUE ES UN BUCLE

#ESTRUCTURA DE CONTROL (EJECUTA CODIGO DE FORMA SECUENCIAL Y CONTROLADA, SEGUN EL CONJUNTO DE INTRUCCCIONES O 
# CONDICIONES QUE APLIQUEMOS.) DE FORMA REPETTIVAS.

#SECUENCIALIDAD: INTRUCIONES QUE SE EJECUTAN UNA TRAS OTRA 

#CONDICIONAL: EJECUTA CODIGO SEGUN UNA DECISION TOMADA, DADA UNA CONDICION (IF,ELIF, ELSE )

# Repetitivas: repetir un bloque de un codigo mientras se cumpla una condicion o durante un rango definido. se usa cuando 
#se debe repetir la misma operacion varias veces o no conocemos de antemano cuantas veces vamos a repetir una accion o si 
# lo sabemos 

#panorama de los bucles 

#para (for):repite un numero conocido de veces o recorre una secuencia o rango 

#mientras (while): repite el codigo mientras la condicion sea verdadera (riesgo de que el bucle sea infinitos i no se 
#cambia la variable que lo rije)

#repetir hasta / do-while: ejecuta una vez y luego verifica la condicion 

# el bucle for.
#recorriendo un rango simple 

# for i in range ( inicial,fin,paso ):
    # codigo que se va a ejecutar , usando i y como variale iteradora.


# range (n)= contar desde 0 hasta n-1
#range(100)= 0 ... 99
# range(a,b)= a hasta b -1
# range (350,498) = 350 ... 498
# range (a,b,s) = a, a+s, a+2s, a+3s ... b (Ppaso puede ser negativo)
#range (1,1001,10) = 1,10,20,30,...1000
#range(1000,-0,-10)= 1000,990,980,970,....-1

# # 1= imprimir numero del 0 al 4
# for i in range(5):
#     print(i)

# # 2) imprimir los numeros del 1 al 5

# for i in range(1,6):
#     print(i)

# # imprimir los numeros pares del 1 al 20 
# print("tercer ejercio")

# for i in range(0,21,2):
#     print(i)


# #4) imprimir los numeros del 1 al 20 , de forma descendente 
# print("cuarto ejercisio")


# for i in range (20,0,-1):
#     print(i)


#contadores y acumuladores
#son variable .. pero estas tienes funciones especificas 
#segun el contexto que nececito para mi algoritmo


#contador : variable para contar cuantas veces sucede algo o contar elementos 

#acumulador: variable que suma, multiplica o contactena valores 


#contar cuantos numeros del 1 al 100 son multiplos de 3 

# conteo =0 
# for i in range(1,101):
#     if i % 3 == 0:
#         conteo= conteo +1 
# print(f"los multiplos de 3 son:{conteo}")


# sumar del 1 al 100 (acumulador)
# suma = 0
# for i in range(1,101):
#     suma = suma + i 
# print(f"la suma e los primeros  100 numeros es:{suma}")


# promedio de N numero de ingresados por el usuarios 
# N = 5 
# acum = 0

# for _ in range (N):
#  x = float(input("hey, dame un numero: "))
# acum = acum + x
# prom = acum / N
# print(F"el promedio es : {prom}")







