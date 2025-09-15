# Configuration file for the Sphinx documentation builder.

project = 'Test Nanodjango Theme'
copyright = '2024, Test'
author = 'Test'

extensions = ['furo_nanodjango']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Theme settings
html_theme = 'furo_nanodjango'

html_static_path = ['_static']

# Copy our static assets to _static
import shutil
from pathlib import Path
theme_static = Path(__file__).parent.parent / 'theme' / 'furo_nanodjango' / 'static'
doc_static = Path(__file__).parent / '_static'
doc_static.mkdir(exist_ok=True)

# Copy logo and CSS
if (theme_static / 'logo.svg').exists():
    shutil.copy2(theme_static / 'logo.svg', doc_static)
if (theme_static / 'furo_nanodjango.css').exists():
    shutil.copy2(theme_static / 'furo_nanodjango.css', doc_static)
if (theme_static / 'icons').exists():
    if (doc_static / 'icons').exists():
        shutil.rmtree(doc_static / 'icons')
    shutil.copytree(theme_static / 'icons', doc_static / 'icons')