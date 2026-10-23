import streamlit as st
import pandas as pd

from src.charts import build_discount_scatter

def render(df_filtered: pd.DataFrame) -> None:
    st.subheader("Auditoria Historica de Rentabilidad y Descuentos")
    if "descuento" in df_filtered.columns and "ganancia" in df_filtered.columns:
        st.plotly_chart(build_discount_scatter(df_filtered), use_container_width=True)
    else:
        st.info("El dataset activo no contiene las columnas requeridas ('descuento', 'ganancia').")
