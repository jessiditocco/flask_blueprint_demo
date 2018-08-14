from flask import Blueprint

# name a module and we need a name for it, site
# we also need to pass in the current module name
mod = Blueprint('site', __name__)


# with blue prints we use the name of the blue print when were inside of the blue print file

@mod.route('/homepage')
def homepage():
	return '<h1> you are on the homepage!!!</h1>'