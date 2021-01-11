from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "嗯呀ヽ(○^㉨^)ﾉ♪"
@app.route("/test")
def test():
    return "this is test"
if __name__=="__main__":
    app.run()

