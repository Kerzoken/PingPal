from flask import Flask
from api.views.users import users_bp
from api.models import db

from api import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(users_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
