import yaml
from yaml import safe_load, safe_dump

def update_yaml():
    with open("pod.yaml") as readfile:
        data = yaml.safe_load(readfile)
        data["kind"] = "service"
        data["metadata"]["namespace"] = "uat"
        readfile.seek(0)
        readfile = yaml.safe_dump(data)
        print(readfile)

update_yaml()