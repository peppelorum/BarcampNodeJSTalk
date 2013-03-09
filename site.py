from flask import Flask
app = Flask(__name__)

import requests

from flask import make_response, render_template

from auth import requires_auth
from utils import get_secret_filepath


@app.route('/')
@requires_auth
def hello():
    return "Hello World!"


@app.route('/file/<filename>')
@requires_auth
def retrieve_file(filename=''):
    abs_filename = get_secret_filepath(filename)
    resp = make_response()
    resp.headers['X-Accel-Redirect'] = abs_filename
    return resp


@app.route('/offline/')
@requires_auth
def offline():
    return render_template('offline.html'), 200


@app.route('/calc/<thing>/')
def calc(thing):
    print 'HSJKHAK JAHJKA  ADHK'
    r = requests.get('http://localhost:8020/calc/'+ thing +'/')
    print r.content
    return r.content
    # return HttpResponse(r.text, mimetype=r.headers.get('content-type'))


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8010)
