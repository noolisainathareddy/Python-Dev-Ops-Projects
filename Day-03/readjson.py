import json

def read_json():
    with open("infra.json", 'r') as f:
        data = json.load(f)
        if (data.get("environment") in ("dev", "qa", "prod") and
            data.get("replicas") >=0 and
            data.get("instance_type") is not None):
            print("Config is valid")
        else:
            print("Config is Invalid")



read_json()