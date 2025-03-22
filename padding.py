import numpy as np

def padding(matriz, padding):
  filas, col, canales = matriz.shape
  output = np.zeros((filas+padding*2, col+padding*2, canales), dtype= matriz.dtype)
  output[padding: padding + filas, padding:padding + col, :] = matriz

  return output
