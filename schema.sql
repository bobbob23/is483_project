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
    Grad_Month DATETIME,
    Past_salary VARCHAR(250),
    Work_permit VARCHAR(250)
);

-- INSERT INTO Access_Control (Access_ID, Access_Control_Name) VALUES ('1', 'Admin');
-- INSERT INTO Access_Control (Access_ID, Access_Control_Name) VALUES ('2', 'User');
-- INSERT INTO Access_Control (Access_ID, Access_Control_Name) VALUES ('3', 'Manager');
-- INSERT INTO Access_Control (Access_ID, Access_Control_Name) VALUES ('4', 'HR');

---------------------- Job_listing -----------------------
CREATE TABLE Job_listing (
    Job_ID int AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(250),
    Location VARCHAR(250),
    Type VARCHAR(250),
    Department VARCHAR(250),
    Closing_date DATETIME
);
