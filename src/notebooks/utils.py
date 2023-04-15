import numpy as np
import random
import os                        # Para manipular directorios y archivos
import cv2                       # Para procesamiento de imágenes (visión artificial)
from skimage.io import imread    # Para lectura de imagenes


# CONSTANTES PARA LAS CARACTERISTICAS DE LAS IMAGENES Y EL MODELO 

IMAGE_HEIGHT = 350
IMAGE_WIDTH = 350
IMAGE_CHANNELS = 3   # RGB o color (3) // ByN o escala grises (1)
DATA_PATH = "../../../data_ML/" 
BATCH_SIZE = 10
EPOCHS = 50


# FUNCIONES DE UTILIDAD

def loadImage(image_path, image_height, image_width, grey_scale:bool = False) -> tuple(np.array, np.array):
    '''Función para leer datos (archivos de imagen) de forma iterativa.

    Input (path): Ruta de los archivos.
    Input (image_height, image_width): Dimensiones de alto y ancho con las que se cargarán los archivos de imagen (resize).
    Input (color): Booleano que configura la lectura de las imágenes en escala de grises. If 'True' converts color images to gray-scale.
        
    Output: Tuple(np.array X, np.array Y)
    
    ''' 
    X = []
    Y = []
    
    image_list = os.listdir(image_path) # Lista de los nombres de los archivos en el directorio especificado.
    
    if grey_scale: # If True
         
        for img in image_list:
            image_loaded = cv2.imread(image_path + img, flags=cv2.IMREAD_GRAYSCALE)  # Ajustamos lectura en escala de grises. Tambien imread(image_path +img, True) y channel 1.  
            image_resized = cv2.resize(image_loaded, (image_height, image_width))    # Cambiamos resolución de la imagen

            X.append(image_resized)

            if 'normal' in img:
                Y.append(0)
            else:
                Y.append(1)


        return (np.array(X), np.array(Y))
    
    else: # If False

        for img in image_list:
            image_loaded = imread(image_path + img)
            imagen_resized = cv2.resize(image_loaded, (IMAGE_HEIGHT, IMAGE_WIDTH)) # Cambiamos resolución de la imagen

            X.append(imagen_resized)

            if 'normal' in img:
                Y.append(0)
            else:
                Y.append(1)


        return (np.array(X), np.array(Y))
    


def balanceData(data_path) -> list(str):
    '''Función para balancear los datos del dataset para algoritmos de clasificación binaria.

    Input (path): Ruta de los archivos.
        
    Output: Lista de strings con los nombres de los archivos.
    
    ''' 
    image_list = os.listdir(data_path)
    category1_list = [img for img in image_list if 'normal' in img] 
    category2_list = [img for img in image_list if 'atipica' in img] 

    while len(category1_list) > len(category2_list):
        category1_list.remove(random.choice(category1_list))

    while len(category1_list) < len(category2_list):
        category2_list.remove(random.choice(category2_list))

    return category1_list + category2_list