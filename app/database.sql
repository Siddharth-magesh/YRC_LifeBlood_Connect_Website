create database YRCBloodRequest;
use YRCBloodRequest;

CREATE TABLE Address_ID (
    address_id VARCHAR(10) PRIMARY KEY,
    pincode INT NOT NULL,
    country VARCHAR(20),
    state VARCHAR(25),
    city VARCHAR(25),
    address VARCHAR(225)
);

CREATE TABLE Disease_ID (
    disease_id VARCHAR(10) PRIMARY KEY,
    disease VARCHAR(200)
);

CREATE TABLE admin_table (
    admin_id VARCHAR(10) PRIMARY KEY,
    admin_email VARCHAR(100),
    admin_username VARCHAR(100) NOT NULL,
    admin_password VARCHAR(500) NOT NULL,
    last_login DATETIME
);

CREATE TABLE victim_request (
    request_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    blood_grp VARCHAR(10) NOT NULL,
    admitted_hospital VARCHAR(100) NOT NULL,
    contact_number INT,
    attendant_name VARCHAR(100) NOT NULL,
    hospital_address VARCHAR(200) NOT NULL,
    due_date DATE,
    reason VARCHAR(150),
    status VARCHAR(25),
    donor_name VARCHAR(100),
    donor_id VARCHAR(10)
);

CREATE TABLE donars_table (
    unique_id VARCHAR(15) PRIMARY KEY,
    Name VARCHAR(100),
    age INT NOT NULL,
    blood_grp VARCHAR(10) NOT NULL,
    DOB DATE NOT NULL,
    address_id VARCHAR(15) NOT NULL,
    no_of_times_donated INT,
    disease_id VARCHAR(15),
    last_donated_date DATE,
    status VARCHAR(20) NOT NULL,
    contact_no VARCHAR(20) NOT NULL,
    FOREIGN KEY (address_id) REFERENCES Address_ID(address_id),
    FOREIGN KEY (disease_id) REFERENCES Disease_ID(disease_id)
);