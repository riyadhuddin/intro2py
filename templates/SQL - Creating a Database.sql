##########################################################

# SQL - Creating a Database

##########################################################

-- Step 1: Use the CREATE statement to create a database

CREATE DATABASE Sales;

-- Alternatively, you can use the word 'schema' for achieving the same goal

### CREATE SCHEMA Sales;

-- Step 2: Use the optional statement IF NOT EXIST to create the same database or verify it is already created

CREATE DATABASE IF NOT EXISTS Sales;

-- Alternatively, you can use the word 'schema' for achieving the same goal

### CREATE SCHEMA IF NOT EXISTS Sales;