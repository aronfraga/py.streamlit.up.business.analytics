import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config import CSS_PATH
from src.constants import PAGE_TITLE, TAB_LABELS

st.set_page_config(
    page_title=PAGE_TITLE,
    layout="wide",
    initial_sidebar_state="expanded"
)

from src.data import apply_filters
from src.metrics import compute_kpis
from src.model import load_ml_model
from src.ui.layout import render_footer, render_hero, render_kpis
from src.ui.sidebar import render_sidebar
from src.ui.styles import load_css
from src.ui.tabs import dashboard, explorer, model_card, simulator

load_css(CSS_PATH)

model, metadata = load_ml_model()

df_raw, filtros = render_sidebar(metadata)
df_filtered = apply_filters(df_raw, **filtros)

render_hero(len(df_filtered), metadata["roc_auc"])

if df_filtered.empty:
    st.warning("No hay registros que coincidan con los filtros seleccionados.")
    st.stop()

render_kpis(compute_kpis(df_filtered))

tab_sim, tab_dash, tab_data, tab_model = st.tabs(TAB_LABELS)

with tab_sim:
    simulator.render(df_raw, model, metadata)

with tab_dash:
    dashboard.render(df_filtered)

with tab_data:
    explorer.render(df_filtered)

with tab_model:
    model_card.render(metadata)

render_footer()
