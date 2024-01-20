#!/bin/bash

/wait-for-it.sh db:3306 -t 30

flask db init
flask db migrate
flask db upgrade

flask run --host=0.0.0.0 --port=5000
