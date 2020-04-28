CREATE TABLE {{ data[0].TABLE_NAME }}(    
    {% for col in data %}{{ col.COLUMN_NAME }} {% if col.DATA_TYPE == "BLOB" %}BINARY{% elif col.DATA_TYPE == "CLOB" %}VARCHAR{% elif col.DATA_TYPE == "DATE" %}TIMESTAMP_NTZ(9)
    {% elif col.DATA_TYPE == "NUMBER" %}FLOAT
    {% elif col.DATA_TYPE == "VARCHAR2" %}VARCHAR({{ col.DATA_LENGTH}})
    {% elif col.DATA_TYPE == "VARCHAR" %}VARCHAR({{ col.DATA_LENGTH}})
    {% elif col.DATA_TYPE == "TIMESTAMP(6)" %}TIMESTAMP_NTZ(9)
    {% elif col.DATA_TYPE == "CHAR" %}VARCHAR{% elif col.DATA_TYPE == "RAW" %}BINARY{% elif col.DATA_TYPE == "ROWID" %}VARCHAR{% endif %}{% if not loop.last %},{% endif %}{% endfor %}
);  
