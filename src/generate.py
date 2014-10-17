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

from pybindgen import *
import sys


def import_eigen3_types(mod):
  mod.add_class('Vector3d', foreign_cpp_namespace='Eigen', import_from_module='eigen3')

  mod.add_class('Matrix3d', foreign_cpp_namespace='Eigen', import_from_module='eigen3')

  mod.add_class('MatrixXd', foreign_cpp_namespace='Eigen', import_from_module='eigen3')
  mod.add_class('VectorXd', foreign_cpp_namespace='Eigen', import_from_module='eigen3')



def import_sva_types(mod):
  mod.add_class('PTransformd', foreign_cpp_namespace='sva', import_from_module='spacevecalg')



def build_sch(sch):
  obj = sch.add_class('S_Object')
  pair = sch.add_class('CD_Pair')

  obj.add_function_as_method('transform', None, [param('sch::S_Object&', 'obj'),
                                                 param('const sva::PTransformd&', 'trans')],
                             custom_name='transform')


  sch.add_function('Sphere', retval('sch::S_Object*', caller_owns_return=True),
                   [param('double', 'radius')])
  sch.add_function('Box', retval('sch::S_Object*', caller_owns_return=True),
                   [param('double', 'x'),
                    param('double', 'y'),
                    param('double', 'z')])
  sch.add_function('STPBV', retval('sch::S_Object*', caller_owns_return=True),
                   [param('const std::string&', 'filename')])
  sch.add_function('Polyhedron', retval('sch::S_Object*', caller_owns_return=True),
                   [param('const std::string&', 'filename')])


  pair.add_constructor([param('sch::S_Object*', 'obj1', transfer_ownership=False),
                        param('sch::S_Object*', 'obj2', transfer_ownership=False)])

  pair.add_method('getDistance', retval('double'), [], custom_name='distance')

  pair.add_function_as_method('distance', retval('double'),
                              [param('sch::CD_Pair&', 'pair'),
                               param('Eigen::Vector3d&', 'p1'),
                               param('Eigen::Vector3d&', 'p2')],
                              custom_name='distance')




if __name__ == '__main__':
  if len(sys.argv) < 2:
    sys.exit(1)

  sch = Module('_sch', cpp_namespace='::sch')
  sch.add_include('<SpaceVecAlg/SpaceVecAlg>')
  sch.add_include('<sch/S_Object/S_Object.h>')
  sch.add_include('<sch/S_Object/S_Sphere.h>')
  sch.add_include('<sch/S_Object/S_Box.h>')
  sch.add_include('<sch/S_Polyhedron/S_Polyhedron.h>')
  sch.add_include('<sch/STP-BV/STP_BV.h>')
  sch.add_include('<sch/CD/CD_Pair.h>')

  sch.add_include('"sch/Python/SCHAddon.h"')

  dom_ex = sch.add_exception('std::domain_error', foreign_cpp_namespace=' ',
                               message_rvalue='%(EXC)s.what()')
  out_ex = sch.add_exception('std::out_of_range', foreign_cpp_namespace=' ',
                               message_rvalue='%(EXC)s.what()')

  # import Eigen3, and sva
  import_eigen3_types(sch)
  import_sva_types(sch)

  # sch
  build_sch(sch)

  with open(sys.argv[1], 'w') as f:
    sch.generate(f)

