from setuptools import setup, find_packages

setup(
    name="furo_nanodjango",
    version="1.0.0",
    description="Nanodjango-themed Furo Sphinx theme",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'furo_nanodjango = furo_nanodjango:get_html_theme_path',
        ]
    },
    install_requires=[
        'furo',
    ],
    package_data={
        'furo_nanodjango': [
            'theme.toml',
            '*.html',
            'static/*',
            'static/**/*',
        ],
    },
)