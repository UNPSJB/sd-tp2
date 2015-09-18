import sys
from flask import Flask, render_template, request
import gevent
from gevent.pywsgi import WSGIServer
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)
from webbrowser import open_new_tab
from thread import start_new_thread
from functools import partial


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


def event():
    while True:
        yield 'data: ' + json.dumps(random.rand(1000).tolist()) + '\n\n'
        gevent.sleep(0.2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream/', methods=['GET', 'POST'])
def stream():
    return Response(event(), mimetype="text/event-stream")

@app.route('/agregar_usuario/', methods=["GET", "POST"])
def agregar_usuario():

    if request.method == 'POST':
        import ipdb; ipdb.set_trace()

    return render_template('agregar_usuario.html')

def abrir(url):
    from time import sleep
    sleep(1)
    print "Vamos a abrir"
    open_new_tab(url)

def main():
    start_new_thread(abrir, ('http://localhost:5000/', ))
    app.run(debug=True)

if __name__ == '__main__':
    print sys.version
    main()
