#!/bin/bash

sudo docker run -ti -p 80:5000 -v ~/course/day0/foobar/logs:/foobar/logs firstimage
