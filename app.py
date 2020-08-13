from flask import Flask
from flask import render_template
import os
from money_mul import *

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route('/')
def hello_world():
    plot = graph_rr()
    return render_template('index.html', plot=plot)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)