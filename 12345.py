from lesson10.flask import Flask

app = Flask(__name__)

@app.route('/<int:int1>&<int:int2>&<txt>/')
def home(int1, int2, txt):
    txt = txt + "!" if len(txt) > 6 else txt + "?"
    return "Summ: " + str((int1 + int2)) + " " + txt


if __name__ == "__main__":
    app.run()
