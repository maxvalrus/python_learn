import datetime
import json
import requests

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
    except Exception as e:
        print(e)

if __name__ == "__main__":
    #write_file("test.txt", str(datetime.datetime.now()) + " Запись в файл \n", "a")

    my_dict = {"name":"max", "pro":"coder", "age":30}
    write_file("my_dump.txt", json.dumps(my_dict), "w")
    str = read_file("my_dump.txt")
    dict_file = json.loads(str)
    print(type(dict_file))
    print(dict_file)
    requests.get("https://ya.ru")