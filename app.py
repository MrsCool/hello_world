from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "段晓勇"
@app.route("/test")
def test():
    return "this is test"
if __name__=="__main__":
    app.run()

