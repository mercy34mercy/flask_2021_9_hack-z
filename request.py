import requests
import json


def req():
    json_t = requests.get("https://prettygirl.azurewebsites.net/url")

    #json = json
    print(json_t.text)
    json_dict = json.loads(json_t.text)

    print(json_dict["top_key"])
    

req()