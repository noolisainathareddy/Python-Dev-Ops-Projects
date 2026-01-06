import sys

def read_app_log():
    dict = {}
    with open("app.log", 'r') as f:
        for line in f:
            data = line.split()
            if dict.__contains__(data[2]):
                dict[data[2]] += 1
                if dict["ERROR"] >= 2:
                    print("exit with Non-200 status code")
                    sys.exit(1)
            else:
                dict[data[2]] = 1
        print(dict)
read_app_log()