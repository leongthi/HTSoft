import json


def InitialBuild(response):
    build_list_json=json.dumps(response.json())
    build_list=json.loads(build_list_json)
    

    return build_list