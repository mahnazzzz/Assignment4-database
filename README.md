# Assignment4-database

Assignmetn findes [her](https://github.com/datsoftlyngby/soft2019spring-databases/blob/master/assignments/assignment4.md)


## pull Docker image of Mysql
- docker run --rm -it mysql:latest /bin/bash

## Remove the container
- docker rm -v <5-6 lettere in container id >

## The Container that runs
- docker container ls -a 

## To store the files of the database on the host

- mkdir -p mysql_databasefiles echo "$(pwd)"

```sh
- docker run \
--rm \
--name my_mysql \
-v $(pwd)/mysql_databasefiles:/var/lib/mysql \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=deterentysker!42snapsnap \
-d \
mysql
echo "Wooootttt"

```

docker exec -it mysql bash

__

