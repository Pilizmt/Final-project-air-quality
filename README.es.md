# **Nivel de peligrosidad de contaminantes atmosféricos🌍🔍**
---

![Logo](polucion.jpg)

## *Descripción del Proyecto*

Este proyecto tiene como objetivo predecir el nivel de peligrosidad de varios contaminantes atmosféricos en función de diferentes variables, como el tipo de área en la que se encuentra y los factores ambientales circundantes. La predicción del nivel de peligrosidad es esencial para comprender y mitigar los posibles riesgos asociados a la exposición a contaminantes en diferentes ubicaciones.


## *Objetivo principal:*

Este proyecto es importante porque permite predecir y comprender los niveles de contaminación del aire para:

- Proteger la salud pública.
- Facilitar la planificación urbana sostenible.
- Mejorar la calidad de vida de las personas.
- Fomentar la conciencia ambiental.
- Contribuir a la investigación científica en calidad del aire.

## *Descripción de los Datos* 📈

Los datos proceden de la página oficial del Gobierno de España, Ministerio para la Transición Ecológica y el Reto Demográfico.

Se introdujeron datos recogidos en la documentación de la página para obtener unos datos que nos ayuden a desarrollar la finalidad de nuestro proyecto.

Fuente: 

https://www.miteco.gob.es/es/calidad-y-evaluacion-ambiental/temas/atmosfera-y-calidad-del-aire/calidad-del-aire/evaluacion-datos/datos/datos-oficiales-2022.html


## *Estructura de los archivos*

- FECHA. Fecha registrada en el momento de la toma de valores de contaminantes (numérico).
- N_CCAA. Nombre de cada comunidad autónoma de España donde se han recogido datos de medición de cada contaminante (categórico)
- PROVINCIA. Nombre de cada provincia en la que se han recogido datos de medición de cada contaminante (categórico)
- N_MUNICIPIO. Nombre de cada municipio en el que se hayan recogido datos de mediciones de cada contaminante (categórico)
- ESTACIÓN. Número asignado a cada estación de cada comunidad autónoma que ha registrado datos de medición de contaminantes (numérico)
- MAGNITUD. Cada contaminante que se ha registrado en las distintas estaciones (categórico)
- TIPO_AREA.Tipo de zona en la que se encuentran, zona urbana, suburbana o rural (categórico).
- TIPO_ESTACION. Según la tipología de la fuente de emisión principal, tráfico, industrial o de fondo (categórico).
- LATITUD, LONGITUD. Datos geográficos de cada estación donde se han registrado los contaminantes (numérico).
- H01, H02, H03... H24. Valor registrado por hora de cada contaminante. Todos los contaminantes se han tomado con unidades de medida unificadas (µg/m3)(numérico)

## *Contaminantes* 🏭💨🚗

> Todos los datos de concentración están expresados en microgramos por metro cúbico (μg/m³).

| Contaminante                           | Nombre completo                      |
|----------------------------------------|-------------------------------------|
| С6Н6 (Benceno)                         | Benceno                             |
| CO (Monóxido de carbono)               | Monóxido de carbono                 |
| NO2 (Dióxido de nitrógeno)             | Dióxido de nitrógeno                |
| NOX (Óxidos de nitrógeno)              | Óxidos de nitrógeno                 |
| O3 (Ozono)                             | Ozono                               |
| PM10 (Partículas diámetro 10 μm)       | Partículas diámetro 10 μm           |
| PM2.5 (Partículas diámetro 2.5 μm)     | Partículas diámetro 2.5 μm         |
| SO2 (Dióxido de azufre)                | Dióxido de azufre                   |

## *Características Principales*

- Análisis Exploratorio de los Datos (EDA)
- Visualización de datos a través de gráficos y tablas.
- Ingeniería de características: Se han creado nuevas caractarísticas a partir de las existentes para mejorar el rendimiento del modelo.
- Selección de características: Decidir qué características se incluirán en el modelo final en función de su importancia y relevancia.
- Creación y entrenamiento de un modelo de machine learning para predecir el nivel de peligrosidad de cada contaminante.

## *Tecnologías Utilizadas*

- Python 🐍
- Pandas 🐼
- Numpy 🧮
- Matplotlib/Seaborn 📊
- Pickle 🥒
- Scikit-learn 🤖 (para el modelo de machine learning)
- Streamlit 🌐 (para desarrollar la aplicación web interactiva)

## *Estructura del Proyecto*

- `data/`: Carpeta que contiene los conjuntos de datos utilizados, procesados y temporales.
- `models/`: Carpeta que contiene los modelos de machine learning.
- `notebooks/`: Carpeta que contiene los cuadernos utilizados para el Análisis Exploratorio de los Datos (EDA) y la construcción del modelo Random Forest
- `src/`: Carpeta que contiene el código para desplegar el modelo usando streamlit.
- `README.md`: Documentación del proyecto (este archivo). 📚

## *Instrucciones de Ejecución*

1. Clona este repositorio:

   ```bash
   git clone (https://github.com/Yakondra/Final-project-air-quality.git)
   o
   git clone (https://github.com/Pilizmt/Final-project-air-quality.git)

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt

## *Render* 

- Para crear la página web se ha usado: https://render.com/

- Enlace a la web interactiva: https://air-quality-predict.onrender.com/

## *Cómo Contribuir*

¡Las contribuciones son bienvenidas! Si encuentras problemas, tienes ideas para mejoras o deseas agregar nuevas características, siéntete libre de enviar un pull request. 🤝🚀