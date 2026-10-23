import pandas as pd

def format_thousands(value) -> str:
    return f"{value:,.0f}".replace(",", ".")

def compute_kpis(df: pd.DataFrame) -> dict:
    ventas_tot = df["venta"].sum() if "venta" in df.columns else 0.0
    ganancia_tot = df["ganancia"].sum() if "ganancia" in df.columns else 0.0
    margen_pct = (ganancia_tot / ventas_tot * 100) if ventas_tot > 0 else 0.0
    pedidos_tot = df["id_pedido"].nunique() if "id_pedido" in df.columns else len(df)
    ticket_prom = ventas_tot / pedidos_tot if pedidos_tot > 0 else 0.0
    filas_perdida = (df["ganancia"] < 0).sum() if "ganancia" in df.columns else 0
    pct_perdida = (filas_perdida / len(df) * 100) if len(df) > 0 else 0.0

    return {
        "ventas_tot": ventas_tot,
        "ganancia_tot": ganancia_tot,
        "margen_pct": margen_pct,
        "pedidos_tot": pedidos_tot,
        "ticket_prom": ticket_prom,
        "filas_perdida": filas_perdida,
        "pct_perdida": pct_perdida,
    }
