import flask
from flask import request, jsonify
from subprocess import run
from tags import calculate_totals

app = flask.Flask(__name__)

@app.route('/api/totals', methods=['GET'])
def totals():
    return jsonify(calculate_totals())
