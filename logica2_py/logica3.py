#fundamentos arrays unidimensionales.session.1

#que es una estructura de datos ; son formas de organizar los datos para poder usarlos de forma eficiente,,
#(es como ordenar nuestras habitaciones: cajones de las medias contiene medias , perchas: colgar camisas, pantalones y etc)


#problemas sin estructura: tengo 50 notas sueltas... encontrar "la de matematicas" toma minutos

#con estrucutra (arreglo):las guardo en un cajon con separadores numerados. ahora se exactamente donde mirar ,


#arreglos cajon casilleros 

#definimos un areglo como una coleccion ordenada de elementos del mismo tipo. 
# esto para lenguajes compilados, no interpretados, de tipado estricto, fuertemente tipado, sin inferencia de tipo.


#indices: empieza desde ceo donde el primer cajon es cero


#tamaño al crearlo se deciden cuantos especios va a tener 

# notas = [15,34,56,64,22]
# print(notas[1])

# como recorre un areglo?

# para i desde 0 hasta n-1:
#mostrar notas[i]

# for i in range(len(notas)):
#     print(f"->{notas[i]}")

#llenados de areglos

#entrada simulada

# edades = [0]*5
# print(edades)

# edades = [0]*5
# valores=[23,45,65,32,46,33]
# for i in range(5):
#     edades [i] = valores[i]
#     print(edades)

# print(edades)
# print(valores)

#actualizacion por indices
# nombres=["ana", "jorge", "pedro", "juan"]
# indice = int(input("que pocision quieres cambiar: "))
# nombres[indice] = input("a quien vamos a integrar: ")
# nombres[1]="carlos"
# print(nombres[1])
# print(nombres)

#insercion y borrado(version simple)
#insercion conceptual: si hay espacio, "corro elementos a la derecha y la pongo el primero"

# borrado conceptual: " corro elemntos" a la izquierda para tapar algun hueco.

# nota.. en lenguajes con lista dinamicas como python esto es necesario 


arr= [10,20,30,40,None]









    