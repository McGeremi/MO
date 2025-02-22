from flask import Flask
from models.user import db
from routes.auth import auth_bp
from routes.imc import imc_bp
from routes.recipes import recipes_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(imc_bp, url_prefix='/imc')
app.register_blueprint(recipes_bp, url_prefix='/recipes')

if __name__ == '__main__':
    app.run(debug=True)
