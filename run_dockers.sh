#!/bin/bash

DB_CONTAINER='db_container'
APP_CONTAINER='app_container'

sudo docker run -ti --name $DB_CONTAINER -d -v ~/course/day0/dbdir/dbdata:/var/lib/postgresql/data postgres
sudo docker run -ti --name $APP_CONTAINER --link $DB_CONTAINER -p 80:5000 -v ~/course/day0/foobar/logs:/foobar/logs firstimage
