import yaml

def read_yaml():
    resources = {}
    with open("resources.yaml", 'r') as f:
        data = yaml.safe_load(f)
        for key, values in data.items():
            for i in values:
                for key, value in i.items():
                    print(key, value)
                    if value in resources:
                        resources[value] = resources[value] + 1
                    else:
                        resources[value] = 1
    print(resources)

read_yaml()