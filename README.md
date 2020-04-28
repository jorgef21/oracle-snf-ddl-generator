# oracle-snf-ddl-generator
DDL Generator using metadata

# Requirements:
- CSV file as input with headers:
TABLE_NAME | COLUMN_NAME | DATA_TYPE | DATA_LENGTH
---------- | ------------- | ------------- | -------------
EMPLOYEE    ID          NUMBER      22
EMPLOYEE    NAME        VARCHAR     255
EMPLOYEE    LAST_NAME   VARCHAR     255
EMPLOYEE    DOB         DATE        7

- .sql Template for the script 
INSERT.sql = INSERT INTO {{ TABLE_NAME }} VALUES {1,2,3}
OUTPUT FOLDER
To output the scripts using the template.