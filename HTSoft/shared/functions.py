import json


def Initial(response):
    list_json=json.dumps(response.json())
    list=json.loads(list_json)
    

    return list