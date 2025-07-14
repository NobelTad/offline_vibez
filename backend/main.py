from flask import Flask, jsonify
from googleapiclient.discovery import build
from flask_cors import CORS
from search import youtube_search
app = Flask(__name__)
CORS(app)
@app.route('/api', methods=['GET'])
def return_json():
    data = {
        "message": "Hello from Flask!",
        "status": "success",
        "code": 200
    }

    return jsonify(youtube_search("pop out of your party"))

if __name__ == '__main__':
    app.run(debug=True)
