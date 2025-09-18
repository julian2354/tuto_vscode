for i in range(1, 11):
    print(i, end=" ")

#punto 2
for i in range(10, 0, -1):
    print(i, end=" ")

#punto 3
suma = 0   

for i in range(1, 101):  
    suma = suma + i      

print("La suma es:", suma)

#punto 4
for i in range(1, 21):
    if i % 2 != 0:   
        continue     
    print(i, end=" ")
print()  

#punto 5
for i in range(1, 11):
    resultado = 7 * i
    print(f"7 x {i} = {resultado}")

#punto 6
# Pedir cuántos números se van a ingresar
N = int(input("¿Cuántos números quieres promediar? "))

suma = 0  
for i in range(N):
    numero = float(input(f"Ingresa el número {i+1}: "))
    suma = suma + numero  

if N > 0:
    promedio = suma / N
    print("El promedio es:", promedio)
else:
    print("No se puede calcular el promedio de 0 números.")

#punto 7
# Pedir un número al usuario
n = int(input("Ingrese un número: "))

# Ciclo while para contar hacia atrás
while n >= 0:
    print(n)
    n = n - 1   # restamos 1 en cada iteración

#punto 8

# Inicializamos acumuladores
suma = 0
conteo = 0

while True:
    monto = float(input("Ingrese un monto (0 para terminar): "))
    
    if monto == 0:
        break  # sentinela: salir del ciclo
    
    suma += monto      # acumula el monto
    conteo += 1        # cuenta la cantidad de montos

print(f"Se ingresaron {conteo} montos")
print(f"El total es: {suma}")

#punto 9

# Pedir una nota válida entre 0 y 5
nota = float(input("Ingrese una nota entre 0 y 5: "))

while nota < 0 or nota > 5:   # condición de invalidez
    print("❌ Nota inválida. Debe estar entre 0 y 5.")
    nota = float(input("Ingrese una nota entre 0 y 5: "))

print(f"✅ La nota válida es: {nota}")

#punto 10
# Inicializamos la bandera
encontrado = False

while True:
    nombre = input("Ingrese un nombre (ENTER vacío para terminar): ")
    
    if nombre == "":   # condición de parada (sentinela)
        break
    
    if nombre.lower().startswith("a"):  # convierte todo a minúscula y revisa si empieza con 'a'
        encontrado = True

# Mostrar resultado
if encontrado:
    print("✅ Se encontró al menos un nombre que empieza con 'A'")
else:
    print("❌ No se encontró ningún nombre que empiece con 'A'")

#punto 11
#Inicializamos el total
total = 0

while True:
    print("\n--- MENÚ ---")
    print("1) Sumar al total")
    print("2) Ver total")
    print("0) Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        numero = float(input("Ingrese un número a sumar: "))
        total += numero
        print(f"✅ Se sumó {numero}. Nuevo total: {total}")
    
    elif opcion == "2":
        print(f"📊 El total actual es: {total}")
    
    elif opcion == "0":
        print("👋 Saliendo del menú...")
        break  # rompe el ciclo while
    
    else:
        print("❌ Opción inválida. Intente de nuevo.")

#punto 12
# Inicializamos lista para guardar los números
numeros = []

while True:
    dato = input("Ingrese un número (ENTER vacío para terminar): ")
    
    if dato == "":   # sentinela: cadena vacía
        break
    
    numero = float(dato)
    numeros.append(numero)

# Verificar si hubo datos
if len(numeros) > 0:
    minimo = min(numeros)
    maximo = max(numeros)
    print(f"✅ Mínimo: {minimo}")
    print(f"✅ Máximo: {maximo}")
else:
    print("❌ No se ingresaron datos.")

