import os
from flask import Flask
from config import DevelopmentConfig
from routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    register_routes(app)

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=app.config["DEBUG"], port=port)