from flask import Flask, render_template, redirect, Response

from tools.qiangji import parse_xls_to_json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/__webpack_hmr')
def npm():
    return redirect('http://localhost:8080/__webpack_hmr')


@app.route('/qj')
def qj():
    resp = Response(parse_xls_to_json())
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run(debug=True)
