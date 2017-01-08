from flask import Flask
from .bar import bar
from .foo import foo

def run():
    app = Flask(__name__)

    @app.route("/bar")
    def return_bar():
        return bar()

    @app.route("/foo")
    def return_foo():
        return foo()
    app.run(host='0.0.0.0')
    return app
