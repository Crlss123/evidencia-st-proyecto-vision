import numpy as np

def convolucion_helper(fragmento, kernel):
  # Declaracion de dimensiones del fragmento y de la matriz resultante
  filas_frag, col_frag, canales_frag = fragmento.shape
  result = np.zeros(canales_frag)

  # Aplica la convolucion para cada canal
  for canal in range(canales_frag):
    for row in range(filas_frag):
      for col in range(col_frag):
        result[canal] += fragmento[row, col, canal] * kernel[row, col]

  return result

def convolucion(matriz, kernel):
  # Declaracion de dimensiones de la matriz y el kernel
  filas_matriz, col_matriz, matriz_channels = matriz.shape
  filas_kernel, col_kernel = kernel.shape

  # Declaracion de dimensiones de la matriz resultante
  filas_salida = filas_matriz - filas_kernel + 1
  col_salida = col_matriz - col_kernel + 1
  salida = np.zeros((filas_salida, col_salida, matriz_channels))

  # Recorre la matriz y llama a la funcion de convolucion
  for i in range(filas_salida):
    for j in range(col_salida):
      salida[i,j] = convolucion_helper(matriz[i:i + filas_kernel, j:j + col_kernel], kernel)

  salida = np.clip(salida, 0, 255).astype(np.uint8)

  return salida
