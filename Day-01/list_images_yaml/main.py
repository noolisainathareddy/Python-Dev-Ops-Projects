import yaml

def list_images():
    with open("deployment.yaml") as readfile:
        data = yaml.safe_load(readfile)
        for i in data["spec"]["template"]["spec"]["containers"]:
            print(i["image"])

list_images()