import os
import sys

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

master_doc = 'index'
project = u'WebBSC documentation'

language = 'en'

