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

cimport c_sch
from libcpp cimport bool as cppbool

cdef extern from "<memory>" namespace "std" nogil:
  cdef cppclass shared_ptr[T]:
    T* get()

cdef class S_Object(object):
  cdef c_sch.S_Object * impl
  cdef cppbool __own_impl

cdef S_ObjectFromPtr(c_sch.S_Object *)

cdef class CD_Pair(object):
  cdef c_sch.CD_Pair * impl

cdef class S_Polyhedron(S_Object):
  cdef c_sch.S_Polyhedron * poly

cdef S_Polyhedron S_PolyhedronFromPtr(shared_ptr[c_sch.S_Polyhedron])
