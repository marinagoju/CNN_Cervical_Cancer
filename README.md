![imagen](https://github.com/marinagoju/ML-Classifier-citology/blob/main/src/data/recortada1.jpg)
# <div align="center">**Clasificador cáncer cervical en citología de cérvix**🔬</div>

En este repositorio se plantea un modelo predictivo de redes convolucionales basado en un clasificador de imágenes de citologías cervicovaginales a nivel celular, es decir fundado en las características de células aisladas procedentes del cuello del útero.
<br></br> 

1. [Dataset y metodología de trabajo](#id1)
2. [Análisis de datos](#id2)
3. [Resultados y observaciones generales](#id3) 
4. [Conclusiones](#id4)
5. [Comentarios del autor](#id5)
6. [Librerías y recursos](#id6)

<br></br>
***¿Por qué un modelo de clasificación de cáncer cervical?***<br></br>

El cáncer de cuello de útero es un problema de salud creciente y una causa importante de mortalidad en las mujeres en todo el mundo. 
Según la Organización Mundial de la Salud (OMS) el carcinoma cervical es el cuarto tipo de cáncer más común entre las mujeres y uno de los cánceres que mayor incidencia de mortalidad tiene. 

Desde que en 1928 el médico griego Papanicolaou descubrió que se podían detectar células cancerosas en frotis cervicovaginales, la citología cervicovaginal ha sido la técnica de cribado por excelencia para detectar lesiones precancerosas en células del cérvix uterino y prevenir sus consecuencias. Lo que ha supuesto hasta ahora una drástica reducción de la incidencia y mortalidad femenina de este tipo de cáncer. No obstante, es una prueba que requiere un trabajo visual y manual exhaustivo y muy repetitivo por parte del citopatólogo. 

Hoy en día, el ingente volumen de muestras citológicas recibidas en los laboratorios, unido a la escasez de facultativos especializados en el sector, obligan a enfrentar la necesidad de incorporar en la práctica clínica nuevas técnicas automatizadas de diagnóstico que auxilien a los citoopatólogos en la detección de células precancerosas o cancerosas, y como otras anomalías cervicales, minimizando el esfuerzo manual exhaustivo del facultativo. Es así como surge la idea de crear un algoritmo que reduzca la carga de trabajo del profesional sanitario.
<br></br>

<div id='id1'/>
<h2> 🔎 1. Dataset y metodología de trabajo</h2>

El dataset sobre el que trabajamos fue obtenido de la base de datos de SIPakMed: https://www.cs.uoi.gr/~marina/sipakmed.html (crear enlace)

Consta de 4049 imágenes de células aisladas recortadas a partir de 966 imágenes de frotis cervicovaginales (con tinción Papanicolau), las cuales fueron obtenidas mediante de una cámara CCD incorporada a un microscopio óptico.

Las células que refieren las imágenes incluyen células del epitelio cervical superficiales, intermedias, parabasales, células metaplásicas de la zona de transformación cervical, así como células disqueratósicas y coilocíticas atípicas. 

Para simplificar el tratamiento de los datos, hemos agrupado las imágenes en dos categorías: 
•	células normales. Incluimos células epiteliales escamosas estratificadas (no queratinizadas) superficiales, intermedias y parabasales, así como células metaplásicas benignas (transformadas) de la zona de transformación cervical.
•	Células atípicas. Incluimos aquí las células disqueratósicas y coilocíticas frecuentemente asociadas a neoplasias cervicales previa infección por el VPH.


<br></br>

<div id='id2'/>
<h2> 📑 2. Análisis de datos</h2>

Como hemos mencionado anteriormente, uno de los pasos clave en el proceso de tratamiento de datos, fue clasificar las imágenes de los diferentes tipos celulares en dos categorías: células normales, y células atípicas. A la primera categoría le asignamos el número 0 y a la segunda categoría el número 1.

La categoría de células normales la constituyen aquellas que encontramos habitualmente en una prueba de Papanicolau (citología cervico-vaginal). Estas son células superficiales, intermedias y parabasales del tipo epitelial escamoso estratificado no queratinizado, además de células metaplásicas benignas.

La categoría de células atípicas la constituyen células coilocíticas y disqueratócicas, cuya presencia constituye una evidencia típicamente patognomónica de la infección por VPH y por tanto de lesiones potencialmente cancerosas o precancerosas.

Otro aspecto crucial en el procesado de los datos fue ajustar todas las imágenes a la misma resolución y dimensión, así como ajustar la configuración para cargarlas en blanco y negro (1 canal o dimensión) y así reducir los features.


txt<br></br>

<div id='id3'/>
<h2> 📋 3. Resultados y observaciones generales</h2>

txt<br></br>

<div id='id4'/>
<h2> 📋 4. Conclusiones</h2>

txt<br></br>

<div id='id5'/>
<h2> 💬 5. Comentarios del autor</h2>

txt<br></br>

<div id='id6'/>
<h2> ⚙️ 6. Librerías y recursos</h2>

- Keras
- Matplotlib
- Pandas
- Canvas
