import streamlit as st
import pandas as pd

from src.constants import DATA_FILENAME, UPLOAD_FILE_TYPES
from src.data import load_base_data, parse_uploaded_file

def _load_active_data() -> pd.DataFrame:
    uploaded_file = st.file_uploader(
        "Actualizar datos (.parquet, .xlsx, .csv):",
        type=UPLOAD_FILE_TYPES,
        help="Sube un archivo para analizarlo en la sesion actual sin modificar el repositorio central."
    )

    origen_texto = ""
    if uploaded_file is not None:
        try:
            df_raw = parse_uploaded_file(uploaded_file)
            origen_texto = f"Cargado en sesion: {uploaded_file.name}"
            st.success("Dataset cargado correctamente en memoria.")
        except Exception as e:
            st.error(f"Error al leer archivo: {e}")
            df_raw = load_base_data()
            origen_texto = f"{DATA_FILENAME} (Base)"
    else:
        df_raw = load_base_data()
        origen_texto = f"{DATA_FILENAME} (Base de produccion)"

    st.markdown(f'<div class="badge-data">Fuente: {origen_texto}</div>', unsafe_allow_html=True)
    st.caption(f"Registros activos: {len(df_raw):,} | Columnas: {df_raw.shape[1]}")
    return df_raw

def _multiselect_filter(df: pd.DataFrame, column: str, label: str):
    if column not in df.columns:
        return None
    available = sorted(df[column].dropna().unique())
    return st.multiselect(label, available, default=available)

def render_sidebar(metadata: dict) -> tuple[pd.DataFrame, dict]:
    with st.sidebar:
        st.markdown("### Centro de control de datos")
        df_raw = _load_active_data()

        st.divider()
        st.markdown("### Filtros analiticos")
        filtros = {
            "anios": _multiselect_filter(df_raw, "anio", "Anio fiscal:"),
            "regiones": _multiselect_filter(df_raw, "region", "Region:"),
            "categorias": _multiselect_filter(df_raw, "categoria", "Categoria:"),
        }

        st.divider()
        st.markdown("### Modelo predictivo en produccion")
        st.write(f"**ROC-AUC Score:** `{metadata['roc_auc']}`")
        st.write(f"**Target:** {metadata['target']}")
        st.caption("Pipeline de Random Forest con ColumnTransformer en memoria RAM.")

    return df_raw, filtros
