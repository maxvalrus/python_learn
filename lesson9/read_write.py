import datetime

def read_file(file):
    try:
        with open(file, encoding="utf-8") as handle:
            print(handle.read())
    except Exception as e:
        print(e)

def write_file(file, data, mode="a"):
    try:
        with open(file, mode=mode, encoding="utf-8") as handle:
            handle.write(data)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    write_file("test.txt", str(datetime.datetime.now()) + " Запись в файл \n", "a")
    read_file("test.txt")
