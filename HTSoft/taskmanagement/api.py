import requests

# Build API
def builds_getall():
    response=requests.get("https://localhost:44320/api/builds/get",verify=False)
    return response