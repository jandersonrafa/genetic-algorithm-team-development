from flask import Blueprint, Flask, render_template
from flask_restful import Api
from server.api.GeneticApi import GeneticApi    

app = Flask(__name__, static_folder = "./static", template_folder = "./")
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route page
@app.route('/')
def hello_world():
  return render_template('index.html')

# Routes api rest
# prefix /api
app.register_blueprint(api_bp, url_prefix='/api')
api.add_resource(GeneticApi, '/genetic')

if __name__ == "__main__":
    app.run(debug=True)