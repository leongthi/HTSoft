import requests

# Build API
def builds_getall():
    url="https://localhost:44320/api/builds/get"
    response=requests.get(url,verify=False)
    return response

# Ticket API get with build id
def buildTicket_get(buildid):
    url="https://localhost:44320/api/tickets/BuildTicket/"+str(buildid)
    PARAMS={'buildid':buildid}
    response=requests.get(url,PARAMS,verify=False)
    return response

#Ticket list
def Tickets_getall():
    url="https://localhost:44320/api/tickets/getall"
    response=requests.get(url,verify=False)
    return response