import json


def read(filename):
    with open(filename, 'r') as f:
        return f.read()

def read_json(filename):
    return json.loads(read(filename))

def get_dict_key_by_value(dictionary: dict, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key



