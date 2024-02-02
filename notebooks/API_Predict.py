import streamlit as st 
import pickle
import os
import joblib
import warnings

from sklearn.exceptions import InconsistentVersionWarning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

model_path = os.path.join('models', 'RandomForestMadrid_23.pk')
model = joblib.load(model_path)

with open('/data/interim/diccionarios/dicc_magnitudes.pk', "rb") as file:
    objeto_cargado = pickle.load(file)