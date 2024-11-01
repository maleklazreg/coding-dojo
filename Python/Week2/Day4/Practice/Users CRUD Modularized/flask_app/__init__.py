from flask import Flask  # type: ignore
app = Flask(__name__)
app.secret.key = "key23"
DATABASE  = "crud_schema"