"""
DDL Generator using metadata

Requirements:

CSV file as input with headers:

TABLE_NAME	COLUMN_NAME	DATA_TYPE	DATA_LENGTH
EMPLOYEE    ID          NUMBER      22
EMPLOYEE    NAME        VARCHAR     255
EMPLOYEE    LAST_NAME   VARCHAR     255
EMPLOYEE    DOB         DATE        7

.sql Template for the script 

INSERT.sql = INSERT INTO {{ TABLE_NAME }} VALUES {1,2,3}

OUTPUT FOLDER
To output the scripts using the template.

"""
import metadata.file_based_template as file_based_template
import glob,os
from termcolor import colored,cprint

def count_files():
    file_count = 0
    for file in glob.glob(os.path.join(file_template.output_directory,'*.*')):
        file_count +=1
    return file_count

def main():
    current_path = os.getcwd()
    file_template = file_based_template.file_based_template()
    file_template.output_directory = current_path+'\OUTPUT'
    file_template.output_file_name_fn = lambda v: v[0]['TABLE_NAME']+'.sql'
    file_template.data_file = current_path+'\\table_metadata.csv'
    file_template.template_directory = current_path+'\TEMPLATES'
    file_template.template_name = 'DDL_METADATA.sql'
    file_template.format = file_template.CSV
    file_template.run_single_file(group_by=lambda row:row["TABLE_NAME"])
    
    print(file_template.template_directory)
    print(file_template.data_file)
    print(file_template.output_directory)

main()