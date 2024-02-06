from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/audio')
def audio():
    return render_template('audio.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
