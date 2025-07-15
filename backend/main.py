from flask import Flask, jsonify
from flask_cors import CORS
from search import youtube_search

app = Flask(__name__)
CORS(app)

@app.route('/api/<path:query>/', methods=['GET'])
def return_json(query):
    return jsonify(youtube_search(query))

if __name__ == '__main__':
    app.run(debug=True)
