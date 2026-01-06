import json

def read_json():
    with open("infrs.json", 'r') as f:
        data= json.load(f)
        print(type(data))