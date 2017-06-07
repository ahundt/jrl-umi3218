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

cmake_minimum_required(VERSION 2.8)

option(PYTHON_BINDING_USER_INSTALL "Install the Python bindings in user space" OFF)
option(DISABLE_TESTS "Disable unit tests." OFF)

set(PIP_EXTRA_OPTIONS "")
if(${PYTHON_BINDING_USER_INSTALL})
  set(PIP_EXTRA_OPTIONS "--user")
endif()

# Build the bindings locally
add_custom_target(sch-python-bindings ALL
  COMMAND python setup.py build_ext --inplace
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  COMMENT "Generating sch Python bindings"
  DEPENDS include/sch_wrapper.hpp
          sch/c_sch.pxd
          sch/c_sch_private.pxd
          setup.py
)

# Test the bindings
if(NOT ${DISABLE_TESTS})
  enable_testing()
  add_test(NAME schPythonBindingsTest
    COMMAND nosetests
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
endif()

# Install the bindings
add_custom_target(install-sch-python-bindings
  COMMAND pip install . ${PIP_EXTRA_OPTIONS}
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  COMMENT "Install sch Python bindings"
)
install(CODE "execute_process(COMMAND ${CMAKE_MAKE_PROGRAM} install-sch-python-bindings)")
