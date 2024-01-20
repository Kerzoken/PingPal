from flask import Flask
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from .views.users import users_bp
from .views.messages import messages_bp
from . import config
from .db import db

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)
migrate.init_app(app, db)

app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(messages_bp, url_prefix='/messages')


SWAGGER_URL = "/swagger"
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    "/static/swagger.json",
    config={
        'app_name': 'PingPal API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
