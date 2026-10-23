import streamlit as st
import pandas as pd

from src.charts import build_risk_gauge
from src.constants import RISK_HIGH_THRESHOLD, RISK_LOW_THRESHOLD
from src.model import predict_loss_probability

def _render_inputs(df_raw: pd.DataFrame, metadata: dict) -> dict:
    with st.container(border=True):
        st.markdown("##### 1. Parametros de la operacion")
        c_cat, c_sub = st.columns(2, gap="medium")
        with c_cat:
            cat_choice = st.selectbox("Categoria:", metadata["categories"]["categoria"])
        with c_sub:
            if "categoria" in df_raw.columns and "subcategoria" in df_raw.columns:
                subcats_avail = df_raw[df_raw["categoria"] == cat_choice]["subcategoria"].unique().tolist()
            else:
                subcats_avail = metadata["categories"]["subcategoria"]
            subcat_choice = st.selectbox("Subcategoria:", sorted(subcats_avail))

        c_reg, c_seg = st.columns(2, gap="medium")
        with c_reg:
            reg_choice = st.selectbox("Region:", metadata["categories"]["region"])
        with c_seg:
            seg_choice = st.selectbox("Segmento:", metadata["categories"]["segmento"])

        c_env1, c_env2 = st.columns(2, gap="medium")
        with c_env1:
            env_choice = st.selectbox("Forma de envio:", metadata["categories"]["forma_envio"])
        with c_env2:
            dias_env_choice = st.slider("Dias de envio estimados:", 0, 10, 4)

    st.write("")

    with st.container(border=True):
        st.markdown("##### 2. Variables comerciales")
        c_vta, c_cant = st.columns(2, gap="medium")
        with c_vta:
            venta_choice = st.number_input("Facturacion estimada ($):", min_value=10.0, max_value=50000.0, value=3500.0, step=100.0)
        with c_cant:
            cant_choice = st.number_input("Cantidad de unidades:", min_value=1, max_value=100, value=5, step=1)

        desc_choice = st.slider(
            "Tasa de descuento ofrecida (%):",
            min_value=0, max_value=80, value=15, step=1,
            help="Prueba superar el 20% para ver la sensibilidad de riesgo proyectada."
        ) / 100.0

    return {
        "categoria": cat_choice,
        "subcategoria": subcat_choice,
        "region": reg_choice,
        "segmento": seg_choice,
        "forma_envio": env_choice,
        "venta": float(venta_choice),
        "cantidad": int(cant_choice),
        "descuento": float(desc_choice),
        "dias_envio": int(dias_env_choice)
    }

def _render_verdict(prob_perdida: float) -> None:
    st.markdown("##### 3. Dictamen del modelo de riesgo")
    st.plotly_chart(build_risk_gauge(prob_perdida), use_container_width=True)

    if prob_perdida < RISK_LOW_THRESHOLD:
        st.success("**Operacion recomendada:** Riesgo bajo. La transaccion preserva un margen saludable.")
    elif prob_perdida < RISK_HIGH_THRESHOLD:
        st.warning("**Requiere aprobacion gerencial:** Riesgo moderado. El descuento roza el limite de rentabilidad.")
    else:
        st.error("**Operacion no recomendada:** Riesgo critico de perdida neta. Ajustar descuento hacia abajo.")

def render(df_raw: pd.DataFrame, model, metadata: dict) -> None:
    st.subheader("Simulador de Cotizaciones y Politicas de Descuento")
    st.markdown("Evalua en tiempo real si una cotizacion comercial generara margen positivo o destruccion neta de capital antes de emitir la orden.")

    col_sim_in, col_sim_out = st.columns([7, 5], gap="large")

    with col_sim_in:
        operacion = _render_inputs(df_raw, metadata)

    prob_perdida = predict_loss_probability(model, operacion)

    with col_sim_out, st.container(border=True):
        _render_verdict(prob_perdida)
