import yaml


def read_yaml():
    yamlfile = "pod.yaml"
    try:
        with open(yamlfile, 'r') as readfile:
            data = yaml.safe_load(readfile)
            print("Pod Name: ", data["metadata"]["name"])
            print("Namespace: ", data["metadata"]["namespace"])
            print("Image: ", data["spec"]["containers"][0]["name"])
    except FileNotFoundError:
        print("Unable to find the pod.yaml file")
    except PermissionError:
        print("Does have access to read a file")
    except Exception as e:
        print("Exception occurred - Error", e)
    finally:
        readfile.close()

read_yaml()