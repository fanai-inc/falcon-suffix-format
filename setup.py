#!/usr/bin/env python3
"""
setup.py

Inspired by:
    https://github.com/kennethreitz/setup.py

"""
from pathlib import Path

from setuptools import find_packages, setup


# Package meta-data.
NAME = 'falcon_suffix_format'
DESCRIPTION = 'Handle routing and setting content type based on url suffix for Falcon projects'
URL = 'https://bitbucket.org/fanai-developers/falcon-suffix-format'
EMAIL = 'jc@fanai.io'
AUTHOR = 'JC Edualino'

REQUIRED = ['falcon']


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for
# that!


here = Path(__file__).parent.absolute()
assert here.exists()

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in
# file!
with open(here / 'README.rst', encoding='utf-8') as f:
    long_description = '\n' + f.read()


with open(here / 'LICENSE') as f:
    license = f.read()


# Load the package's __version__.py module as a dictionary.
about = {}
with open(here / NAME / '__version__.py') as f:
    exec(f.read(), about)


# Where the magic happens.
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests', 'docs', 'requirements')),
    install_requires=REQUIRED,
    python_requires='>=3',
    include_package_data=True,
    license=license,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
