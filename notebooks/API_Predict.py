import streamlit as st 
from pickle import load
import joblib
import os


# # Correspondence

# dicc_municipality = load(open('../data/interim/diccionarios/dicc_tipo_estacion.pk', 'rb'))
# dicc_area = load(open('../data/interim/diccionarios/dicc_tipo_estacion.pk', 'rb'))
# dicc_station = load(open('../data/interim/diccionarios/dicc_tipo_estacion.pk', 'rb'))
# dicc_magnitudes = load(open('../data/interim/diccionarios/dicc_tipo_estacion.pk', 'rb'))


# # Title
# st.title('Nivel de peligrosidad de contaminantes atmosféricos')

# # Introductory message
# st.write('Introduzca los siguientes valores para iniciar.')

# # Users data
# sel_municipality = st.selectbox('Seleccione el municipio:', dicc_municipality)
# sel_area = st.selectbox('Seleccione el tipo de área:', dicc_area)
# sel_station = st.selectbox('Seleccione el tipo de estación:', dicc_station)
# sel_magnitud = st.selectbox('Seleccione la magnitud:', dicc_magnitudes)
# mean_value = st.slider('Introduzca el valor recogido:',
#                     min_value = 0.04,
#                     max_value = 800.00,
#                     step = 0.01
#                     )

# model_path = os.path.join('models', 'DecisionTree_23.sav')
# model = joblib.load(model_path)


# def perform_prediction(sel_municipality, sel_area, sel_station, sel_magnitud, mean_value, model):
#     input_data = [[sel_municipality, sel_area, sel_station, sel_magnitud, mean_value]]

#   # Create a button for prediction
#     if st.button("Predecir"):
#         # Call a function to perform prediction
#         prediction_result = perform_prediction(sel_municipality, sel_area, sel_station, sel_magnitud, mean_value, model)
        
#         # Display the prediction result
#         st.success(f"Nivel de peligrosidad: {prediction_result}")

#     # Create a dictionary with the user's entries
#     user_input = {
#         "Municipio": sel_municipality,
#         "Tipo de área": sel_area,
#         "Tipo de estación": sel_station,
#         "Magnitud": sel_magnitud,
#         "Media diaria": mean_value
#     }

#     # Display the dictionary in the application
#     st.write("Entrada del usuario:", user_input)

#     # Map the numerical result to labels
    
# danger = {
#         0: "Baja",
#         1: "Normal",
#         2: "Alta"
# }
#     # Make prediction using the model
# prediction = model.predict(input_data)[0]


#     # Returns the type and description corresponding to the predicted star type
#         return danger.get(prediction)

# if __name__ == "__main__":
#     main()


import streamlit as st
from pickle import load
import os
import joblib

# # Assuming the correct paths are set for each dictionary
# dicc_municipality = load(open('../data/interim/factorize_values/N_MUNICIPIO_correspondencia.pkl', 'rb'))
# dicc_area = load(open('../data/interim/factorize_values/TIPO_AREA_correspondencia.pkl', 'rb'))
# dicc_station = load(open('../data/interim/factorize_values/TIPO_ESTACION_correspondencia.pkl', 'rb'))
# dicc_magnitudes = load(open('../data/interim/factorize_values/MAGNITUD_correspondencia.pkl', 'rb'))
# dicc_danger = load(open('../data/interim/factorize_values/PELIGROSIDAD_correspondencia.pkl', 'rb')) 

# model = load(open('../notebooks/DecisionTreeMadrid_23.pk', 'rb'))

# def perform_prediction(sel_municipality, sel_area, sel_station, sel_magnitud, mean_value, model):
#     input_data = [[sel_municipality, sel_area, sel_station, sel_magnitud, mean_value]]
#     prediction = model.predict(input_data)[0]
#     danger = dicc_danger
#     return danger.get(prediction)

# def main():
#     st.title('Nivel de peligrosidad de contaminantes atmosféricos')
#     st.write('Introduzca los siguientes valores para iniciar.')

#     sel_municipality = st.selectbox('Seleccione el municipio:', list(dicc_municipality.keys()))
#     sel_area = st.selectbox('Seleccione el tipo de área:', list(dicc_area.keys()))
#     sel_station = st.selectbox('Seleccione el tipo de estación:', list(dicc_station.keys()))
#     sel_magnitud = st.selectbox('Seleccione la magnitud:', list(dicc_magnitudes.keys()))
#     mean_value = st.slider('Introduzca el valor recogido:', min_value=0.04, max_value=800.00, step=0.01)

#     if st.button("Predecir"):
#         prediction_result = perform_prediction(sel_municipality, sel_area, sel_station, sel_magnitud, mean_value, model)
#         st.success(f"Nivel de peligrosidad: {prediction_result}")

#     user_input = {
#         "Municipio": sel_municipality,
#         "Tipo de área": sel_area,
#         "Tipo de estación": sel_station,
#         "Magnitud": sel_magnitud,
#         "Media diaria": mean_value
#     }

#     st.write("Entrada del usuario:", user_input)

# if __name__ == "__main__":
#     main()


import streamlit as st 
from pickle import load

dicc_municipality = load(open('../data/interim/diccionarios/N_MUNICIPIO_dicc.pk', 'rb'))
dicc_magnitudes = load(open('../data/interim/diccionarios/MAGNITUD_dicc.pk', 'rb'))
dicc_area = load(open('../data/interim/diccionarios/TIPO_AREA_dicc.pk', 'rb'))
dicc_station = load(open('../data/interim/diccionarios/TIPO_ESTACION_dicc.pk', 'rb'))
dicc_peligrosidad = load(open('../data/interim/diccionarios/PELIGROSIDAD_dicc.pk', 'rb'))


st.title('Nivel de peligrosidad de contaminantes atmosféricos')
# Introductory message
st.write('Introduzca los siguientes valores para iniciar.')

#Users data

mean_value = st.slider('Introduzca el valor recogido:',
                    min_value = 0.04,
                    max_value = 800.00,
                    step = 0.01
                    )

sel_municip = st.selectbox('Seleccione el municipio:','Seleccione el municipio:', dicc_municipality)

sel_magnitud = st.selectbox('Seleccione la magnitud:', dicc_magnitudes)

sel_area = st.selectbox('Seleccione el tipo de área:', dicc_area)

sel_station = st.selectbox('Seleccione el tipo de estación:', dicc_station)


# Load factorized values

fact_values = load(open('../data/interim/factorize_values/facto_madrid.pk', 'rb'))

# Button to predict

row = [mean_value,
    fact_values["N_MUNICIPIO_N"][sel_municip.lower()],
    fact_values["MAGNITUD_N"][sel_magnitud.lower()],
    fact_values["TIPO_AREA_N"][sel_area.lower()],
    fact_values["TIPO_ESTACION_N"][sel_station.lower()]
    ]

if st.button('Predict:'):

    model = load(open('../models/linear_regression.pk', 'rb'))
    y_pred = model.predict([row])

    st.text('The price of the insurance would be:' +str(round(y_pred[0, 0], 2)))