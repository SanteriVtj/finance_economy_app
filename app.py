from flask import Flask, render_template, request
import os
from money_mul import *
import numpy as np
import pandas as pd

app = Flask(__name__)
# port = int(os.environ.get("PORT", 5000))


@app.route('/')
def index():
    feature = 'mm_rr'
    plot = create_plot(feature)
    return render_template('index.html', plot=plot)

@app.route('/graph/', methods=['GET', 'POST'])
def change_fetures():
    return create_plot(request.args['selected'])

def create_plot(feature):
    if feature == 'mm_rr':
        with open('plots/graph_rr.txt', 'r') as f:
            return json.load(f)
    elif feature == 'mm_c':
        with open('plots/graph_c.txt', 'r') as f:
            return json.load(f)

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0')