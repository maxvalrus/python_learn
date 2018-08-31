import datetime
import json
import requests
import re

def read_file(file):
    try:
        with open(file) as handle:
            return handle.read()
    except Exception as e:
        print(e)

def write_file(file, data, mode="a"):
    try:
        with open(file, mode=mode) as handle:
            handle.write(data)
            return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
# var №1
    # gt = requests.get("https://jsonplaceholder.typicode.com/comments")
    # if gt.status_code == 200:
    #     print("data received")
    # js = gt.json()
    # if write_file("comments.txt", str(js), "w"):
    #     print("file save")
    # print(js)

#var №2
    # js = read_file("comments.txt")
    # pre_dict = re.findall(r"{.+?}", js)
    # my_dict = dict()
    # for item in pre_dict:
    #     item = item.replace("'", "\"")
    #     my_dict.update(json.loads(item))
    # print(my_dict)

#var №3
    gt = requests.get("https://jsonplaceholder.typicode.com/comments")
    if gt.status_code == 200:
        js = gt.json()
        for item in js:
            print(item["name"], " - ", item["email"])

