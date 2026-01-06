import yaml

def read_yaml():
    with open('pod.yaml', 'r') as f:
        data = yaml.safe_load(f)
        print(type(data))

read_yaml()