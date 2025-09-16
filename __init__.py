from pathlib import Path

__version__ = "1.0.0"

def get_html_theme_path():
    return str(Path(__file__).parent)