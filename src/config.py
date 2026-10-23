from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CSS_PATH = ROOT_DIR / "assets" / "styles.css"

def resolve_path(filename: str) -> Path:
    path = ROOT_DIR / filename
    if not path.exists():
        path = Path(filename)
    return path
