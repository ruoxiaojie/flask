from flask import Flask
app = Flask(__name__)

from .views import account
from .views import login

app.register_blueprint(account.ac)
app.register_blueprint(login.bc)