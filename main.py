import requests
from _datetime import datetime

USERNAME = "phiton"
TOKEN = "sadfwqe123sdf34"
id= "graph2"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)
#https://pixe.la/@phiton
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": id,
    "name": "Jogging Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers  ={
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{id}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today? "),
}

#response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{id}/{today.strftime('%Y%m%d')}"
update_data ={
    "quantity": "1.1",
}
#response = requests.put(url=update_endpoint, json=update_data, headers=headers)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{id}/{today.strftime('%Y%m%d')}"

#response = requests.delete(url=update_endpoint, headers=headers)
#print(response.text)