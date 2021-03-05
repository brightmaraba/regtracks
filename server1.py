from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return ("Hello World, this is Flask")


@app.route("/abc", methods=['GET'])
def abc():
    return ("Hello World, this is abc")

if __name__ == "__nmain__":
    app.run(host="127.0.0.1:5000")