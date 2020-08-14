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
        return graph_rr()
    elif feature == 'mm_c':
        return graph_c()

if __name__ == '__main__':
    app.run(threaded=True,port=5000)