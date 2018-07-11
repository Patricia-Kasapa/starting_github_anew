from flask import Flask
app = Flask(__name__)

@app.route('/y')
def y():
    return ("My First Raspberry Website")

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
