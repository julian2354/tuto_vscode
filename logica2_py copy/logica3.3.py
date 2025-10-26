# logica 3 tercera clase 
#funciones y busquedas en arreglos

# que es una fucion

# def cuadradro(x):
#     return x * x 

# print (cuadrado (5))

#parametros
#son loa insumos con lo que va trabajar mi funcion 
#los parametros pueden ser mutables o inmutables.

# inmutables int, str o bolean :si los cambiamos dentro del a funcion, no necesariamente van 
# VAN A CAMBIAR POR FUERA
  

#mutables lista y diccionarios: si lo modificamos por funcion, 
# el dato de insumo si cambia por fuera 

# def suma_uno_valor(n):
#     n= n+1
#     return


# x = 10 
# y = suma_uno_valor(x)
# print(x,y)



# def sumar_uno_lista(a):
#     for i  in range(len(a)):
#         a[i]+=1


# arr=[1,2,3]
# print(arr)
# sumar_uno_lista(arr)
# print(arr)

# busqueda lineal...

#cuando usar la busqueda lineal?
#usamos la busqueda lineal cuANDO EL ARREGLO  no esta ordenado o no impora
#la efciencia para tamaños pequeños o medios...

#especificacion:
#entrada objetos ( valor a ser buscado), arr (lista donde vamos a buscar)


# salida: indice de la primera pocsion que coincida con la busqueda 
# 0 -1 si o no esta 
# arr =[1,2,3,4,5,5,6,7,8,8,9]

# def buscar_lineal(arr,objetivo):
#     for i in range(len(arr)):
#         if arr[i] == objetivo:
#             return i
#     return-1


# datos = [7,2,9,4,2]
# print(buscar_lineal(datos,2))
# print(buscar_lineal(datos,5))

#busqueda binaria:
#mirar al centro y descartar la mitad que no sirve.
# requisitos: el arreglo debe estar ordenado (ascendente aqui).

#especificacion

# entrada: arr_ordenado (lista ascendente), objetivo

#salida: indice donde aparece; -1 si no esta

def buscar_binaria(arr, objetivo):
    ini, fin = 0, len(arr) -1
    while ini <= fin:
        mid = (ini + fin) // 2
        if arr[mid] == objetivo:
            return mid
        elif arr [mid] < objetivo:
            ini = mid + 1
        else:
            fin = mid -1
    return -1

arr= [1,2,3,4,5,9]

print(buscar_binaria(arr,5))
print(buscar_binaria(arr,6))



