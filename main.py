from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/feedback")
def welcome():
    return "<p>hope you guys enjoyed the session!!</p>"

app.run(debug=True)