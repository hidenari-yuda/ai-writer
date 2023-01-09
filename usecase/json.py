import json


def write_json(data):

    dict = {
        "aaa": 123,
        "bbb": "123",
        "ccc": "あいうえお",
        "ddd": "一二三",
    }

    path3 = './test3.json'
    json_file3 = open(path3, mode="w")
    json.dump(dict, json_file3, indent=2, ensure_ascii=False)
    json_file3.close()
