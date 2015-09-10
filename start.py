from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        "base.html",
        title="Hola mundo",
        variable="Una variable",
    )


@app.route('/agregar_usuario/', methods=["GET", "POST"])
def agregar_usuario():

    if request.method == 'POST':
        print request.form
    return render_template('agregar_usuario.html')


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
