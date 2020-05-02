#pip3 installation
sudo apt install python3-pip

#mysql installation
pip3 install mysql-connector-python

#sql user creation
https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql


#database creation
create databse radb;

#table creation
create table users(id int AUTO_INCREMENT primary key,name varchar(200),email varchar(200),username varchar(200),password varchar(200));

