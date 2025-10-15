# Bucles anidados, tablas y patrones.

#por que anidar?

#cuando los ejercicios o el problema que tenemos que solucionar 
# requiere que hagamos multiples iteraciones sobre un valor que ya se esta iterando, tenemos que anidar.

# for numerin in range(1, 11):
#     for numeron in range(1, 11):
#         print(f"{numerin} x {numeron} = {numerin * numeron}")
#     print()

# coordenada cartesiana

for fila in range(1, 19):
    for col in range(1, 10):
        print(f"({fila}, {col})", end=" ")
    print()


#rectangulo de asteriscos al que le vamos a pasar alto x ancho
# alto = int(input("ingrese el valor del alto: "))
# ancho = int(input("ingrese el valor del ancho: "))

# for i in range(alto):
#     fila = ""
#     for j in range(ancho):
#         fila = fila + "*"
#     print(fila)

n = 16
for i in range(1 ,n+1):
    linea = ""
    for j in range(i):
        linea = linea + "#"
    print(linea)

# n = 16
# for i in range(1, n+1):
#     espacios = ""
#     signos = ""
#     for e in range(n - i):
#         espacios = espacios + " "
#     for s in range(i):
#         signos = signos + "#"
#     print(espacios + signos)


# while True:
#     print("\n1) Ver tabla de multiplicar NxM")
#     print("0) Salir")
#     op = input("Opción: ").strip()
#     if op == "0":
#         print("Adiós")
#         break
#     elif op == "1":
#         n = int(input("Filas (N): "))
#         m = int(input("Columnas (M): "))
#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 print(i*j, end="\t")
#             print()
#     else:
#         print("Inválida")
#plano cartesiano
for fila in range(1, 12):
    for col in range(1, 12):
        print (f"({fila}, {col})", end=" ")
    print()

fila= int()

