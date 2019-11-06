Sample python CGI-bin app based on Bottle
=========================================

Uses miniconda distribution, makes environment for app, allows run app on python dev server.

Install deps:
----------
```shell script
make bootstrap
```

Update deps:
-----------
```shell script
make update
```

Test:
-----
```shell script
make test 
```

Run:
----
```shell script
make run
```

Format:
------
Black used as formatter.

```shell script
make format
```

You can check it running on `http://localhost:8000/cgi-bin/controller.py/time`
Swagger docs available on `http://localhost:8000/cgi-bin/controller.py/swagger/`
