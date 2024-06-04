from flask import Flask, request, jsonify
from requests import post, exceptions
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)
cors = CORS(app)
target_url = 'https://8c8dd3eb21bac6.lhr.life/'

@app.route('/', methods=['POST'])
def proxy():
    print("[proxy] Received request at /")
    data = request.get_json()

    try:
        print(f"[proxy] Relaying request to {target_url}")
        response = post(target_url, json=data)
        sentiment = json.loads(response.content.decode("utf-8"))
        print(f"[proxy] Received response: {sentiment}")
 
        db_data = {
            'Data': data,
            'Sentiment': sentiment
        }
        
        doc_ref = db.collection('SentimentAnalysis').document()
        doc_ref.set(db_data)

        print("Data stored in FireStore Collection with Document ID: ", doc_ref.id)
        return sentiment

    except exceptions.RequestException as e:
        print(f"[proxy] Error occured")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
