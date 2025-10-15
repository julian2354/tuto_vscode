#areglos de bidimensionales o matices 

#que es una matrix 
#definicion:




m =[ [3,1,2,],
     [0,5,9,],
     [6,8,2,]
]

# print(m[1][2])

# filas =len(m)
# colunmas =len(m[0])

# print(f"las dimensiones de este areglo son {filas} X {columnas} ")
# for c in range(cols):
#     for f in range (filas):
#         print(f"f={f}, c={c}") -> {m[f][c]}")

# n= len(m)
# cols= len(m[0])

# #validacion de cuadrada .

# if n == cols:
#     #diagonal principal
#     for i in range (n):
#         print(f"principal:{m[i][i]}")


# #diagonal secundaria 
# for i in range (n):
#     print(f"secundaria : {m[i][n - 1 -i]}")

#suma total de matiz

# total =  0

# for f in range (len(m)):
#     for c in range (len(m[0])):
#         total += m[f][c]


# print(f"suma total:{total}")

#sumas por fila y columnas
# filas = len(m)
# cols = len(m[0])

# #sumar por fila ...
# for f in range (filas):
#     suma_f = 0
#     for c in range (cols):
#         suma_f += m[f][c]
#     print(f"suma fila{f}:{suma_f}")


# #suma por colunmas 
# for c in range (cols):
#     suma_c = 0
#     for f in range (filas):
#         suma_c += m[f][c]
#         print(f"suma de colunmas {c}:{suma_c}")


#conteo con condicion.... (cuantos >5)

# m =[
# [3,1,2],
# [0,5,9],
# [6,8,2]
# ]

# conteo = 0
# for f in range(len(m)):
#     for c in range(len(m[0])):
#         if m [f][c]>5 :
#             conteo += 1
# print(f"mayores que 5:{conteo}")


#buscar el valor maximo y definir su ubucacion
# max_val =m[0][0]
# pos_f = 0
# pos_c =0

# for f in range(len(m)):
#     for c in range (len(m[0])):
#         if m [f][c] > max_val :
#             max_val = m[f] [c]
#             pos_f =f
#             pos_c =c

# print(f"el maximo:{max_val},ubicado en : {pos_f},{pos_c}")

#tranformacion de suma 1 a cada elemento

# for f in range (len(m)):
#     for c in range (len(m[0])):
#         m[f] [c] = m[f] [c] +1

# print(m)


#tranposicion de matrices.

# m =[[1,2,3],     # 3x3
#     [4,5,6],
#     [7,8,9]
# ]
# filas = len(m)
# cols = len(m[0])

# t = []
# for c in range (cols):
#     nueva_fila = []
#     for f in range (filas):
#         nueva_fila.append(m[f] [c])
#     t.append(nueva_fila)

# print(f"arreglo og:{m}")
# print(f"transpuesta:{t}")
# for fila in t :
#     print(*[fila])

# n = len(m)

# for f in range(n):
#     for c in range(f + 1):
#         #intercambiar m [f][c] con m[c][f]
#         temp= m[f][c]
#         m[f] [c] = m[c][f]
#         m[c][f] = temp

# print(f" transpuesta in place: {m}")

# nota= float(input("introduzca su nota"))
# if nota < 5 :
#     print("esta suspendido")
# else:
#     print("has ganado tio")



