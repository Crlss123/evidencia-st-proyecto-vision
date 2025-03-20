import numpy as np

def conv_helper(matriz, kernel, i, j):
  #multiplica dos matrices y se suman los resultados
  filas_kernel = len(kernel)
  col_kernel = len(kernel[0])
  total = 0

  #se recorre la matriz original con ayuda de i,j para recorrerla
  for fila in range(filas_kernel):
    for col in range(col_kernel):
      total += matriz[fila + i][col + j] * kernel[fila][col]

  return total

def convolution(matriz, kernel):
  filas_matriz = len(matriz)
  col_matriz = len(matriz[0])
  filas_kernel = len(kernel)
  col_kernel = len(kernel[0])

  #Se establecen las dimensiones de la matriz resultante
  filas_salida = filas_matriz - filas_kernel + 1
  col_salida = col_matriz - col_kernel + 1
  salida = np.zeros((filas_salida, col_salida))

  for i in range(filas_salida):
    for j in range(col_salida):
      salida[i][j] = conv_helper(matriz, kernel, i, j)

  return salida
