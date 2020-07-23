import json
import requests
import jsonpath

api_url= "https://reqres.in/api/users?page=2"

#Make a request
response1= requests.get(api_url)
print(response1.text)

#Validate Status Code
assert response1.status_code==200

#Parse response into Json format
json_response= json.loads(response1.text)
print(json_response)

#Apply Json path
x= jsonpath.jsonpath(json_response, 'total')
print(x[0])
y=jsonpath.jsonpath(json_response, 'data[0].avatar')
print(y)

for val in json_response['data']:
    print(val['email'])

