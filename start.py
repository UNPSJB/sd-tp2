from flas import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <html>
        <title>{titulo}</title>
    <head>
    </head>
    <body>
    {cuerpo}
    </body>
    </html>
    '''.format(titulo="Hola mundo", cuerpo="Hola mundo")


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
