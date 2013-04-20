#!/bin/bash

python2.7 manage.py collectstatic
python2.7 manage.py syncdb
python2.7 manage.py runserver 0.0.0.0:8888
