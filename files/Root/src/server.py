import base64

from flask import Flask

app = Flask(__name__)

PATH_BASE64 = "L2Q5OWJhMjhiYzY4YjNjYjhlODc5MjdjZGEyNzE5ZWU5NDkwNmQ2MGEudHh0"
FLAG_BASE64 = "ZHhjdGZ7bjBfZzBidXN0ZXJfYW5kX2ZmdWZ9"


@app.route(base64.b64decode(PATH_BASE64).decode("utf-8"))
def flag():
    return base64.b64decode(FLAG_BASE64)


if __name__ == '__main__':
    app.run()
