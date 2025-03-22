from convolucion import convolucion
import numpy as np
import cv2
from padding import padding
import matplotlib.pyplot as plt

kernel_nitidez = np.array([
      [-1, -1, -1],
      [-1, 9, -1],
      [-1, -1, -1]
])

image = cv2.imread("img/papel.jpg", cv2.IMREAD_COLOR_RGB)
image = convolucion(image, kernel_nitidez)
image = padding(image, 1)

plt.imshow(image)
plt.axis('off')
plt.show()
