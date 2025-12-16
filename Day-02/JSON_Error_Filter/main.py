import json

def log_errors():
    with open("output.json", 'r') as f:
        data = json.load(f)
        for i in data:
            if i["level"] == "ERROR":
                print(i["msg"])

log_errors()