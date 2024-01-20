from flask import Flask
from api.views.auth import auth_bp
from api.models import db

from api import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
