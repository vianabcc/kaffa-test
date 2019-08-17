from dateutil import tz
from datetime import datetime
import requests

# 5) Rest Client - World Clock
def convertToLocal(dateTime):
    utc_zone = tz.tzutc()
    local_zone = tz.tzlocal()
    
    utc = datetime.strptime(dateTime, '%Y-%m-%dT%H:%MZ')
    utc = utc.replace(tzinfo=utc_zone)

    # Convert time zone
    local = utc.astimezone(local_zone)
    return local

def requestCurrentDate():
    response = requests.get("http://worldclockapi.com/api/json/utc/now")
    rjson = response.json()
    print("UTC Data/Time:", rjson['currentDateTime'])
    print("Local Data/Time:", convertToLocal(rjson['currentDateTime']))

requestCurrentDate()

# 6) Rest Server - World Clock
def requestServer():
    currentDateTime = datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ')
    return { 
                "currentDateTime": currentDateTime 
           }

response = requestServer()
print("Current Date/Time response: ", response)