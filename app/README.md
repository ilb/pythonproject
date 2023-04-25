Sample python web app based on Bottle
=========================================

Install deps:
----------
```shell script
python setup.py .["dev"]
```

Test:
-----
```shell script
pytest
```

Build package:
----
```shell script
python setup.py sdist bdist_wheel
```

Install package:
----

```shell script
pip install dist/*.whl
```

Run package:
----

```shell script
(PYTHON_EXEC)/bin/webapp
/usr/bin/python3.8.5/bin/webapp
```

Swagger schema on `http://localhost:8000/webapp/swagger/`

You can check it running on `http://localhost:8000/webapp/time/`
