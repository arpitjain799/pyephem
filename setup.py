try:
    from setuptools import setup, Extension
except:
    from distutils.core import setup, Extension

import os
from glob import glob

# Read the current version from ephem/__init__.py itself.

path = os.path.join(os.path.dirname(__file__), 'src', 'ephem', '__init__.py')
for line in open(path):
    if line.startswith('__version__'):
        __version__ = eval(line.split(None, 2)[2]) # skip '__version__', '='

# The `pyephem' module is built from every .c file in the libastro
# directory plus ...

libastro_version = '3.7.3'
libastro_files = glob('libastro-%s/*.c' % libastro_version)
libastro_data = glob('extensions/data/*.c')

def read(*filenames):
    return open(os.path.join(os.path.dirname(__file__), *filenames)).read()

setup(name = 'pyephem',
      version = __version__,
      description = 'Scientific-grade astronomy routines',
      long_description = read('README'),
      license = 'LGPL',
      author = 'Brandon Craig Rhodes',
      author_email = 'brandon@rhodesmill.org',
      url = 'http://rhodesmill.org/pyephem/',
      classifiers = [
        'Development Status :: 6 - Mature',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved ::'
        ' GNU Library or Lesser General Public License (LGPL)',
        'Topic :: Scientific/Engineering :: Astronomy',
        ],
      packages = [ 'ephem', 'ephem.tests' ],
      package_dir = { '': 'src' },
      package_data = { 'ephem': ['doc/*.rst', 'tests/usno/*.txt'],},
      test_suite = 'ephem.tests',
      ext_modules = [
    Extension('ephem._libastro',
              ['extensions/_libastro.c'] + libastro_files + libastro_data,
              include_dirs=['libastro-' + libastro_version],
              )],
      )
