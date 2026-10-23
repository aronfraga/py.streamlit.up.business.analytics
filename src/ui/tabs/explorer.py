import streamlit as st
import pandas as pd
from src.constants import EXPLORER_COLUMNS, EXPORT_FILENAME

def render(df_filtered: pd.DataFrame) -> None:
    st.subheader("Explorador de Transacciones Filtradas")
    cols_show = [c for c in EXPLORER_COLUMNS if c in df_filtered.columns]
    st.dataframe(df_filtered[cols_show], width="stretch", hide_index=True)

    csv_data = df_filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar datos filtrados en CSV",
        data=csv_data,
        file_name=EXPORT_FILENAME,
        mime="text/csv"
    )
