import os
import sys

from recommonmark.parser import CommonMarkParser

templates_path = ['_templates']

source_suffix = ['.rst', '.md', '.markdown']
source_parsers = {
    '.md': CommonMarkParser,
    '.markdown': CommonMarkParser,
}

master_doc = 'index'
project = u'WebBSC documentation'

html_static_path = ['_static']

html_theme = 'default'
htmlhelp_basename = 'ReadtheDocsTemplatedoc'

language = 'en'
