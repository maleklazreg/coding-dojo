from flask import Flask   # type: ignore
app=Flask(__name__)

app.secret_key="key243"
DATABASE = "users_bd"