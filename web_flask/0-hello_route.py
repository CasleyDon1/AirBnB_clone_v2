#!/usr/bin/python3
"""Starts a web flask application.

The application listens on 0.0.0.0 port 5000.
Routes:
	:/ Display 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
	"""Displays 'Hello HBNB!'"""


if __name == "__main__"
	app.run(host="0.0.0.0")
