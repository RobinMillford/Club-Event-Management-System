create database ClubDB1;
create table Events (
Event_Id varchar(20) not null primary key,
Club_Id varchar(20) not null,
Event_Name varchar(20),
Event_Picture varchar(255),
Event_Type  varchar(20),
Event_Day varchar(10),
Event_Date Date,
Event_Start_Time Time,
Event_End_Time time,
Event_Venue varchar(50),
Event_Mail varchar(20),
Event_Phone_No varchar(15),
Event_Budget float,
Event_Ticket varchar(5),
Event_url varchar(50));

create table Clubs ( 
Club_Id varchar(20) not null primary key,
Club_Name varchar(50) not null,
Club_Type varchar(15),
Club_Picture varchar(255),
Club_Faculty_Cordinator_Name varchar(30),
Club_Mail varchar(20),
Club_Activity varchar(20),
Club_Total_Events int,
Club_Details varchar(255),
Club_Photos_Viwer varchar(255),
FOREIGN KEY (Club_Id) REFERENCES Events(Club_Id));


create table User_Student (
User_Student_Name varchar(30) not null,
User_Student_Id varchar(15) not null primary key,
User_Student_Type varchar(30),
User_Student_Club_Id varchar(20),
FOREIGN KEY (User_Student_Club_Id) REFERENCES Clubs(Club_Id));

create table User_Faculty (
User_Faculty_Name varchar(30) not null,
User_Faculty_Id varchar(15) not null primary key,
User_Faculty_Type varchar(30),
User_Faculty_Club_Id varchar(20),
FOREIGN KEY (User_Faculty_Club_Id) REFERENCES Clubs(Club_Id))
;

create table User_Student_Welfare (
User_Student_Welfare_Name varchar(30) not null,
User_Student_Welfare_Id varchar(15) not null primary key,
User_Student_Welfare_Type varchar(30),
User_Student_Welfare_Club_Id varchar(20));
-- FOREIGN KEY (User_Student_Club_Id) REFERENCES Events(Club_Id));