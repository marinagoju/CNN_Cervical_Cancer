![imagen](https://github.com/marinagoju/ML-Classifier-citology/blob/main/src/data/portada.jpg)
# <div align="center">**Redes neuronales convolucionales en screening de cáncer de cérvix**</div>

En este proyecto se muestra el desarrollo de un modelo de detección de cancer cervical basado en redes neuronales convolucionales.
El algoritmo que se propone es un clasificador de imágenes de citologías cervicovaginales al microscopio a nivel celular, es decir en base las características celulares de células aisladas en frotis de cérvix (pap smear).
<br></br> 

1. [Dataset y metodología de trabajo](#id1)
2. [Entrenamiento del modelo](#id2)
3. [Resultados y conclusiones](#id3) 
4. [Comentarios del autor](#id4)
5. [Librerías y recursos](#id5)<br></br>

***¿Por qué un modelo de clasificación de cáncer cervical?***<br></br>

El cáncer de cuello de útero es un problema de salud creciente y una causa importante de mortalidad en las mujeres en todo el mundo. 
Según la Organización Mundial de la Salud (OMS) el carcinoma cervical es el cuarto tipo de cáncer más común entre las mujeres y uno de los cánceres que mayor incidencia de mortalidad tiene. 

Desde que en 1928 el médico griego Papanicolaou descubrió que se podían detectar células cancerosas en frotis cervicovaginales, la citología cervicovaginal ha sido la técnica de cribado por excelencia para detectar lesiones precancerosas en células del cérvix uterino y prevenir sus consecuencias. Lo que ha supuesto hasta ahora una drástica reducción de la incidencia y mortalidad femenina de este tipo de cáncer. No obstante, es una prueba que requiere un trabajo visual y manual exhaustivo y muy repetitivo por parte del citopatólogo. 

Hoy en día, el ingente volumen de muestras citológicas recibidas en los laboratorios, unido a la escasez de facultativos especializados en el sector, obligan a enfrentar la necesidad de incorporar en la práctica clínica nuevas técnicas automatizadas de diagnóstico que auxilien a los citopatólogos en la detección de células precancerosas o cancerosas, y como otras anomalías cervicales, minimizando el esfuerzo manual exhaustivo del facultativo. Es así como surge la idea de crear un algoritmo que reduzca la carga de trabajo del profesional sanitario.
<br></br>

<div id='id1'/>
<h2> 🔎 1. Dataset y metodología de trabajo</h2>

El dataset sobre el que trabajamos fue obtenido de la base de datos de [SIPakMed ](https://www.cs.uoi.gr/~marina/sipakmed.html)

Consta de 4049 imágenes de células aisladas recortadas a partir de 966 imágenes de frotis cervicovaginales (con tinción Papanicolau), las cuales fueron obtenidas mediante de una cámara CCD incorporada a un microscopio óptico.

Las células que refieren las imágenes incluyen células del epitelio cervical superficiales, intermedias, parabasales, células metaplásicas de la zona de transformación cervical, así como células disqueratósicas y coilocíticas atípicas. 

Para simplificar el tratamiento de los datos, se agruparon las imágenes en dos categorías: 
- células normales. Incluimos células epiteliales escamosas estratificadas (no queratinizadas) superficiales, intermedias y parabasales, así como células metaplásicas benignas (transformadas) de la zona de transformación cervical.
- Células atípicas. Incluimos aquí las células disqueratósicas y coilocíticas frecuentemente asociadas a neoplasias cervicales previa infección por el VPH.
<br></br>

<div id='id2'/>
<h2> 📑 2. Entrenamiento del modelo</h2>

Como hemos mencionado anteriormente, uno de los pasos clave en el proceso de tratamiento de datos, fue clasificar las imágenes de los diferentes tipos celulares en dos categorías: células normales, y células atípicas. A la primera categoría le asignamos el número 0 y a la segunda categoría el número 1.

La categoría de células normales la constituyen aquellas que encontramos habitualmente en una prueba de Papanicolau (citología cervico-vaginal). La categoría de células atípicas  son aquellas cuya presencia constituye una evidencia típicamente patognomónica de la infección por VPH y por tanto de lesiones potencialmente cancerosas o precancerosas.

Otro aspecto crucial en el procesado de los datos fue ajustar todas las imágenes a la misma resolución y dimensión, así como ajustar la configuración para poder cargarlas en blanco y negro o a color para hacer las pruebas.

En el notebook se muestran dos modelos, un modelo estandar de redes neuronales convolucionales con tres capas, una de input, hiden y output respectivamente, y otro en el que se implementa el algoritmo preentrenado VGG-16 en la capa de entrada (transfer learning).
<br></br>

<div id='id3'/>
<h2> 📋 3. Resultados y conclusiones</h2>

El modelo que tuvo mejor scoring con un % de exactutud y una pérdida de %, fue en el que implementamos el modelo preentrenado de VGG-16, aunque en el repositorio se pueden revisar ambos.<br></br>

<div id='id4'/>
<h2> 💬 4. Comentarios del autor</h2>

Proximamente realizaremos pruebas adicionales con el dataset de imagenes de Herlev.<br></br>

<div id='id5'/>
<h2> ⚙️ 5. Librerías y recursos</h2>

- Keras
- Tensorflow
- Matplotlib
- Seaborn
- Pandas
- Numpy
- Opencv2
- os
- random
- skimage
- sklearn
- Canvas
