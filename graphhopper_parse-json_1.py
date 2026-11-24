import requests 
import urllib.parse 
geocode_url = "https://graphhopper.com/api/1/geocode?" 
route_url = "https://graphhopper.com/api/1/route?" 
loc1 = "Rome" 
loc2 = "Italy" 
key = "f097bc9e-0d73-4697-ad57-d45b20ea32fc"  ## Replace with your API key 

url = geocode_url + urllib.parse.urlencode({"q":loc1, "limit": "1", "key":key}) 

replydata = requests.get(url) 
json_data = replydata.json() 
json_status = replydata.status_code 
print(json_data) 