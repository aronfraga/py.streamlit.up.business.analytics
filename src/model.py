import streamlit as st
import pandas as pd
import joblib
from src.config import resolve_path
from src.constants import MODEL_FILENAME

@st.cache_resource(show_spinner="Inicializando modelo predictivo de Machine Learning...")
def load_ml_model():
    package = joblib.load(resolve_path(MODEL_FILENAME))
    return package["pipeline"], package["metadata"]

def predict_loss_probability(model, operacion: dict) -> float:
    input_df = pd.DataFrame([operacion])
    return float(model.predict_proba(input_df)[0][1])
