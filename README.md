# pydig

pydig is a python wrapper library for the 'dig' command line tool.

[![Build Status](https://travis-ci.org/leonsmith/pydig.svg?branch=master)](https://travis-ci.org/leonsmith/pydig)
[![Python Versions](https://img.shields.io/pypi/pyversions/pydig.svg)](https://pypi.org/project/pydig/)
[![License](https://img.shields.io/pypi/l/pydig.svg?color=informational)](https://pypi.org/project/pydig/)

## Versioning

pydig follows [SemVer](https://semver.org/) (MAJOR.MINOR.PATCH) to track what is in each release.

* Major version number will be bumped when there is an incompatible API change
* Minor version number will be bumped when there is functionality added in a backwards-compatible manner.
* Patch version number will be bumped when there is backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.


## Installation

Installation the package from pypi with your tool of choice `pip`, `poetry`
or `pipenv`.

```bash
pip install pydig
```

## Usage

To use the default resolver you can call `pydig.query` this resolver will use
the `dig` command found in your `$PATH`.
```
>>> import pydig
>>> pydig.query('example.com', 'A')
['93.184.216.34']
>>> pydig.query('www.github.com', 'CNAME')
['github.com.']
>>> pydig.query('example.com', 'NS')
['a.iana-servers.net.', 'b.iana-servers.net.']
```

If your want to adjust the executable location, the nameservers to dig will
query against or would like to pass additional arguments/flags, you can
configure your own instance of a resolver. and call the `query` method of your
custom resolver.

```
>>> import pydig
>>> resolver = pydig.Resolver(
...     executable='/usr/bin/dig',
...     nameservers=[
...         '1.1.1.1',
...         '1.0.0.1',
...     ],
...     additional_args=[
...         '+time=10',
...     ]
... )
>>> resolver.query('example.com', 'A')
>>> ['93.184.216.34']
```

## Documentation

The code is 150~ lines with 100% test coverage

https://github.com/leonsmith/pydig/tree/master/pydig
