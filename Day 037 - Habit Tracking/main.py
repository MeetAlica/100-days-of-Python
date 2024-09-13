import requests
from datetime import datetime
from constants import USERNAME, TOKEN, GRAPH_ID, QUANTITY, NAME, UNIT, TYPE, COLOR


pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": NAME,
    "unit": UNIT,
    "type": TYPE,
    "color": COLOR
}
headers = {
    "X-USER-TOKEN": TOKEN
}

requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
today_date = today.strftime("%Y%m%d")
pixel_data = {
    "date": today_date,
    "quantity": QUANTITY
}

requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
