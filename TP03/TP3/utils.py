import json


def load_json(json_file_name):
    with open(json_file_name) as json_data:
        json_file = json.load(json_data)
    print(json_file)

def write_json(json_file_name, python_object):
    with open(json_file_name, "w")as json_data:
        json.dump(python_object, json_data, sort_keys=True, indent=4)
