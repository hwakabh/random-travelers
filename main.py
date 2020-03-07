from flask import Flask, render_template, request
import gacha

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gacha', methods=['GET', 'POST'])
def gacha_result():
    result = gacha.get_country()
    return result

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
