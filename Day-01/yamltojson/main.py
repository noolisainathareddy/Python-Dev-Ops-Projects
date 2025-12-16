import yaml
import json

def convert_yaml():
    with open("service.yaml", 'r') as readyaml:
        data = yaml.safe_load(readyaml)
        yaml.lo
        print(data)
    with open("service.json", 'w') as updatejson:
         json.dump(data, updatejson, indent=4)



convert_yaml()

