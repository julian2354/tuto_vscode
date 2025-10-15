# recorrido de listas.
# crear, recorrer, y modificar listas
# cadenas como listas
# patrones clasicos y algoritmos de orden

# que es una lista (areglos, arrays, vectores)
# es un tipo de dato que agrupa a otros tipos de datos con una lectura secuencial, es decir, 
# los datos van ordenados con un indice. este indice va desde 0, que seria la primera posicion. 
# estos se simbolizan o se guardan entre corchete [] y los tipos de datos que almacenan pueden ser todos
#  los primitivos y otros compuestos como tuplas, arreglos y diccionarios.

# edades = [15, 18, 12, 21]
# print(edades)
# print(edades[0])
# edades[3] = 19
# print(edades)
# print(len(edades))

# recorriendo y acumulando valores numericos.

# edades = [12, 15, 18, 21, 19]
# suma = edades[1]
# for i in range(len(edades)):
#     suma = suma + edades[i]
# print(f"promedio: {suma/len(edades)}")

# agregar datos con un input (sabiendo cuantas posiciones vamos a guardar.)

# N = 5
# datos = []
# for _ in range(N):
#     x = int(input("Ingrese un numero: "))
#     datos.append(x)
#     print(datos)
# print(f"lista final: {datos}")
# print(datos[-1])



#modicar edades 



# edades = [23,78,56,43,78,4,67,89,23,45,6,78,65,44,35,65,64]
# edades[3] = 59
# print(edades)



#agregar edades
edades=[23,34,565,675,7545,54]
edades.append(99)
print(edades)


#recorrer edades usando un for 
# edades = [23,34,65,87,91,23,45]
# for edad in edades:
#     print(edades)

# recorre las edades usando un acmulador
edades
