import numpy as np 
import random
from typing import List          # Para la función de balanceData()
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

def loadImage(image_list, image_path, image_height, image_width, grey_scale:bool = False) -> tuple:
    '''Función para leer datos (archivos de imagen) de forma iterativa.

    Input (image_list): Lista de los nombres de los archivos de imagenes a leer.
    Input (path): Ruta donde se encuentran los archivos.
    Input (image_height, image_width): Dimensiones de alto y ancho con las que se cargarán los archivos de imagen (resize).
    Input (color): Booleano que configura la lectura de las imágenes en escala de grises. If 'True' converts color images to gray-scale.
        
    Output: Tuple(np.array X, np.array Y)
    
    ''' 
    X = []
    Y = []

    if grey_scale: # If True -> EN BLANCO Y NEGRO
         
        for img in image_list:
            image_loaded = cv2.imread(image_path + img, flags=cv2.IMREAD_GRAYSCALE)  # Ajustamos lectura en escala de grises. Tambien imread(image_path +img, True) y channel 1.  
            image_resized = cv2.resize(image_loaded, (image_height, image_width))    # Cambiamos resolución de la imagen

            X.append(image_resized)

            if 'normal' in img:
                Y.append(0)
            else:
                Y.append(1)


        return (np.array(X), np.array(Y))
    
    else: # If False -> EN COLOR

        for img in image_list:
            image_loaded = imread(image_path + img)
            imagen_resized = cv2.resize(image_loaded, (IMAGE_HEIGHT, IMAGE_WIDTH)) # Cambiamos resolución de la imagen

            X.append(imagen_resized)

            if 'normal' in img:
                Y.append(0)
            else:
                Y.append(1)


        return (np.array(X), np.array(Y))
    


def balanceData(data_path) -> tuple: 
    '''Función para balancear los datos del dataset en algoritmos de clasificación binaria.

    Input (path): Ruta de los archivos del dataset.
        
    Output: Tupla de dos Lista de strings. La primera con los nombres de los archivos del dataset balanceado, y la segunda con los nombres de los archivos que hemos eliminado.
    
    ''' 
    image_list = os.listdir(data_path)
    category1_list: List[str] = [img for img in image_list if 'normal' in img] 
    category2_list: List[str] = [img for img in image_list if 'atipica' in img]
    storelist: List[str] = []

    while len(category1_list) > len(category2_list):
        image_dropped = category1_list.pop(random.randint(0,(len(category1_list)-1)))
        storelist.append(image_dropped)

    while len(category1_list) < len(category2_list):
        image_dropped = category2_list.pop(random.randint(0,(len(category2_list)-1)))
        storelist.append(image_dropped)


    return category1_list + category2_list, storelist