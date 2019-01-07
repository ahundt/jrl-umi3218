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

from eigen.c_eigen cimport Vector3d
from sva.c_sva cimport *
from libcpp.string cimport string

cdef extern from "<sch/S_Object/S_Object.h>" namespace "sch":
  cdef cppclass S_Object:
    S_Object()

cdef extern from "<sch/S_Polyhedron/S_Polyhedron.h>" namespace "sch":
  cdef cppclass S_Polyhedron(S_Object):
    S_Polyhedron()

cdef extern from "<sch/CD/CD_Pair.h>" namespace "sch":
  cdef cppclass CD_Pair:
    CD_Pair(S_Object*, S_Object*)
    double getDistance()
