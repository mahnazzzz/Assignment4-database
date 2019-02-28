# Assignment4-database

Assignmetn findes [her](https://github.com/datsoftlyngby/soft2019spring-databases/blob/master/assignments/assignment4.md)


## pull Docker image of Mysql

```sh
- docker run --rm -it mysql:latest /bin/bash
or
- docker run --rm --name my_mysql -v ./mysql_databasefiles:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql
```
### Run the docker
```sh
docker exec -it my_mysql bash
```
### Check for runing the container
```sh
- docker container ls -a 
```
### To store the files of the database on the host
```sh
- mkdir -p mysql_databasefiles echo "$(pwd)"
```
### Remove the container

```sh
For close or remove the container: docker kill my_mysql docker rm my_mysql
```

- Link for download the mysql data [her](http://www.mysqltutorial.org/mysql-sample-database.aspx)

```sh
After you find the sql statement you can run that script on mysql database
```

## Create a database user for each of the four roles  

```sh
CREATE USER 'inventory'@'%' IDENTIFIED BY 'invAdmin';
CREATE USER 'bookkeeping'@'%' IDENTIFIED BY 'bookAdmin';
CREATE USER 'hr'@'%' IDENTIFIED BY 'hrAdmin';
CREATE USER 'sales'@'%' IDENTIFIED BY 'saleAdmin';
CREATE USER 'it'@'%' IDENTIFIED BY 'itAdmin';

@'%' account uses the '%' wildcard for the host part, so it can be used to connect from any host.
```
## restrictive in what the each user can do in the database.
```sh
GRANT SELECT, INSERT, UPDATE, DELETE ON classicmodels.products TO inventory@'%';
GRANT SELECT, INSERT, UPDATE, DELETE ON classicmodels.productlines TO inventory@'%';

GRANT SELECT, UPDATE  ON classicmodels.orderdetails TO bookkeeping@'%';
GRANT SELECT, UPDATE  ON classicmodels.orders TO bookkeeping@'%';
GRANT SELECT, UPDATE  ON classicmodels.payments TO bookkeeping@'%';
GRANT SELECT  ON classicmodels.customers TO bookkeeping@'%';

GRANT SELECT, INSERT, UPDATE, DELETE ON classicmodels.employees TO hr@'%';
GRANT SELECT, INSERT, UPDATE, DELETE ON classicmodels.offices TO hr@'%';

GRANT SELECT, INSERT, UPDATE, DELETE ON classicmodels.customers TO sales@'%';
GRANT SELECT, INSERT, UPDATE, DELETE ON classicmodels.orderdetails TO sales@'%';
GRANT SELECT, INSERT, UPDATE, DELETE ON classicmodels.orders TO sales@'%';
GRANT SELECT, UPDATE ON classicmodels.products TO sales@'%';

GRANT ALL PRIVILEGES ON *.* TO 'it'@'%';

By manipulating the MySQL grant tables directly with statements such as INSERT, UPDATE, or DELETE.
*Bookkeeping - Making sure that all orders are payed.
```

### Exeercize.2

## Create the users
```sh
INSERT INTO `classicmodels`.`employees` (`employeeNumber`, `lastName`, `firstName`, `extension`, `email`, `officeCode`, `reportsTo`, `jobTitle`) VALUES ('1703', 'Kim', 'kim keri', 'x5429', 'mahnaazi@yahoo.com', '4', '1143', 'Sales Rep');
INSERT INTO `classicmodels`.`employees` (`employeeNumber`, `lastName`, `firstName`, `extension`, `email`, `officeCode`, `reportsTo`, `jobTitle`) VALUES ('1705', 'Florance', 'Maria', 'x2312', 'sisam@gmail.com', '5', '1621', 'Sales Rep');
```

## Insert new product
```sh
INSERT INTO `classicmodels`.`products` (`productCode`, `productName`, `productLine`, `productScale`, `productVendor`, `productDescription`, `quantityInStock`, `buyPrice`, `MSRP`) VALUES ('S10_2825', 'HMS1 Bounty2', 'Motorcycles', '1:10', 'Min Lin Diecast', 'Comes with 2 masts, all square-rigged', '221', '33.22', '568.79');
```
## Create new order
```sh
INSERT INTO `classicmodels`.`orders` (`orderNumber`, `orderDate`, `requiredDate`, `status`, `customerNumber`) VALUES ('10427', '2005-06-01', '2005-10-07', 'In Process', '119');
```
## Backup
docker exec CONTAINER /usr/bin/mysqldump -u root --password=root DATABASE > backup.sql

## Restore
cat backup.sql | docker exec -i CONTAINER /usr/bin/mysql -u root --password=root DATABASE
