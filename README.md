# Evidencias Individuales Semana Tec

### Carlos Alberto Amador Amador A01253409

## Descripción

En este repositorio se encuentra la implementación de una función que realiza una operación de convolución sobre una matriz de entrada utilizando un kernel especificado. La convolución se aplica a la matriz, realizando una serie de multiplicaciones y sumas entre los valores de la matriz y el kernel, generando como resultado una nueva matriz filtrada.

Además, se incluye la implementación de una función de padding, que se aplica después de la convolución. Esta función agrega un borde de ceros alrededor de la matriz original antes de realizar la convolución, lo que permite mantener las dimensiones de la matriz resultante y evitar la pérdida de información en los bordes de la imagen o matriz.

Estas funciones han sido diseñadas con el propósito de aplicar filtros a imágenes. El proceso comienza con la conversión de la imagen a una matriz utilizando la librería OpenCV (CV2). Una vez que la imagen ha sido transformada en una matriz numérica, el programa puede aplicar la convolución y el padding de manera eficiente sobre los datos.

Después de aplicar el filtro a la matriz, la matriz resultante se convierte nuevamente a una imagen que puede ser visualizada, permitiendo observar los efectos del filtro aplicado en la imagen original.

## Requisitos para ejecutar el programa

- Cualquier version de Python3
- Libreria Numpy
- Libreria Matplotlib
- Libreria OpenCv2

\*\*Se recomienda utilizar un entorno virtual para instalar estas librerias pero tambien se pueden instalar directamente en la computadora donde se ejecute el programa

## Pruebas

El filtro a aplicar es un filtro de nitidez que busca alzar los contrastes en la imagen. El padding aplicado sera de 0s como se menciono anteriormente.

![Antes](img/papel.jpg)

![Despues](img/output.png)
