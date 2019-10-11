Sample python library 
=========================

Uses miniconda distribution, makes environment for development process, builds python package. 

Install deps:
----------
```shell script
make bootstrap
```

Test:
-----
```shell script
make test 
```

Publish:
----
```shell script
make publish 
```
Result wheel and package will be on dist/
You can test it, following this:

```shell script
pip install dist/library*.whl
python
```
```shell script
Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from library.library import Library
>>> lib = Library()
>>> lib.call()
2.22.0
>>>
```
