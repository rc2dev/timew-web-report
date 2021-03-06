import flask
from flask import request, jsonify, render_template, redirect
import pandas as pd
from datetime import datetime
from tags import calculate_totals

app = flask.Flask(__name__)


@app.route('/api/totals', methods=['GET'])
def api_totals():
    return jsonify(calculate_totals())


@app.route('/', methods=['GET'])
def index():
    return redirect('/totals')


@app.route('/totals', methods=['GET'])
def view_totals():
    data = calculate_totals()
    df = pd.DataFrame.from_dict(data, orient='index')

    # Configure display
    df.fillna('-', inplace=True)
    df.sort_index(ascending=False, inplace=True)
    # Display '_all' and '_prod' first
    df = df[['_all', '_prod'] +
            [col for col in df if col not in ['_all', '_prod']]]

    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    return render_template('totals.html', tables=[df.to_html(classes=['table', 'table-striped', 'table-hover'])], time=time)
