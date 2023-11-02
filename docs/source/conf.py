# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import time

project = 'Документи'
copyright = f'{time.strftime("%Y")}, Природниче Відділення'
author = 'ЦК "Комп\'ютерні науки"'

# The full version, including alpha/beta/rc tags
version = '1'
release = '0'
master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 
              'myst_parser', "sphinx_design", "sphinx.ext.autodoc"
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme' # 'sphinx_rtd_theme'
html_title = ""
html_theme_options = {
    "home_page_in_toc": True,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

latex_elements = {
    'papersize': 'a4paper',
    'preamble': r'''
\usepackage[utf8]{inputenc}	
''',
    'babel': r'''
    \usepackage[ukrainian]{babel}
    ''',
}
latex_show_urls = 'footnote'


# -- MyST settings ---------------------------------------------------

myst_enable_extensions = ["deflist", "colon_fence"]
