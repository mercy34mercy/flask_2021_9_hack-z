import requests
import json

from requests.api import get


def req(qua,num):
    json_t = requests.post("https://beautifulgirl-ronauziko.herokuapp.com/url",json = {"quali":qua,"num":num})
    json_dict = json.loads(json_t.text)

    top_key =json_dict["top_key"]
    get_key = json_dict["get_key"]
    # print(top_key)
    # print(get_key)
    a = (top_key,get_key)
    #print(a)

    return a                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            