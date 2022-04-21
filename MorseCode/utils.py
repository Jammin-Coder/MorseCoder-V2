import json


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def read_json(file_path):
    return json.loads(read_file(file_path))


def get_dict_keys_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key