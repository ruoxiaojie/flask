from flask import Flask
app = Flask(__name__)

from .views import account

app.register_blueprint(account.ac)