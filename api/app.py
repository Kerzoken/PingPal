from flask import Flask
from api.views.users import users_bp
from api.views.messages import messages_bp
from api.models import db

from api import config

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"


swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(messages_bp, url_prefix='/messages')
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
