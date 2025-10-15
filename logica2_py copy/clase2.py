#clase de logica 2  02 domingo

#ciclo (while):
#la variable de control ,contador, suma o condiccion que regule el ciclo debe ser inicializada
 
# x = 5
# while x > 0: 
#     print(f"interacion de x: {x}")
#     x = x - 1
# print("fin")

#errorres de ue pueden causar un bucle infinito

# no actualizar la condicion dentro del bucle

# colocar mal la condicion (siempre verdadera o siempre falsa)

# cuando estamos comparando algo usando un igual solito en vez de un == , esto en python da error,
# pero hay otros lenguajes donde funciona 

# lecturas no acotadas, uso de sentinelas.
# un sentinela es un valor que indica " terminar"

# texto = input ("Escribe algo o (fin) para terminar:" )

# while texto != "fin":
#     print(f"he leido lo siguiente {texto}")
#     texto = input("escribe algo o (fin) para terminar: ")
# print("listo")

# while true y break

# while True:
#     n = int(input("numero(0 para terminar: )"))
#     if n == 0:
#         break
#     print(f'cuadrado{n* n}')
# print("terminar")

# sentinelas con contadores y acumuladores .

# suma, conteo = 0, 0
# while True:
#     dato = input(" monto ( enter vaciopara terminar) ")
#     if dato =="":
#         break
#     monto = float(dato)
#     suma = suma + monto
#     conteo = conteo + 1
# if conteo > 0:
#     print(F"el total es {suma} el promedio es {suma/conteo}")

# else:
#     print("joa, no agregaste nada mani")


#banderas o flags
# una bandera es una variable boleana que recuerda si paso algo 

# encontrado = False 
# while True:
#     palabra = input("escribe una palabra o x para salir: ")
#     if palabra =="x":
#         break
#     if palabra == "python":
#         encontrado == True
# if encontrado:
#     print("aparecio(python)al menos una vez")
# else:
#     print("nunca de escribe la 'palabra python' ")

# break y continue
# break frena el ciclo
# continue : salta a la siguiente iteracion.

# saltar numero negativos y solo vamos a sumar numeros negativos.

# suma = 0
# while True:
#     n = int(input(" numero(0 corta:"))
#     if n == 0:
#         break
#     if n <0:
#         print("eso no me sirve, deme otro numero")
#         continue
#     suma = suma + n
# print(f'la suma unicmente de los pasitivo es {suma}')

   