import json


def validate_json():
    required_keys = ["name", "port", "env"]
    with open("app.json", 'r') as readjson:
        data = json.load(readjson)
        keys = data.keys()
        for i in required_keys:
            if i in keys:
                print("Key exists: ", i)
            else:
                print("Key doesn't exist: ", i)


validate_json()