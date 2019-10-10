Sample python CGI-bin app
=========================

Uses miniconda distribution, makes environment for app, allows run app on python dev server.

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

Run:
----
```shell script
make run dev 
```
You can check it running on `http://localhost:8000/cgi-bin/app.py`
