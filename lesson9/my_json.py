import json

def read_file(file):
    with open(file) as f:
        return f.read()

def write_file(file, text, mode='w'):
    '''
    mode:
    w - all write files
    a - add string
    '''
    with open(file, mode=mode) as f:
        f.write(text)

if __name__ == "__main__":
    data = read_file("data.json")
    #print(data)
    obj = json.loads(data)
    #print("---------------" + obj["object"]["key"][0])
    obj["new"] = "secret"
    print(json.dumps(obj, sort_keys=True, indent=4))