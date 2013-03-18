# -*- coding: utf-8 -*-
#
# MPC-HC documentation build configuration file, created by
# sphinx-quickstart on Sat Mar 17 17:15:28 2012.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
sys.path.append(os.path.abspath('../ext'))
extensions = ['sphinx.ext.ifconfig', 'traclinks', 'feed']

traclinks_base_url = 'https://trac.mpc-hc.org'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'MPC-HC'
copyright = u'MPC-HC Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.6.6'
# The full version, including alpha/beta/rc tags.
release = '1.6.6.6957'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'ext']

# The reST default role (used for this markup: `text`) to use for all documents
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Trim spaces before footnote references that are necessary for the reST
# parser to recognize the footnote, but do not look too nice in the output.
trim_footnote_reference_space = True


# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = 'MPC-HC project'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = 'logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d %Y, %H:%M:%S'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Sphinx will add "permalinks" for each heading and description environment
# as paragraph signs that become visible when the mouse hovers over them.
html_add_permalinks = None

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/name.
# The default is True.
#
# Warning
# If this config value is set to False, the JavaScript search function will
# only display the titles of matching documents, and no excerpt from the
# matching contents.
html_copy_source = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = '.html'

# Suffix for generated links to HTML files.
# The default is whatever html_file_suffix is set to;
# it can be set differently (e.g. to support different web server setups).
#html_link_suffix = '.html'

# A string with the fully-qualified name of a HTML Translator class,
# that is, a subclass of Sphinx’ HTMLTranslator, that is used to translate
# document trees to HTML. Default is None (use the builtin translator).
#html_translator_class

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'mpchcdoc'


# Feed configuration
base_uri = "http://mpc-hc.org"
feed_title = "Media Player Classic - Home Cinema"
feed_description = "Latest information about the project."
feed_link = '%s/rss.xml' % (base_uri,)
feed_maxitems = 10
feed_ignorepagenames = ['index_*', 'search', 'about', 'archive', 'changelog',
                        'contact-us', 'donate', 'downloads', 'faq',
                        'latest_posts', 'sitemap']
