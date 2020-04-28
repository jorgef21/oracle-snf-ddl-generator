# oracle-snf-ddl-generator
DDL Generator using metadata

# Requirements:
- CSV file as input with headers:

__TABLE_NAME__ | __COLUMN_NAME__ | __DATA_TYPE__ | __DATA_LENGTH__
---------- | ----------- | --------- | -----------
EMPLOYEE   |  ID         |   NUMBER  |        22
EMPLOYEE   |  NAME       |   VARCHAR |        255
EMPLOYEE   |  LAST_NAME  |   VARCHAR |        255
EMPLOYEE   |  DOB        |   DATE    |        7

- .sql Template for the script(folder TEMPLATEs): 
```SQL
CREATE TABLE {{ data[0].TABLE_NAME }}(    
    {% for col in data %}{{ col.COLUMN_NAME }} {% if col.DATA_TYPE == "BLOB" %}BINARY{% elif col.DATA_TYPE == "CLOB" %}VARCHAR{% elif col.DATA_TYPE == "DATE" %}TIMESTAMP_NTZ(9)
    {% elif col.DATA_TYPE == "NUMBER" %}FLOAT
    {% elif col.DATA_TYPE == "VARCHAR2" %}VARCHAR({{ col.DATA_LENGTH}})
    {% elif col.DATA_TYPE == "VARCHAR" %}VARCHAR({{ col.DATA_LENGTH}})
    {% elif col.DATA_TYPE == "TIMESTAMP(6)" %}TIMESTAMP_NTZ(9)
    {% elif col.DATA_TYPE == "CHAR" %}VARCHAR{% elif col.DATA_TYPE == "RAW" %}BINARY{% elif col.DATA_TYPE == "ROWID" %}VARCHAR{% endif %}{% if not loop.last %},{% endif %}{% endfor %}
);  
```

### Output script would be(in folder output) EMPLOYEE.sql:
```SQL
CREATE TABLE EMPLOYEE(    
    ID FLOAT
    ,NAME VARCHAR(255)
    ,LAST_NAME VARCHAR(255)
    ,DOB TIMESTAMP_NTZ(9)
    ,STATUS VARCHAR
);  
```

### You can download a CSV files with metadata-info from OracleDB with the following query
```SQL
SELECT TABLE_NAME,COLUMN_NAME,DATA_TYPE,DATA_LENGTH
FROM ALL_TAB_COLUMNS
WHERE TABLE_NAME LIKE 'ANY_PATERN%' #
AND OWNER='TABLE_SCHEMA'
ORDER BY TABLE_NAME,COLUMN_ID;
```

## You can modify the variables 
```python
  file_template.output_directory = current_path+'\OUTPUT'                    #Change output folder
  file_template.output_file_name_fn = lambda v: v[0]['TABLE_NAME']+'.sql'    #Change output scripts name
  file_template.data_file = current_path+'\\table_metadata.csv'              #Change meta-data file_name/directory
  file_template.template_directory = current_path+'\TEMPLATES'               #Change templates folder
  file_template.template_name = 'DDL_METADATA.sql'                           #Chante template
  file_template.format = file_template.CSV                                   
  file_template.run_single_file(group_by=lambda row:row["TABLE_NAME"])      
```