[![Latest version on
PyPi](https://badge.fury.io/py/tox-teamcity.svg)](https://badge.fury.io/py/tox-teamcity)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/tox-teamcity.svg)](https://pypi.org/project/tox-teamcity/)
[![Azure Pipelines build
status](https://dev.azure.com/morganwahl/tox-teamcity/_apis/build/status/tox%20ci?branchName=master)](https://dev.azure.com/morganwahl/tox-teamcity/_build/latest?definitionId=9&branchName=master)
[![Documentation
status](https://readthedocs.org/projects/tox-teamcity/badge/?version=latest&style=flat-square)](https://tox-teamcity.readthedocs.io/en/latest/?badge=latest)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

# tox-teamcity

A [Tox](https://tox.wiki/en/latest/) plugin for better integration with the [TeamCity](https://www.jetbrains.com/teamcity/) CI server.

Features
--------

Tells TeamCity that the tests run in each tox environment are a separate "test
suite" with the same name as the environment.


Requirements
------------

Depends on the `teamcity-messages` library to format the output for TeamCity.


Installation
------------

You can install "tox-teamcity" via [pip](https://pypi.org/project/pip/) from [PyPI](https://pypi.org):

```
pip install tox-teamcity
```

Usage
-----

Just install the plugin in the same virtualenv as tox itself.

Contributing
------------
Contributions are very welcome. Tests can be run with [tox](https://tox.readthedocs.io/en/latest/), please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the **GNU GPL v3.0** license, `tox-teamcity` is
free and open source software.


Issues
------

If you encounter any problems, please
[file an issue](https://github.com/morganwahl/tox-teamcity/issues)
along with a detailed description.
