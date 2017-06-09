# distutils: language = c++

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
cimport c_sch_private
cimport eigen.eigen as eigen
cimport sva.sva as sva

from cython.operator cimport dereference as deref
from libcpp.string cimport string

cdef class S_Object(object):
  def __dealloc__(self):
    if self.__own_impl and isinstance(self, S_Object):
      del self.impl
  def __cinit__(self):
    self.__own_impl = True
    self.impl = NULL
  def transform(self, sva.PTransformd trans):
    c_sch_private.transform(deref(self.impl), deref(trans.impl))

cdef S_ObjectFromPtr(c_sch.S_Object * p):
  cdef S_Object ret = S_Object()
  ret.__own_impl = False
  ret.impl = p
  return ret


def Sphere(double radius):
  cdef S_Object ret = S_Object()
  ret.impl = c_sch_private.Sphere(radius)
  return ret

def Box(double x, double y, double z):
  cdef S_Object ret = S_Object()
  ret.impl = c_sch_private.Box(x, y, z)
  return ret

def STPBV(string fname):
  cdef S_Object ret = S_Object()
  ret.impl = c_sch_private.STPBV(fname)
  return ret

def Polyhedron(string fname):
  cdef S_Object ret = S_Object()
  ret.impl = c_sch_private.Polyhedron(fname)
  return ret

cdef class CD_Pair(object):
  def __dealloc__(self):
    del self.impl
  def __cinit__(self, S_Object obj1, S_Object obj2):
    self.impl = new c_sch.CD_Pair(obj1.impl, obj2.impl)
  def distance(self, eigen.Vector3d p1 = None, eigen.Vector3d p2 = None):
    if p1 is None and p2 is None:
      return self.impl.getDistance()
    elif p1 is not None and p2 is not None:
      return c_sch_private.distance(deref(self.impl), p1.impl, p2.impl)
    else:
      raise TypeError("Wrong argument provided to distance")

cdef class S_Polyhedron(S_Object):
  def __cinit__(self, *args):
    super(S_Polyhedron, self).__init__()
    pass

cdef S_Polyhedron S_PolyhedronFromPtr(shared_ptr[c_sch.S_Polyhedron] ptr):
  cdef S_Polyhedron ret = S_Polyhedron()
  ret.__own_impl = False
  ret.poly = ret.impl = ptr.get()
  return ret
