from flask import Flask, request

app = Flask(__name__)

@app.route('/nova-mensagem', methods=["POST"])
def new_message():
    body = request.json
    app.logger.info(f"Chegou uma nova mensagem: {body}")
    return {"ok": True}

