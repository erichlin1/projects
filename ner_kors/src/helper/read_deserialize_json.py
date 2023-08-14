import json

def read_deserialize_json(file_path):
    with open(file_path, 'r') as file:
        ## returns json object as dict
        data = json.load(file)
        return data
    
