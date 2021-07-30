# time-table-api

### Important commands to help run program
1. to start django project: `docker-compose run web django-admin startproject config .`

2. to build docker: `docker-compose up -d --build` or `docker build .`
3. to makemigration: `docker-compose run web python manage.py makemigration`
4. to migrate: ` docker-compose run web python manage.py migrate`
5. to run docker: `docker-compose up`
6. to remove docker: ` docker rm [docker ID]`
7. to see docker: `docker ps`
8. `docker-compose down -v` to remove the volumes along with the containers.

### some db commands
9. to check that the default django db were created `docker-compose exec db psql --username=postgres --dbname=postgres`
10. ` \l ` to list db
11. ` \c ` postgres to switch to postgres db
12. ` \dt ` to see tables in db


### important link to help in production environment for docker

[Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)