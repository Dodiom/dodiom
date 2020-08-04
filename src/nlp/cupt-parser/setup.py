# -*- coding: utf-8 -*-
import os

from setuptools import setup

VERSION = '0.1.1'

setup(
    name='parseme-cupt',
    # packages=["parseme.cupt"],
    py_modules=["parseme.cupt"],
    version=VERSION,
    description='A Python parser for the CUPT format (http://multiword.sourceforge.net/cupt-format)',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    author=u'Jakub Waszczuk',
    author_email='waszczuk.kuba@gmail.com',
    url='https://github.com/kawu/parseme-cupt',
    install_requires=['conllu>=2.2.2'],
    keywords=['parseme', 'cupt', 'nlp'],
)
