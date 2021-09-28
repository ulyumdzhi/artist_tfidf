from flask import Flask, render_template

from api.musicmatcher import rec_music
# from static.texts import HEADER

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Привет', 200

    # render_template('index.html', header=HEADER)

@app.route('/result', methods=['GET'])
def music_match():
    result = rec_music()
    return result, 200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)