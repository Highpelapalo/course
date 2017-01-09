CREATE USER docker_user;
CREATE DATABASE docker;
GRANT ALL PRIVILEGES ON DATABASE docker TO docker_user;
SET search_path TO foobar, public;
