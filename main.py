import requests
from datetime import datetime


USERNAME = "name"
TOKEN = "password"


headers = {
    "X-USER-TOKEN": TOKEN
}


year = datetime.now().strftime("%Y")
month = datetime.now().strftime("%m")
day = datetime.now().strftime("%d")
date = f"{year}{month}{day}"


# create user
# user_params = {
#     "token": "token",
#     "username": "name",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# pixela_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)



# create graph
# graph_params = {
#     "id": "mygraph",
#     "name": "Study Time",
#     "unit": "hours",
#     "type": "int",
#     "color": "momiji",
# }
# create_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
# response = requests.post(url=crete_graph_endpoint, headers=headers, json=graph_params)
# print(response.text)



# create pixel
create_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/mygraph"
post_data = {
    "date": date,
    "quantity": input("How many hours did you study today? ")
}
response = requests.post(url=create_pixel_endpoint, json=post_data, headers=headers)
print(response.text)


# update pixel
# update = {
#     "quantity": "5"
# }
# update_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/mygraph/{date}"
# response = requests.put(url=update_pixel_endpoint, json=update, headers=headers)
# print(response.text)



# delete pixel
# delete_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/mygraph/{date}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
