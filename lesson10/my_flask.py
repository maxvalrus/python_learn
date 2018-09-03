from flask import Flask

app = Flask(__name__)


@app.route('/<txt>/')
def home(txt):
    #txt = txt + "!" if len(txt) > 6 else txt + "?"
    try:
        with open("D:/Github/python_learn/" + str(txt)) as handle:
            txt = "file open success!"
    except Exception:
        txt = "Failure!"
    return txt


if __name__ == "__main__":
    app.run()
