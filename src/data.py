import streamlit as st
import pandas as pd

from src.config import resolve_path
from src.constants import DATA_FILENAME, DATE_COLUMN

def _parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    if DATE_COLUMN in df.columns:
        df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])
    return df

@st.cache_data(show_spinner="Cargando dataset base...")
def load_base_data() -> pd.DataFrame:
    df = pd.read_parquet(resolve_path(DATA_FILENAME))
    return _parse_dates(df)

def parse_uploaded_file(uploaded_file) -> pd.DataFrame:
    nombre = uploaded_file.name.lower()
    if nombre.endswith(".parquet"):
        df = pd.read_parquet(uploaded_file)
    elif nombre.endswith(".xlsx") or nombre.endswith(".xls"):
        df = pd.read_excel(uploaded_file)
    elif nombre.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        raise ValueError("Formato no soportado. Suba archivos .parquet, .xlsx o .csv")
    return _parse_dates(df)

def apply_filters(df: pd.DataFrame, anios=None, regiones=None, categorias=None) -> pd.DataFrame:
    df_filtered = df.copy()
    if anios and "anio" in df_filtered.columns:
        df_filtered = df_filtered[df_filtered["anio"].isin(anios)]
    if regiones and "region" in df_filtered.columns:
        df_filtered = df_filtered[df_filtered["region"].isin(regiones)]
    if categorias and "categoria" in df_filtered.columns:
        df_filtered = df_filtered[df_filtered["categoria"].isin(categorias)]
    return df_filtered
