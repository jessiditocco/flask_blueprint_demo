from flask import Flask
from blue.api.routes import mod
from blue.site.routes import mod

app = Flask(__name__)

app.register_blueprint(site.routes.mod) 
# with blueprints, you can specify where the blueprint starts
# so i will have everything related to api only relative /api route
app.register_blueprint(api.routes.mod, url_prefix='/api')