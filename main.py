from sys import path
from flask import Flask, Blueprint
from .api import api


app = Flask(__name__)


blueprint_app = Blueprint('todo', __name__, url_prefix='/api')
api.init_app(blueprint_app)

app.register_blueprint(blueprint_app)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)