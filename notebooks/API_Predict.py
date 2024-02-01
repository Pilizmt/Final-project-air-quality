import streamlit as st 
import pickle
import os
import joblib

model_path = os.path.join('models', 'RandomForestMadrid_23.pk')
model = joblib.load(model_path)

with open("../data/interim/dicc_municipios.pkl", "rb") as archivo:
    dicc_municipios = pickle.load(archivo)

# def main():
#     st.title("Star type prediction")

#     # Introductory message
#     st.write("Welcome. Please enter the following data to predict the type of star.")
#     # User input
#     temperature = st.slider(
#         "Temperature (K)",
#         min_value=2000,
#         max_value=40000,
#         value=15000)

#     luminosity = st.slider(
#         "Luminosity (L/Lo)",
#         min_value=0.00001,
#         max_value=100000.0,
#         value=1.0)

#     radius = st.slider(
#         "Radio (R/Ro)",
#         min_value=0.01,
#         max_value=100.0,
#         value=1.0)

#     absolute_magnitude = st.slider(
#         "Absolute Magnitude (Mv)",
#         min_value=-10,
#         max_value=20,
#         value=10)

# if st.button("Predict"):
#         # Call a function to perform prediction
#         prediction_result = perform_prediction(temperature, luminosity, radius, absolute_magnitude, model)


# def perform_prediction(temperature, luminosity, radius, absolute_magnitude, model):
#     input_data = [[temperature, luminosity, radius, absolute_magnitude]]

#     # Make prediction using the model
#     prediction = model.predict(input_data)[0]

#     # Map the numerical result to labels
#     star_types = {
#         0: "Brown Dwarf",
#         1: "Red Dwarf",
#         2: "White Dwarf",
#         3: "Main Sequence",
#         4: "Supergiant",
#         5: "Hypergiant"
#     }

# def clasificar_peligrosidad(valor, umbrales):
#     if valor < umbrales['bajo']:
#         return 'Baja'
#     elif valor < umbrales['alto']:
#         return 'Normal'
#     else:
#         return 'Alta'


# umbrales_peligrosidad = {
#     'SO2': {'bajo': 25, 'alto': 40},
#     'CO': {'bajo': 2, 'alto': 4},
#     'C6H6': {'bajo': 2, 'alto': 5},
#     'NO2': {'bajo': 15, 'alto': 25},
#     'PM2.5': {'bajo': 10, 'alto': 15},
#     'PM10': {'bajo': 25, 'alto': 45}, 
#     'NOX': {'bajo': 75, 'alto': 100},
#     'O3': {'bajo': 75, 'alto': 100}
# }