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

from c_sch cimport *

cdef extern from "sch_wrapper.hpp" namespace "sch":
  void transform(S_Object & obj, const PTransformd&)
  S_Object* Sphere(double)
  S_Object* Box(double, double, double)
  S_Object* STPBV(const string&)
  S_Object* Polyhedron(const string&)
  double distance(CD_Pair&, Vector3d& p1, Vector3d& p2)

