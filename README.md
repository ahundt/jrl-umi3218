sch-core-python
===============

Python bindings for [sch-core][core]. These bindings were initially part of
[Tasks][tasks] by @jorisv.

## Dependencies

* [sch-core][core]
* Python 2 or 3
* [PyBindGen][pybindgen]
* [SpaceVecAlg][sva]
* [Eigen 3][eigen]

## Install

```sh
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX="/your/install/prefix" -DCMAKE_BUILD_TYPE=RelWithDebInfo
make
make install
```

Note: if you are on a Debian-based distribution (e.g. Ubuntu), you may want to
add the `-DPYTHON_DEB_LAYOUT` flag to the `cmake` command in order to install
this package with the specific Debian layout.

[core]:      https://github.com/jrl-umi3218/sch-core
[eigen]:     http://eigen.tuxfamily.org
[pybindgen]: https://pypi.python.org/pypi/PyBindGen
[sva]:       https://github.com/jorisv/SpaceVecAlg
[tasks]:     https://github.com/jorisv/Tasks
