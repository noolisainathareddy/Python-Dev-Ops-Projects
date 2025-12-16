import yaml
import os

def read_files():
    allowed_types = ["Deployment", "Pod", "Service"]
    list = os.listdir("manifest_files")
    print(list)
    for i in list:
        file_path = os.path.join("manifest_files", i)
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
            if data["kind"] in allowed_types:
                print(data["kind"], "is allowed")
            else:
                print(data["kind"], "is not allowed")

read_files()
