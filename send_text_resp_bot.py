from flask import Flask, request
import requests

app = Flask(__name__)

# ATENÇÃO - NINGUÉM ALÉM DE VOCÊ DEVE SABER ESSE TOKEN
BOT_TOKEN = "SEU_TOKEN_AQUI"  # NÃO SUBIR PARA O GITHUB

@app.route('/nova-mensagem', methods=["POST"])
def new_message():
    # pegar a mensagem que o telegram enviou
    body = request.json
    app.logger.info(f"Chegou uma nova mensagem: {body}")
    # enviar mensagem respondendo o usuário
    enviar_mensagem("Sua resposta aqui!!", body)
    # falar para o telegram que tudo ocorreu bem :)
    return {"ok": True}

def enviar_mensagem(texto, body):
    endpoint = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": body['message']['chat']['id'],
        "text": texto,
    }
    requests.get(endpoint, params)

