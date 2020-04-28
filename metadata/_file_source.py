def single_value_file_source(data_file):
    with open(data_file, 'r') as table_list:
        content = table_list.readlines()
    content = [entry.strip() for entry in content]
    return content

def json_file_source(data_file):
    import json
    with open(data_file, 'r') as table_list:
        #content = table_list
        content = json.load(table_list)
    return content

def csv_file_source(data_file, **kwargs):
    import csv
    with open(data_file) as csvfile:
        reader = csv.DictReader(csvfile, **kwargs)
        content = list(reader)
    return content
