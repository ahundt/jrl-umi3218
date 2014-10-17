# Copyright 2014, Benjamin Chrétien, CNRS-UM2 LIRMM
#
# This file is part of sch-core-python.
# sch-core-python is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# sch-core-python is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# sch-core.  If not, see <http://www.gnu.org/licenses/>.

# Requires at least CMake 2.6 to configure the package.
CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

INCLUDE(cmake/base.cmake)
INCLUDE(cmake/eigen.cmake)
INCLUDE(cmake/python.cmake)

SET(PROJECT_NAME sch-core-python)
SET(PROJECT_DESCRIPTION "SCH Core Python")
SET(PROJECT_URL "http://github.com/jrl-umi3218/sch-core-python")

SET(HEADERS
  ${CMAKE_SOURCE_DIR}/include/sch/Python/SCHAddon.h
  )

SET(CXX_DISABLE_WERROR 1) #FIXME: disable for now.

SETUP_PROJECT()

# Search for dependencies.
ADD_REQUIRED_DEPENDENCY("sch-core")
ADD_REQUIRED_DEPENDENCY("eigen3")
ADD_REQUIRED_DEPENDENCY("SpaceVecAlg")

# FIXME: add pybindgen build dependency

# Look for Python 2.7 in priority
SET(Python_ADDITIONAL_VERSIONS 2.7)
FINDPYTHON()

HEADER_INSTALL("${HEADERS}")

ADD_SUBDIRECTORY(src)

SETUP_PROJECT_FINALIZE()
