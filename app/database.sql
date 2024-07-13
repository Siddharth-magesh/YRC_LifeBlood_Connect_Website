create database YRCBloodRequest;
use YRCBloodRequest;

create table Address_ID ( 
address_id varchar(10), 
pincode int NOT NULL, 
country varchar(20),
state varchar(25),
city varchar(25),
address varchar(225),
primary key (address_id)
);

create table Disease_ID (
disease_id varchar(10),
disease varchar(200),
primary key (disease_id)
);

create table admin_table (
admin_id varchar(10) NOT NULL,
admin_name varchar(100),
admin_username varchar(100) NOT NULL,
admin_password varchar(500) NOT NULL,
last_login datetime,
primary key (admin_id)
);

create table victim_request(
name varchar(100),
age int,
blood_grp varchar(10) NOT NULL,
admitted_hospital varchar(100),
contact_number int,
attendant_name varchar(100),
hospital_address varchar(200),
due_date date,
reason varchar(150),
request_id varchar(10),
status varchar(25),
donor_name varchar(100),
donar_id varchar(10),
primary key (request_id)
);

create table donars_table (
unique_id varchar(15) NOT NULL, 
Name varchar(100), 
age int NOT NULL,
blood_grp varchar(10) NOT NULL,
DOB date NOT NULL,
address_id varchar(15),
no_of_times_donated int NOT NULL,
disease_id varchar(15),
last_donated_date date NOT NULL,
primary key (unique_id),
foreign key (address_id) references Address_ID(address_id),
foreign key (disease_id) references Disease_ID(disease_id)
);

