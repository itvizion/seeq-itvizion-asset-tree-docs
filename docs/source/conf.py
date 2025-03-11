# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Tell Sphinx to find modules inside your project directory
import os
import sys
sys.path.insert(0, os.path.abspath("/Users/tpomavil/repos/ITVizion/seeq-itvizion-asset-tree/src"))  # Adjust this path if needed

# Monkey patch versioneer to avoid Sphinx import issues
import versioneer
def get_version_stub():
    return "unknown"
versioneer.get_version = get_version_stub

project = 'seeq-itv-asset-tree'
copyright = '2025, Tim Pomaville'
author = 'Tim Pomaville'
release = 'v1.3.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Enables Google-style docstrings
    "sphinx.ext.viewcode",  # Adds links to source code
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
