import streamlit as st 
from pickle import load
import pickle

dicc_area = load(open('../data/interim/diccionarios/dicc_area.pk', 'rb'))
dicc_ccaa = load(open('../data/interim/diccionarios/dicc_ccaa.pk', 'rb'))
dicc_estacion = load(open('../data/interim/diccionarios/dicc_estacion.pk', 'rb'))
dicc_magnitudes = load(open('../data/interim/diccionarios/dicc_magnitudes.pk', 'rb'))
dicc_municipios = load(open('../data/interim/diccionarios/dicc_municipios.pk', 'rb'))
dicc_provincias = load(open('../data/interim/diccionarios/dicc_provincias.pk', 'rb'))


