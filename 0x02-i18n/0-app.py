#!/usr/bin/env python3
"""Create a single / route and an index.html template"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """func that displays the page 0-index.html"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
