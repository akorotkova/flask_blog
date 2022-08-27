from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)


@app.route("/")
def home():
    return "Hello, Flask!"
