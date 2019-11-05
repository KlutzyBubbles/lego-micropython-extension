import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../pybricks_ext'))

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages'
]

autodoc_member_order = 'bysource'

numfig = True

templates_path = ['_templates']

source_suffix = ['.rst']

master_doc = 'index'

project = u'Lego Micropython'

version = os.environ['VERSION']
release = os.environ['PACKAGE_VERSION']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

add_function_parentheses = True

add_module_names = True

pygments_style = 'sphinx'

todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'display_version': False
}

html_title = u'Lego Micropython Extension Docs'

html_logo = 'images/lego-education-logo-small.png'

html_show_sphinx = False

html_show_copyright = False

htmlhelp_basename = 'testdoc'
