from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # a simple page that says hello
    @app.get('/')
    def hello():
        return 'Hello, World!'

    return app
