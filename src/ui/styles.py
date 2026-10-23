from pathlib import Path
import streamlit as st

def load_css(css_path: Path) -> None:
    css = css_path.read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
