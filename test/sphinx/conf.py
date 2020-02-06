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

project = 'sphinx-doxygen-docker'
copyright = '2020, MusicScience37 (Kenta Kabashima)'
author = 'Kenta Kabashima'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# -- Options for Latex output ------------------------------------------------

latex_documents = [(
    # start doc name
    'index',
    # target name
    'sphinx-doxygen-docker.tex',
    # title
    'Sphinx-Doxygen Docker Image',
    # author
    'Kenta Kabashima',
    # document class
    'manual',
    # toc tree only
    False,
)]

latex_elements = {
    'fontpkg' : r'''
    \usepackage{lmodern}
    ''',
}

# ---Extensions --------------------------------------------------------------

extensions += ['sphinx.ext.mathjax']
mathjax_config = {
    'TeX' : {
        'Macros': {
            'bm': ['{\\boldsymbol{#1}}',1],
        },
    },
}

extensions += ['sphinxcontrib.plantuml']
plantuml_output_format = 'svg'
plantuml_latex_output_format = 'pdf'
plantuml_syntax_error_image = True

extensions += ['breathe']
breathe_projects = { 'TestBreathe': '' }
breathe_default_project = 'TestBreathe'
breathe_default_members = ('members','private-members')
breathe_domain_by_extension = {
    "h" : "cpp",
}
