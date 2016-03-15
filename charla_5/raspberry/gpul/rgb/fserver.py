from flask import Flask
from flask.ext.cors import CORS
from colorlib import RgbLed

app = Flask(__name__)
CORS(app)

r = RgbLed()

@app.route('/color/<int:red>/<int:green>/<int:blue>')
def hello_world(red, green, blue):
    r.setColor(red, green, blue)
    return 'Ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
