import requests

# Build API
def usersticket_getall():
    url="https://localhost:44320/api/usersticket/getall"
    response=requests.get(url,verify=False)
    return response