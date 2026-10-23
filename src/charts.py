import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.constants import (
    BRAND_COLORS,
    CHART_FONT,
    DANGER_COLOR,
    GRID_COLOR,
    MUTED_TEXT_COLOR,
    PRIMARY_COLOR,
    RISK_HIGH_COLOR,
    RISK_HIGH_THRESHOLD,
    RISK_LOW_COLOR,
    RISK_LOW_THRESHOLD,
    RISK_MEDIUM_COLOR,
    TEXT_COLOR,
    TICK_COLOR,
    TRANSPARENT,
)

def build_risk_gauge(prob_perdida: float) -> go.Figure:
    low = RISK_LOW_THRESHOLD * 100
    high = RISK_HIGH_THRESHOLD * 100
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob_perdida * 100,
        title={'text': "Probabilidad de Perdida Neta", 'font': {'size': 14, 'color': MUTED_TEXT_COLOR}},
        number={'suffix': "%", 'valueformat': ".1f", 'font': {'size': 40, 'color': PRIMARY_COLOR}},
        gauge={
            'axis': {'range': [0, 100], 'tickcolor': TICK_COLOR, 'tickfont': {'color': MUTED_TEXT_COLOR}},
            'bar': {'color': PRIMARY_COLOR, 'thickness': 0.3},
            'borderwidth': 0,
            'steps': [
                {'range': [0, low], 'color': RISK_LOW_COLOR},
                {'range': [low, high], 'color': RISK_MEDIUM_COLOR},
                {'range': [high, 100], 'color': RISK_HIGH_COLOR}
            ],
            'threshold': {
                'line': {'color': DANGER_COLOR, 'width': 3},
                'thickness': 0.75,
                'value': high
            }
        }
    ))
    fig_gauge.update_layout(
        height=260,
        margin=dict(l=20, r=20, t=40, b=10),
        paper_bgcolor=TRANSPARENT,
        font=CHART_FONT
    )
    return fig_gauge

def build_discount_scatter(df: pd.DataFrame) -> go.Figure:
    fig_scat = px.scatter(
        df,
        x="descuento",
        y="ganancia",
        color="categoria" if "categoria" in df.columns else None,
        size="venta" if "venta" in df.columns else None,
        hover_data=["subcategoria", "region"] if "subcategoria" in df.columns else None,
        title="Ganancia Neta vs. Descuento Aplicado en Transacciones Activas",
        color_discrete_sequence=BRAND_COLORS,
        opacity=0.7
    )
    fig_scat.add_hline(y=0, line_dash="dash", line_color=DANGER_COLOR, line_width=1.5)
    fig_scat.update_layout(
        template="plotly_white",
        height=520,
        font=CHART_FONT,
        title_font=dict(size=15, color=TEXT_COLOR),
        paper_bgcolor=TRANSPARENT,
        plot_bgcolor=TRANSPARENT,
        margin=dict(l=10, r=10, t=70, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, title_text="")
    )
    fig_scat.update_xaxes(tickformat=".0%", gridcolor=GRID_COLOR, zeroline=False, title_text="Descuento")
    fig_scat.update_yaxes(gridcolor=GRID_COLOR, zeroline=False, tickprefix="$", title_text="Ganancia")
    return fig_scat
