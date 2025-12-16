import json
from textwrap import indent


def merge_json():
    with open("base.json", 'r') as basejson:
        basedata = json.load(basejson)
        # print(json.dumps(basedata, indent=4))
        # basejson.seek(0)

    with open("override.json", 'r') as override:
        overridedata = json.load(override)
        # print(json.dumps(overridedata, indent=4))

    # merged = basedata | overridedata
    # print(merged)
    #========OR========================
    merged = basedata.copy()
    merged.update(overridedata)
    print(merged)


merge_json()