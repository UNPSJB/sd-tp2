import sys
from flask import Flask, render_template, request, Response
import werkzeug.serving

import gevent
from gevent.pywsgi import WSGIServer
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)
from webbrowser import open_new_tab
from thread import start_new_thread
from functools import partial
from datetime import datetime


@app.route('/')
def index():
    return render_template(
        "base.html",
        title="Hola mundo",
        variable="Una variable",
    )

@app.route('/js')
def js():
    return render_template("js.html")



@app.route('/agregar_usuario/', methods=["GET", "POST"])
def agregar_usuario():

    if request.method == 'POST':
        import ipdb; ipdb.set_trace()

    return render_template('agregar_usuario.html')

@app.route('/sse')
def sse():
    return render_template('sse.html')

def event():
    while True:
        msg = 'data: %s \n\n' % datetime.now()
        yield msg
        gevent.sleep(0.2)


@app.route('/stream/', methods=['GET', 'POST'])
def stream():
    return Response(event(), mimetype="text/event-stream")


@werkzeug.serving.run_with_reloader
def main():
    app.debug = True

    ws = WSGIServer(('', 5000), app)
    ws.serve_forever()


if __name__ == '__main__':
    print sys.version
    main()
