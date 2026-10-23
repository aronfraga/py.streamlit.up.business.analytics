# Aplicacion
PAGE_TITLE = "Supertienda Analytics Hub"
FOOTER_TEXT = "Universidad de Palermo • Business Intelligence & Analytics • Clase 11: Cloud Deploy • Ing. Matias A. Perez"

TAB_LABELS = [
    "Simulador What-If",
    "Tablero de Rentabilidad",
    "Explorador y Descarga",
    "Ficha Tecnica del Modelo"
]

DATA_FILENAME = "supertienda_curated.parquet"
MODEL_FILENAME = "model_superstore.joblib"
EXPORT_FILENAME = "supertienda_reporte_filtrado.csv"
UPLOAD_FILE_TYPES = ["parquet", "xlsx", "csv"]

DATE_COLUMN = "fecha_pedido"
EXPLORER_COLUMNS = ["id_pedido", "fecha_pedido", "nombre_cliente", "region", "categoria", "subcategoria", "venta", "ganancia", "descuento"]

# Umbrales de riesgo (probabilidad de perdida)
RISK_LOW_THRESHOLD = 0.30
RISK_HIGH_THRESHOLD = 0.60

PRIMARY_COLOR = "#0A3073"
DANGER_COLOR = "#DC2626"
TEXT_COLOR = "#1E2433"
MUTED_TEXT_COLOR = "#64748B"
TICK_COLOR = "#94A3B8"
GRID_COLOR = "#EEF2F7"
RISK_LOW_COLOR = "#D1FAE5"
RISK_MEDIUM_COLOR = "#FEF3C7"
RISK_HIGH_COLOR = "#FEE2E2"
TRANSPARENT = "rgba(0,0,0,0)"

BRAND_COLORS = [PRIMARY_COLOR, "#2563EB", "#14B8A6", "#F59E0B", "#8B5CF6"]
CHART_FONT = dict(family="Inter, sans-serif", color=TEXT_COLOR)
