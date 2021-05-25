# Configuration file for the Sphinx_pyaedt documentation builder.
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
import sys
import os
import shutil
import pathlib
import glob
from distutils.dir_util import copy_tree

local_path = os.path.dirname(os.path.realpath(__file__))
module_path = pathlib.Path(local_path)
root_path = module_path.parent.parent
sys.path.append(os.path.abspath(os.path.join(local_path)))
sys.path.append(os.path.join(root_path))

sys.path.append(os.path.join(root_path, "pyaedt"))
project = 'pyaedt'
copyright = 'Copyright(c) 1986-2021, ANSYSInc. unauthorised use, distribution or duplication is prohibited. This tool release is unofficial and not covered by standard Ansys Support license.'
author = 'Ansys Inc.'
documentation_dir = os.path.join(root_path, "pyaedt", "Documentation")
if not os.path.exists(documentation_dir):
    os.mkdir(documentation_dir)
with open(os.path.join(root_path,"pyaedt", "version.txt"), "r") as f:
    version = f.readline()
# The full version, including alpha/beta/rc tags
release = version

# Not needed since examples moved into pyaedt Folder
# example_dir = os.path.join(documentation_dir,"examples")
# if not os.path.exists(example_dir):
#     os.mkdir(example_dir)
# model_dir = os.path.join(example_dir, "Examples_Files")
# if not os.path.exists(model_dir):
#     os.mkdir(model_dir)
# copy_tree(os.path.join(root_path,"examples", "pyaedt", "Examples_Files"), model_dir)
# python_files = glob.glob(os.path.join(root_path,"examples","pyaedt") + "/0*.py")
# python_files += glob.glob(os.path.join(root_path,"examples","pyaedt") + "/1*.py")
# for f in python_files:
#     shutil.copy2(f, example_dir)
#
# jupyter_files = glob.glob(os.path.join(root_path, "examples","pyaedt","Notebooks") + "/*.ipynb")
# for f in jupyter_files:
#     shutil.copy2(f, example_dir)

# -- General configuration ---------------------------------------------------

# Add any Sphinx_pyaedt extension module names here, as strings. They can be
# extensions coming with Sphinx_pyaedt (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              "sphinx.ext.viewcode",
              "sphinx.ext.autosummary",
              "nbsphinx",
              "sphinx.ext.intersphinx",
              'sphinx.ext.napoleon',
              'sphinx.ext.coverage',
              "sphinx_copybutton",
              'recommonmark',
              'sphinx.ext.graphviz',
              'nbsphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.inheritance_diagram']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx_pyaedt. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'Python'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', "sphinx_boogergreen_theme_1", 'Thumbs.db', '.DS_Store', '*.txt']

inheritance_graph_attrs = dict(rankdir="RL", size='"8.0, 10.0"',
                               fontsize=14, ratio='compress')
inheritance_node_attrs = dict(shape='ellipse', fontsize=14, height=0.75,
                              color='dodgerblue1', style='filled')


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}



# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'





# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
#html_theme = 'bootstrap-astropy'

# html_theme = 'sphinx_adc_theme'
# import sphinx_adc_theme
# html_theme_path = [sphinx_adc_theme.get_html_theme_path()]

# The name of the Pygments (syntax highlighting) style to use.


# Options for HTML output
# -----------------------

# html_theme = "furo"
#
# html_theme_options = {
#         }
#
# html_sidebars = {
#         }


#html_theme = "sphinx_boogergreen_theme"
html_show_sourcelink = True

html_theme = 'pydata_sphinx_theme'
html_logo = "./Resources/logo-ansys.png"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']
html_css_files = ['css/ansys.css']

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyaedtdoc'