# Copyright 2012-2017 CNRS-UM LIRMM, CNRS-AIST JRL
#
# This file is part of sch-core-python.
#
# sch-core-python is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# sch-core-python is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with sch-core-python.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
try:
  from setuptools import setup
  from setuptools import Extension
except ImportError:
  from distutils.core import setup
  from distutils.extension import Extension

from Cython.Build import cythonize

import hashlib
import numpy
import os
import subprocess
import sys

win32_build = os.name == 'nt'

this_path  = os.path.dirname(os.path.realpath(__file__))
with open(this_path + '/sch/__init__.py', 'w') as fd:
    fd.write('from .sch import *\n')

sha512 = hashlib.sha512()
src_files = ['sch/sch.pyx', 'sch/c_sch.pxd', 'sch/sch.pxd', 'include/sch_wrapper.hpp']
src_files = [ '{}/{}'.format(this_path, f) for f in src_files ]
for f in src_files:
  chunk = 2**16
  with open(f, 'r') as fd:
    while True:
      data = fd.read(chunk)
      if data:
        sha512.update(data.encode('ascii'))
      else:
        break
version_hash = sha512.hexdigest()[:7]

class pkg_config(object):
  def __init__(self, package):
    self.compile_args = []
    self.include_dirs = []
    self.library_dirs = []
    self.libraries = []
    self.found = True
    self.name = package
    try:
      tokens = subprocess.check_output(['pkg-config', '--libs', '--cflags', package]).split()
      tokens = [ token.decode('ascii') for token in tokens ]
    except subprocess.CalledProcessError:
      tokens = []
      self.found = False
    for token in tokens:
      flag = token[:2]
      value = token[2:]
      if flag == '-I':
        self.include_dirs.append(value)
      elif flag == '-l':
        if value[0] == ':':
          value = value[1:]
        self.libraries.append(value)
      elif flag == '-L':
        self.library_dirs.append(value)
      else:
        if win32_build:
          if token[len(token)-4:] == '.lib':
            self.libraries.append(token[:len(token)-4])
          elif token[:9] == '/LIBPATH:':
            self.library_dirs.append(token[9:])
          else:
            self.compile_args.append(token)
        else:
          self.compile_args.append(token)
  def merge(self, pc):
    self.compile_args.extend([ca for ca in pc.compile_args if ca not in self.compile_args])
    self.include_dirs.extend([ca for ca in pc.include_dirs if ca not in self.include_dirs])
    self.library_dirs.extend([ca for ca in pc.library_dirs if ca not in self.library_dirs])
    self.libraries.extend([ca for ca in pc.libraries if ca not in self.libraries])
  def __repr__(self):
    return str(self.include_dirs)+", "+str(self.library_dirs)+", "+str(self.libraries)

configs = { pkg: pkg_config(pkg) for pkg in ['sch-core'] }
if not configs['sch-core'].found:
  configs['sch-core'] = pkg_config('sch-core_d')
configs['sch-core'].merge(pkg_config('SpaceVecAlg'))

for p,c in configs.items():
  c.compile_args.append('-std=c++11')
  c.include_dirs.append(os.getcwd() + "/include")
  if win32_build:
    c.compile_args.append("-DWIN32")

def GenExtension(name, pkg, ):
  pyx_src = name.replace('.', '/')
  cpp_src = pyx_src + '.cpp'
  pyx_src = pyx_src + '.pyx'
  ext_src = pyx_src
  if pkg.found:
    return Extension(name, [ext_src], extra_compile_args = pkg.compile_args, include_dirs = pkg.include_dirs + [numpy.get_include()], library_dirs = pkg.library_dirs, libraries = pkg.libraries)
  else:
    print("Failed to find {}".format(pkg.name))
    sys.exit(1)
    return None

extensions = [
  GenExtension('sch.sch', configs['sch-core'])
]

extensions = [ x for x in extensions if x is not None ]
packages = ['sch']
data = ['__init__.py', 'c_sch.pxd', 'sch.pxd']

cython_packages = [ x for x in packages if any([ext.name.startswith(x) for ext in extensions]) ]

extensions = cythonize(extensions)

setup(
    name = 'sch',
    version='1.0.0-{}'.format(version_hash),
    ext_modules = extensions,
    packages = packages,
    package_data = { 'sch': data }
)
