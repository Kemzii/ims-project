drop database if exists ims;
create database ims;

create table users (
    id varchar primary key,
    firstname varchar(255) not null,
    lastname varchar(255) not null,
    username varchar(255) not null,
    password varchar(255) not null,
    email varchar(255) not null,
    trn varchar(255) not null,
    gender varchar(255) not null
    );
    
