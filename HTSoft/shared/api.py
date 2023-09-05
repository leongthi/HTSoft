import requests

# Build API
def clients_getall():
    url="https://localhost:44320/api/clients/getall"
    response=requests.get(url,verify=False)
    return response


def usersTicket_getall():
    url="https://localhost:44320/api/usersticket/getall"
    response=requests.get(url,verify=False)
    return response