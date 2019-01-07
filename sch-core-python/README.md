sch-core-python
===============

Python bindings for [sch-core][core]. These bindings were initially part of
[Tasks][tasks] by @jorisv.

## Dependencies

* [sch-core][core]
* Python 2 or 3
* [Cython][cython]
* [SpaceVecAlg][sva] (including Python bindings)
* [Eigen 3][eigen] (including [Python bindings][eigenpython])

## Install

```sh
pip install .
```

[core]:      https://github.com/jrl-umi3218/sch-core
[cython]: http://cython.org/
[eigen]:     http://eigen.tuxfamily.org
[eigenpython]: https://github.com/jrl-umi3218/Eigen3ToPython
[pybindgen]: https://pypi.python.org/pypi/PyBindGen
[sva]:       https://github.com/jorisv/SpaceVecAlg
[tasks]:     https://github.com/jorisv/Tasks
