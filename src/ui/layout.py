import streamlit as st
from src.constants import FOOTER_TEXT, PAGE_TITLE
from src.metrics import format_thousands

def render_hero(n_registros: int, roc_auc) -> None:
    registros_txt = format_thousands(n_registros)
    st.markdown(f"""<div class="hero">
                    <div class="hero-title">{PAGE_TITLE}</div>
                    <div class="hero-sub">Plataforma de inteligencia de negocios y simulacion prescriptiva de decisiones comerciales.</div>
                    <span class="hero-pill">{registros_txt} registros filtrados</span>
                    <span class="hero-pill">ROC-AUC {roc_auc}</span>
                </div>
                """, unsafe_allow_html=True)

def render_kpis(kpis: dict) -> None:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Ventas Totales", f"${format_thousands(kpis['ventas_tot'])}", f"{format_thousands(kpis['pedidos_tot'])} pedidos")
    c2.metric("Ganancia Neta", f"${format_thousands(kpis['ganancia_tot'])}", f"Margen: {kpis['margen_pct']:.1f}%")
    c3.metric("Ticket Promedio", f"${format_thousands(kpis['ticket_prom'])}")
    c4.metric("Ordenes con Perdida", f"{kpis['pct_perdida']:.1f}%", f"{kpis['filas_perdida']} pedidos", delta_color="inverse")
    st.write("")


def render_footer() -> None:
    st.divider()
    st.markdown(f'<div class="app-footer">{FOOTER_TEXT}</div>', unsafe_allow_html=True)
