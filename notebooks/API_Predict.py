import streamlit as st 
from pickle import load


dicc_municipality = load(open('../data/interim/diccionarios/N_MUNICIPIO_correspondencia.pkl', 'rb'))
dicc_magnitudes = load(open('../data/interim/diccionarios/MAGNITUD_correspondencia.pkl', 'rb'))
dicc_area = load(open('../data/interim/diccionarios/TIPO_AREA_correspondencia.pkl', 'rb'))
dicc_station = load(open('../data/interim/diccionarios/TIPO_ESTACION_correspondencia.pkl', 'rb'))
dicc_peligrosidad = load(open('../data/interim/diccionarios/PELIGROSIDAD_correspondencia.pkl', 'rb'))


# Title
st.title('Nivel de Peligrosidad de Contaminantes Atmosféricos')

# Introductory message
st.write('### Introduzca los siguientes valores para iniciar:')

#Users data

sel_municip = st.selectbox('Seleccione el municipio:', options= list(dicc_municipality.keys()))

sel_area = st.selectbox('Seleccione el tipo de área:', options= list(dicc_area.keys()))

sel_station = st.selectbox('Seleccione el tipo de estación:', options= list(dicc_station.keys()))

sel_magnitud = st.selectbox('Seleccione el contaminante:', options= list(dicc_magnitudes.keys()))

mean_value = st.number_input('Introduzca el valor recogido (µg/m3):',
                    min_value = 0.04,
                    max_value = 800.00,
                    step = 0.01
                    )


# Button to predict
row = [mean_value,
    dicc_municipality[sel_municip],
    dicc_magnitudes[sel_magnitud],
    dicc_area[sel_area],
    dicc_station[sel_station]
    ]   

if st.button('Predict:'):
    model = load(open('../models/RandomForestMadrid_23.pk', 'rb'))

    y_pred = model.predict([row])
    y_result = round(y_pred[0], 2)


    if y_pred == 0:
        result = "😎 BAJO 😎"
    elif y_pred == 1:
        result = "⛅ NORMAL ⛅"
    elif y_pred == 2:
        result = "⚠️ ALTO ⚠️"

    st.text('Peligrosidad:' + result)



