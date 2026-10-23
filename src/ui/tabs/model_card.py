import streamlit as st

def render(metadata: dict) -> None:
    st.subheader("Ficha Tecnica de Arquitectura del Modelo")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        cat_chips = "".join(f'<span class="chip">{f}</span>' for f in metadata.get("cat_features", []))
        num_chips = "".join(f'<span class="chip">{f}</span>' for f in metadata.get("num_features", []))
        st.markdown('<div class="spec-label">Algoritmo</div>'
                    '<div>Random Forest Classifier (Pipeline de Scikit-Learn)</div>'
                    '<div class="spec-label">ROC-AUC Score</div>'
                    f'<div><span class="chip">{metadata["roc_auc"]}</span></div>'
                    '<div class="spec-label">Features categoricas</div>'
                    f'<div>{cat_chips}</div>'
                    '<div class="spec-label">Features numericas</div>'
                    f'<div>{num_chips}</div>',
                    unsafe_allow_html=True
                    )
    with col_m2:
        st.info("**Politica de Despliegue en la Nube:**\n"
                "- **Inferencia en memoria RAM:** El pipeline serializado con joblib se carga una sola vez al levantar el contenedor mediante `@st.cache_resource`.\n"
                "- **Persistencia en uploader:** Al cargar archivos interactivos, los datos residen en el buffer de sesion sin modificar el archivo base del repositorio."
                )
