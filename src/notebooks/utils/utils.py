# CONSTANTES PARA LAS CARACTERISTICAS DE LAS IMAGENES Y EL MODELO 

IMAGE_HEIGHT = 125
IMAGE_WIDTH = 125
IMAGE_CHANNELS = 3   # RGB o color (3) // ByN o escala grises (1)
DATA_PATH = "../../../data_ML/" 
BATCH_SIZE = 16
EPOCHS = 50
PATIENCE = 13
STEP = 100


# FUNCIONES DE UTILIDAD

def balanceData(data_list) -> tuple: 
    import random
    from typing import List 
    '''Función para balancear datos en algoritmos de clasificación binaria. Para datasets con dos categorias.

    Input (data_list): Lista con los nombres de los archivos a equilibrar por categoria.
        
    Output: Tupla de dos Lista de strings. La primera lista con los nombres de los archivos equilibrados por categorias,
            y la segunda con los nombres de los archivos que se han eliminado.
    
    ''' 
    category_1: List[str] = [img for img in data_list if 'normal' in img] 
    category_2: List[str] = [img for img in data_list if 'atipica' in img]
    storelist: List[str] = []

    while len(category_1) > len(category_2):
        item_dropped = category_1.pop(random.randint(0,(len(category_1)-1)))
        storelist.append(item_dropped)

    while len(category_1) < len(category_2):
        item_dropped = category_2.pop(random.randint(0,(len(category_2)-1)))
        storelist.append(item_dropped)

    balanced_dataset = category_1 + category_2
    return balanced_dataset, storelist



def loadImage(image_list, image_path, image_height, image_width, grey_scale:bool = False) -> tuple:
    import numpy as np 
    import cv2                       
    from skimage.io import imread  
    '''Función para leer datos de imagen de forma iterativa.

    Input (image_list): Lista con los nombres de los archivos a leer.
    Input (image_path): Ruta donde se encuentran los archivos.
    Input (image_height, image_width): Dimensiones de alto y ancho con las que se cargarán los archivos de imagen (resize).
    Input (grey_scale): Booleano que configura la lectura de las imágenes en escala de grises. If 'True' converts color images to gray-scale.
        
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
    
    # TODO Funcion para representar las imagenes donde no precide bien el modelo (para estudiar casos).