from flask import Flask, request
import os

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")
PHONE_ID = os.environ.get("PHONE_ID")
VERIFY_TOKEN = "negrute123"

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Token errado", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    print("Mensagem recebida:", request.get_json())
    return "ok", 200

@app.route("/")
def home():
    return "Bot Negrute Online!"

if __name__ == "__main__":
    app.run()
