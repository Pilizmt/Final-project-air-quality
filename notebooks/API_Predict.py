import streamlit as st 
from pickle import load
import pickle

dicc_area = load(open('../data/interim/diccionarios/dicc_area.pk', 'rb'))
dicc_ccaa = load(open('../data/interim/diccionarios/dicc_ccaa.pk', 'rb'))
dicc_estacion = load(open('../data/interim/diccionarios/dicc_estacion.pk', 'rb'))
dicc_magnitudes = load(open('../data/interim/diccionarios/dicc_magnitudes.pk', 'rb'))
dicc_municipios = load(open('../data/interim/diccionarios/dicc_municipios.pk', 'rb'))
dicc_provincias = load(open('../data/interim/diccionarios/dicc_provincias.pk', 'rb'))


name_municipality = st.selectbox('Selecciona el nombre del Municipio:',
                                 )



# ipyleaflet>=0.14.0
# ipywidgets>=7.7.1
# matplotlib>=3.7.0
# numpy>=1.24.2
# opencv-python>=4.1.2
# pandas>=1.5.3
# python-dotenv>=0.20.0
# requests>=2.27.1
# scikit-learn>=1.3.2
# seaborn>=0.12.2
# streamlit==1.31.0
# joblib
