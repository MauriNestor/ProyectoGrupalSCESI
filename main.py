from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/juego')
def juego():
    return render_template('juego.html')

@app.route('/opciones')
def opciones():
    return render_template('opciones.html')


if __name__ == '__main__':
    app.run(debug=True)
