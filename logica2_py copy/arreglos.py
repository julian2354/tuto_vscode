#1
 #Índices y acceso (Básico)
a = [7, 3, 9, 5, 9]
print([0])
print([3])
print(a[len(a)-1]) # lo usamos para acceder al ultimo valor

#2
#Recorrido y conteo (Básico)
notas = [12, 8, 15, 19, 10, 14]
contador = 0

for nota in notas:
    if nota >= 14:
        contador += 1

print("Cantidad de notas ≥ 14:", contador)


#3
# Llenado con datos simulados (Básico)
# Crear un arreglo de 5 edades inicializado en cero
edades = [0, 0, 0, 0, 0]


edades = [21, 18, 30, 25, 19]


for i in range(len(edades)):
    print(i, "→", edades[i])

#4
nombres = ['Ana', 'Luis', 'Mar', 'Sofi']


nombres[2] = 'María'


print("Elemento actualizado:", nombres[2])


print("Arreglo completo:", nombres)

#5
# Inserción conceptual con desplazamiento (Intermedio)
arr = [10, 20, 30, 40, None]

print("Estado inicial:", arr)


for i in range(len(arr)-1, 2, -1):
    arr[i] = arr[i-1]
    print("Después de mover índice", i, "→", arr)


arr[2] = 25

print("Resultado final:", arr)


#6
#Borrado conceptual con desplazamiento (Intermedio)
arr = [4, 6, 8, 10, 12]

print("Estado inicial:", arr)


for i in range(2, len(arr)-1):
    arr[i] = arr[i+1]
    print("Después de mover índice", i, "→", arr)


arr[-1] = None

print("Resultado final:", arr)

#7
#Búsqueda lineal (Intermedio)
datos = [7, 2, 9, 4, 2]
buscado = 2
encontrado = False  

for i in range(len(datos)):
    if datos[i] == buscado:
        print("Encontrado en índice:", i)
        encontrado = True
        break  

if not encontrado:
    print("No encontrado")

#8
#Traza de Burbuja (Intermedio)
a = [5, 1, 4, 2]
n = len(a)

print("Estado inicial:", a)


for pasada in range(n - 1):
    for i in range(n - 1 - pasada):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    print("Después de pasada", pasada + 1, ":", a)

print("Arreglo ordenado:", a)

#9
# Burbuja optimizada y métricas (Avanzado)
a = [3, 2, 4, 1, 5]
n = len(a)
comparaciones = 0
intercambios = 0

print("Estado inicial:", a)

for pasada in range(n - 1):
    hubo_cambio = False

    for i in range(n - 1 - pasada):
        comparaciones += 1
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            intercambios += 1
            hubo_cambio = True

    print("Después de pasada", pasada + 1, ":", a)

    if not hubo_cambio:
        break  # Se detiene si no hubo intercambios

print("\nComparaciones totales:", comparaciones)
print("Intercambios totales:", intercambios)
print("Arreglo final:", a)

