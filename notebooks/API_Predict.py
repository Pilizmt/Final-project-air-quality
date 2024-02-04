# import streamlit as st 
# from pickle import load
# import joblib
# import os


# # Dictionaries
# dicc_municipality = load(open('../data/interim/factorize_values/N_MUNICIPIO_correspondencia.pkl', 'rb'))
# dicc_area = load(open('../data/interim/factorize_values/TIPO_AREA_correspondencia.pkl', 'rb'))
# dicc_station = load(open('../data/interim/factorize_values/TIPO_ESTACION_correspondencia.pkl', 'rb'))
# dicc_magnitudes = load(open('../data/interim/factorize_values/MAGNITUD_correspondencia.pkl', 'rb'))
# # dicc_danger = load(open('../data/interim/factorize_values/PELIGROSIDAD_correspondencia.pkl', 'rb')) 

# model = load(open('../models/RandomForestMadrid_23.pk', 'rb'))

# def perform_prediction(sel_municipality, sel_area, sel_station, sel_magnitud, mean_value, model, danger_thresholds):
#     # input_data = [[sel_municipality, sel_area, sel_station, sel_magnitud, mean_value]]
#     # prediction = model.predict(input_data)[0]
#     # danger = dicc_danger
#     # return danger.get(prediction)

#     input_data = [[sel_municipality, sel_area, sel_station, sel_magnitud, mean_value]]
#     prediction = model.predict(input_data)[0]

#     contaminante = list(dicc_magnitudes.keys())[list(dicc_magnitudes.values()).index(sel_magnitud)]  # Asumiendo que sel_magnitud ya es numérico y necesitas el nombre
#     thresholds = danger_thresholds.get(contaminante)

#     if thresholds:
#         if mean_value <= thresholds['Bajo']:
#             nivel_peligrosidad = 'Bajo'
#         elif mean_value <= thresholds['Alto']:
#             nivel_peligrosidad = 'Normal'
#         else:
#             nivel_peligrosidad = 'Alto'
#     else:
#         nivel_peligrosidad = 'desconocido'  # En caso de que el contaminante no esté en los thresholds

#     return nivel_peligrosidad

# def main():
#     st.title('Nivel de peligrosidad de contaminantes atmosféricos')
#     st.write('Introduzca los siguientes valores para iniciar.')

#     sel_municipality = st.selectbox('Seleccione el municipio:', list(dicc_municipality.keys()))
#     sel_area = st.selectbox('Seleccione el tipo de área:', list(dicc_area.keys()))
#     sel_station = st.selectbox('Seleccione el tipo de estación:', list(dicc_station.keys()))
#     sel_magnitud = st.selectbox('Seleccione la magnitud:', list(dicc_magnitudes.keys()))
#     mean_value = st.number_input('Introduzca el valor recogido:', min_value=0.04, max_value=800.00, step=0.01)

# # Convertir los valores seleccionados a sus correspondientes valores numéricos
#     sel_municipality_num = dicc_municipality[sel_municipality]
#     sel_area_num = dicc_area[sel_area]
#     sel_station_num = dicc_station[sel_station]
#     sel_magnitud_num = dicc_magnitudes[sel_magnitud]

#     if st.button("Predecir"):
#         prediction_result = perform_prediction(sel_municipality_num, sel_area_num, sel_station_num, sel_magnitud_num, mean_value, model)
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


#     thresholds_peligrosidad = {
#     'SO2': {'Bajo': 25, 'Alto': 40},
#     'CO': {'Bajo': 2, 'Alto': 4},
#     'C6H6': {'Bajo': 2, 'Alto': 5},
#     'NO2': {'Bajo': 15, 'Alto': 25},
#     'PM2.5': {'Bajo': 10, 'Alto': 15},
#     'PM10': {'Bajo': 25, 'Alto': 45}, 
#     'NOX': {'Bajo': 75, 'Alto': 100},
#     'O3': {'Bajo': 75, 'Alto': 100}
# }




