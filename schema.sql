DROP SCHEMA IF EXISTS tsh_db;
CREATE DATABASE tsh_db;
USE tsh_db;

-- DROP TABLE Applicant;
-- DROP TABLE Job_listing;

---------------------- Applicant -----------------------

CREATE TABLE Applicant (
    Email VARCHAR(250) PRIMARY KEY,
    First_name VARCHAR(250),
    Last_name VARCHAR(250),
    Phone_number int(8),
    School VARCHAR(250),
    Course_of_study VARCHAR(250),
    GPA VARCHAR(20),
    Grad_month DATETIME,
    Past_salary VARCHAR(250),
    Work_permit VARCHAR(250),
    Resume VARCHAR(250),
    Transcript VARCHAR(250),
    Reference_Letter VARCHAR(250)
);

---------------------- Job_listing -----------------------
CREATE TABLE Job_listing (
    Job_ID int AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(250),
    Location VARCHAR(250),
    Type VARCHAR(250),
    Department VARCHAR(250),
    Closing_date DATETIME
);
