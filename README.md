**Hazardous level of atmospheric pollutants🌍🔍**.
---
## *Project Description*

This project aims to predict the hazard level of various atmospheric pollutants as a function of different variables, such as the type of area in which it is located and the surrounding environmental factors. Hazard level prediction is essential to understand and mitigate potential risks associated with exposure to pollutants at different locations.


## *Main objective:*

This project is important because it allows predicting and understanding air pollution levels to:

- Protect public health.
- Facilitate sustainable urban planning.
- Improve people's quality of life.
- Promote environmental awareness.
- Contribute to scientific research in air quality.

## *Description of the Data* 📈

Data are from the official website of the Government of Spain, Ministry for Ecological Transition and Demographic Challenge.

Data collected from the documentation of the page were introduced to obtain some data to help us develop the purpose of our project.

Source: 

https://www.miteco.gob.es/es/calidad-y-evaluacion-ambiental/temas/atmosfera-y-calidad-del-aire/calidad-del-aire/evaluacion-datos/datos/datos-oficiales-2022.html


## *Principal Characteristics*

- FECHA. Date recorded at the time the pollutant values were taken (numeric).
- N_CCAA. Name of each autonomous community in Spain where measurement data were collected for each pollutant (categorical).
- PROVINCIA. Name of each province in which measurement data for each pollutant were collected (categorical).
- N_MUNICIPIO. Name of each municipality in which measurement data were collected for each pollutant (categorical).
- ESTACION. Number assigned to each station in each autonomous community that has recorded pollutant measurement data (numeric).
- MAGNITUD. Each pollutant that has been registered in the different stations (categorical).
- TIPO_AREA.Type of area in which they are located, urban, suburban or rural area (categorical).
- TIPO_ESTACION. According to the typology of the main emission source, traffic, industrial or background (categorical).
- LATITUD, LONGITUD. Geographical data of each station where pollutants have been recorded (numeric).
- H01, H02, H03.... H24. Hourly recorded value for each pollutant. All pollutants are taken with unified measurement units (µg/m3) (numeric).

## *Pollutants* 🏭💨🚗

> All concentration data are expressed in micrograms per cubic meter (μg/m³).

| Pollutant                            | Full Name            |
|---------------------------------------|-----------------------------------|
| С6Н6 (Benzene)                        | Benzene                           |
| CO (Carbon Monoxide)                  | Carbon Monoxide                   |
| NO2 (Nitrogen Dioxide)                | Nitrogen Dioxide                  |
| NOX (Nitrogen Oxides)                 | Nitrogen Oxides                   |
| O3 (Ozone)                            | Ozone                             |
| PM10 (Particulate Matter 10 μm)       | Particulate Matter (PM10)         |
| PM2.5 (Particulate Matter 2.5 μm)     | Particulate Matter (PM2.5)        |
| SO2 (Sulfur Dioxide)                  | Sulfur Dioxide                    |


## *File structure*

- Exploratory Data Analysis (EDA)
- Data visualization through graphs and tables.
- Feature engineering: New features have been created from existing features to improve model performance.
- Feature selection: Deciding which features to include in the final model based on their importance and relevance.
- Creation and training of a machine learning model to predict the hazard level of each pollutant.

## *Technologies Used*

- Python 🐍
- Pandas 🐼
- Numpy 🧮
- Matplotlib/Seaborn 📊
- Pickle 🥒
- Scikit-learn 🤖 (for the machine learning model)
- Streamlit 🌐 (for developing the interactive web application)

## *Project structure*

- `data/`: Folder containing the used, processed and temporary datasets.
- `models/`: Folder containing the machine learning models.
- notebooks/`: Folder containing the notebooks used for the Exploratory Data Analysis (EDA) and the construction of the Random Forest model.
- `src/`: Folder containing the code to deploy the model using streamlit.
- `README.md`: Project documentation (this file). 📚

## *Execution Instructions*

1. Clone this repository:

   ````bash
   git clone https://github.com/Yakondra/Final-project-air-quality.git
   o
   git clone https://github.com/Pilizmt/Final-project-air-quality.git

2. Install the dependencies:

    ````bash
    pip install -r requirements.t

## *Render*

- To create the website we have used: https://render.com/

- Link to the interactive website: https://air-quality-predict.onrender.com/

## *How to Contribute*

Contributions are welcome! If you encounter problems, have ideas for improvements or want to add new features, feel free to send a pull request. 🤝🚀


