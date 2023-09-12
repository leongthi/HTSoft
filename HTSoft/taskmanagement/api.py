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

#xử lý ticket tuần
#1. api/tickets/listweek/getallweek
def listweek_GetAllWeek():
    url="https://localhost:44320/api/tickets/listweek/getallweek"
    response=requests.get(url,verify=False)
    return response


#2. api/tickets/listweek/getallteam

def listweek_GetAllTeam():
    url="https://localhost:44320/api/tickets/listweek/getallteam"
    response=requests.get(url,verify=False)
    return response

#3.  api/tickets/listweek/getlistweek
def get_list_week(weekid, teamid):
    url = 'http://localhost/api/tickets/listweek/getlistweek'  # Thay đổi URL tương ứng với địa chỉ của API
    params = {'weekid': weekid, 'teamid': teamid}  # Đặt các tham số trong query string

    response = requests.get(url, params=params)
    
    return response

#end xử lý ticket tuần