import streamlit as st
from pickle import load

# Carga de los diccionarios
dicc_municipality = load(open('../data/interim/factorize_values/N_MUNICIPIO_correspondencia.pkl', 'rb'))
dicc_area = load(open('../data/interim/factorize_values/TIPO_AREA_correspondencia.pkl', 'rb'))
dicc_station = load(open('../data/interim/factorize_values/TIPO_ESTACION_correspondencia.pkl', 'rb'))
dicc_magnitudes = load(open('../data/interim/factorize_values/MAGNITUD_correspondencia.pkl', 'rb'))

# Carga del modelo
model = load(open('../models/RandomForestMadrid_23.pk', 'rb'))

# Umbrales de peligrosidad definidos
umbrales_peligrosidad = {
    'SO2': {'Bajo': 25, 'Alto': 40},
    'CO': {'Bajo': 2, 'Alto': 4},
    'C6H6': {'Bajo': 2, 'Alto': 5},
    'NO2': {'Bajo': 15, 'Alto': 25},
    'PM2.5': {'Bajo': 10, 'Alto': 15},
    'PM10': {'Bajo': 25, 'Alto': 45}, 
    'NOX': {'Bajo': 75, 'Alto': 100},
    'O3': {'Bajo': 75, 'Alto': 100}
}

def perform_prediction(sel_municipality, sel_area, sel_station, sel_magnitud, mean_value, model, danger_thresholds):
    # Preparación de los datos de entrada para el modelo
    input_data = [[sel_municipality, sel_area, sel_station, sel_magnitud, mean_value]]
    prediction = model.predict(input_data)[0]

    # Obteniendo el nombre del contaminante a partir del valor seleccionado
    contaminante_nombre = list(dicc_magnitudes.keys())[list(dicc_magnitudes.values()).index(sel_magnitud)]
    thresholds = danger_thresholds.get(contaminante_nombre)

    if thresholds:
        if mean_value <= thresholds['Bajo']:
            nivel_peligrosidad = 'Bajo'
        elif mean_value <= thresholds['Alto']:
            nivel_peligrosidad = 'Normal'
        else:
            nivel_peligrosidad = 'Alto'
    else:
        nivel_peligrosidad = 'desconocido'

    return nivel_peligrosidad

def main():
    st.title('Nivel de peligrosidad de contaminantes atmosféricos')

    # Selección de parámetros por el usuario
    sel_municipality = st.selectbox('Seleccione el municipio:', list(dicc_municipality.keys()))
    sel_area = st.selectbox('Seleccione el tipo de área:', list(dicc_area.keys()))
    sel_station = st.selectbox('Seleccione el tipo de estación:', list(dicc_station.keys()))
    sel_magnitud = st.selectbox('Seleccione la magnitud:', list(dicc_magnitudes.keys()))
    mean_value = st.number_input('Introduzca el valor recogido:', min_value=0.04, max_value=800.00, value=0.04, step=0.01)

    # Conversión de las selecciones a valores numéricos
    sel_municipality_num = dicc_municipality[sel_municipality]
    sel_area_num = dicc_area[sel_area]
    sel_station_num = dicc_station[sel_station]
    sel_magnitud_num = dicc_magnitudes[sel_magnitud]

    if st.button("Predecir"):
        prediction_result = perform_prediction(sel_municipality_num, sel_area_num, sel_station_num, sel_magnitud_num, mean_value, model, umbrales_peligrosidad)
        st.success(f"Nivel de peligrosidad: {prediction_result}")

    user_input = {
        "Municipio": sel_municipality,
        "Tipo de área": sel_area,
        "Tipo de estación": sel_station,
        "Magnitud": sel_magnitud,
        "Media diaria": mean_value
    }

    st.write("Entrada del usuario:", user_input)

if __name__ == "__main__":
    main()
