import yaml

def read_yaml():
    with open("config.yaml", 'r') as f:
        data = yaml.safe_load(f)
        for key, value in data.items():
            if key == "prod":
                print(value["replicas"])

read_yaml()

