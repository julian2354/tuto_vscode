#algoritmos de ordenacion de areglos ( burbuja e insercion)

#que es un areglo, como se declara, como accede por indice, como se recorre por for,

# comparadores >,<,>=,<=,

#porque ordenar?: se facilita la busqueda la comparacion y los reportes 

# notas de menor a mayor me permite ver quienes aprobaron rapidamente, o puedo validar los precios  
# de una tienda para comprar del mas barato al mas caro.

#siempre debo definir el criterio de orden, sea ascendente o descendente

#metodo d ordenacion por burbujas 

# porque se llama burbuja

# porque vusualmente , cunado se ordenan parecen burbujas donde los elementos mas grande 
#se van espujando hacia el final del arreglo.


#idea general:
#usa oara cmparar pares adyecente
#si esta en orden  incorrecto, se intercanbian y repiten pasadas hata que no se nececite hacer 
#intercambios . ( esto utilipso puede optmizarse)


# arr = [5,1,4,2,8,3,11,9,6,]
# print("insercion")

# n = len(arr)

# for pasada in range (n - 1):
#     hubo_cambio = False
#     for i in range(n - 1 -pasada):
#         if arr[i]> arr[i+1]:
#             arr[i], arr[i+1]= arr[i+1],arr[i]
#             hubo_cambio = True
#     if not hubo_cambio:
#         break
#     print(arr)

#metodo de insercion (insertion sort)
#metafora



# for i in range (1, len(arr)):
#     actual = arr[i]
#     j = i-1
#     while j >= 0 and arr [j] > actual:
#         arr[j+1] = arr[j]
#         j -= 1
#         arr[j+1] = actual

# print(arr)


a = [9, 7, 8, 3]
print("incial", a)

for i in range(1, len(a)):
    actual = a[i]
    j = i -1
    desplazamientos = 0

    # desplazamos hacia la derecha todos los numeros mayores que actual.
    while j >= 0 and a[j] > actual:
        a[j + 1] = a[j]
        j -= 1
        desplazamientos +=1

    #insertar actual en el hueco donde va
    a[j + 1] = actual

    print(f"i = {i}, actual={actual}, desplazamientos ={desplazamientos}, arreglo={a}")

print("ordenado", a)





























