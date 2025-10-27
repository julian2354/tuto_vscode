#1
def sumatoria_1d(arr):

    if not arr:
        return  0  
  
    suma = 0
    for num in arr:
        suma += num
    return suma 

#prueba
print(sumatoria_1d([]))
print(sumatoria_1d([5]))
print(sumatoria_1d([1, 2, 3,]))
print(sumatoria_1d([-2, 3, -1]))



#2
def contar_mayores_igual(arr, umbral):
    
    
    
    contador = 0
    for num in arr:
        if num >= umbral:
            contador += 1
    return contador


#prueba
print(contar_mayores_igual([12, 8, 15, 19, 10, 14], 14))  
print(contar_mayores_igual([1, 1, 1], 2))                 

#3
def es_ordenado_asc(arr):
    

    
    
    if len(arr) <= 1:
        return True

    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print(es_ordenado_asc([]))          
print(es_ordenado_asc([3]))          
print(es_ordenado_asc([1, 2, 2, 5])) 
print(es_ordenado_asc([3, 2, 4]))    

#4
def insertar_en_pos(arr, pos, x):
    
    
    
    if pos < 0 or pos > len(arr):
        raise ValueError("La posición está fuera del rango válido.")

    
    nueva = arr[:pos] + [x] + arr[pos:]
    return nueva


#prueba
print(insertar_en_pos([10, 20, 30, 40], 2, 25))  
print(insertar_en_pos([], 0, 5))                
print(insertar_en_pos([1, 2, 3], 3, 4))         


#5
def eliminar_en_pos(arr, pos):
    
    
    
    
    if pos < 0 or pos >= len(arr):
        raise ValueError("La posición está fuera del rango válido.")

    
    nueva = arr[:pos] + arr[pos+1:]
    return nueva

#prueba
print(eliminar_en_pos([4, 6, 8, 10, 12], 2))  
print(eliminar_en_pos([1, 2, 3, 4], 0))       
print(eliminar_en_pos([1, 2, 3, 4], 3))    


#6
def burbuja(arr):
    
    
    n = len(arr)
    nueva = arr[:]  

    
    for pasada in range(n - 1):
        hubo_cambio = False
        for i in range(n - 1 - pasada):
            if nueva[i] > nueva[i + 1]:

                nueva[i], nueva[i + 1] = nueva[i + 1], nueva[i]
                hubo_cambio = True
       
        if not hubo_cambio:
            break
    return nueva
#prueba
print(burbuja([]))               
print(burbuja([3]))              
print(burbuja([3, 1, 2]))        
print(burbuja([5, 2, 5, 1]))      
print(burbuja([1, 2, 3, 4]))      


#7
def insercion(arr):
    
    
    nueva = arr[:]  
    n = len(nueva)

    
    for i in range(1, n):
        clave = nueva[i]
        j = i - 1
        
        while j >= 0 and nueva[j] > clave:
            nueva[j + 1] = nueva[j]
            j -= 1
        nueva[j + 1] = clave

    return nueva

#prueba
print(insercion([]))              
print(insercion([3]))             
print(insercion([3, 1, 2]))       
print(insercion([5, 2, 5, 1]))    
print(insercion([1, 2, 3, 4]))    


#8
def buscar_lineal(arr, objetivo):
    
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1


print(buscar_lineal([7, 2, 9, 4, 2], 2))  
print(buscar_lineal([7, 2, 9, 4, 2], 5))  
print(buscar_lineal([], 3))               
print(buscar_lineal([10], 10))            

#9
def buscar_binaria(arr_ordenado, objetivo):
    
    inicio = 0
    fin = len(arr_ordenado) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr_ordenado[medio] == objetivo:
            return medio
        elif arr_ordenado[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1
#prueba
print(buscar_binaria([1, 2, 4, 5, 9], 5))  
print(buscar_binaria([1, 2, 4, 5, 9], 6))  
print(buscar_binaria([1, 2, 4, 5, 5, 9], 5)) 
print(buscar_binaria([], 3))                

#10
def suma_total_2d(m):
    
    

    if not m:
        return 0

    total = 0
    for fila in m:
        for valor in fila:
            total += valor
    return total


#prueba
print(suma_total_2d([[1, 2, 3], [4, 5, 6]]))       
print(suma_total_2d([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))  
print(suma_total_2d([]))                           

#12
def insercion(arr):
    
    copia = arr[:]  
    for i in range(1, len(copia)):
        actual = copia[i]
        j = i - 1
        while j >= 0 and copia[j] > actual:
            copia[j + 1] = copia[j]
            j -= 1
        copia[j + 1] = actual
    return copia


def buscar_binaria(arr_ordenado, objetivo):
    
    inicio, fin = 0, len(arr_ordenado) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr_ordenado[medio] == objetivo:
            return medio
        elif arr_ordenado[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1


def ordenar_y_buscar(arr, objetivo):
    
    
    lista_ordenada = insercion(arr)
    indice = buscar_binaria(lista_ordenada, objetivo)
    return (lista_ordenada, indice)

#prueba
arr = [12, 5, 7, 5, 9, 1]
objetivo = 7
print(ordenar_y_buscar(arr, objetivo))  
