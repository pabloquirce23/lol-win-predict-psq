import streamlit as st
import pandas as pd
import joblib

clf = joblib.load("model/league_win_prediction_model.pkl")

st.title("CALCULADORA PORCENTAJE DE VICTORIA LOL")

gold_difference = st.number_input("Diferencia de Oro:")
experience_difference = st.number_input("Diferencia de Experiencia:")
kills_difference = st.number_input("Diferencia de Kills:")
avg_lvl_difference = st.number_input("Diferencia de Media de Niveles:")

if st.button("Submit"):
    X = pd.DataFrame([[gold_difference, experience_difference, kills_difference, 
                       avg_lvl_difference]],
                     columns=["blueGoldDiff", "blueExperienceDiff", "blueKillsDiff",
                              "blueAvgLvlDiff"])
    prediction = clf.predict(X)[0]

    if prediction > 1:
        prediction = 1
    elif prediction < 0:
        prediction = 0
    else:
        prediction = prediction

    st.text(f"Tu equipo tiene un {prediction * 100}% de conseguir la victoria")