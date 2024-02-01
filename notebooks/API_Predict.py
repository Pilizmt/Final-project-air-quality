import streamlit as st 
from pickle import dump
import pickle
import os
import joblib

model_path = os.path.join('models', 'RandomForestMadrid_23.pk')
model = joblib.load(model_path)


input_data = {
    'LATITUD': valor_latitud,
    'LONGITUD': valor_longitud,
    'MEDIA_DIARIA': valor_media_diaria,
    'N_MUNICIPIO_N': valor_municipio,
    'MAGNITUD_N': valor_magnitud,
    'TIPO_AREA_N': valor_tipo_area,
    'TIPO_ESTACION_N': valor_tipo_estacion,
    'PELIGROSIDAD_N': valor_peligrosidad
}