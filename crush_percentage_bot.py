from flask import Flask, request
import requests
import random

app = Flask(__name__)

# ATENÇÃO - NINGUÉM ALÉM DE VOCÊ DEVE SABER ESSE TOKEN
BOT_TOKEN = "SEU_TOKEN_AQUI"  # NÃO SUBIR PARA O GITHUB

@app.route('/nova-mensagem', methods=["POST"])
def new_message():
    # pegar a mensagem que o telegram enviou
    body = request.json
    app.logger.info(f"Chegou uma nova mensagem: {body}")
    # escolher um texto de resposta para a mensagem recebida
    resposta = montar_resposta(body)
    # enviar mensagem respondendo o usuário
    enviar_mensagem(resposta, body)
    # falar para o telegram que tudo ocorreu bem :)
    return {"ok": True}

def montar_resposta(body):
    if 'text' in body['message']:
        texto_recebido = body['message']['text']
        nome_usuario = body['message']['from']['first_name']
        porcentagem = random.randint(0, 100)
        if texto_recebido == '/start':
            return (
                "Olá!\n\n"
                "Quer saber o que o futuro guarda para você e a pessoa amada?\n"
                "Me mande o nome dela e lhe direi..."
            )
        return (
            f"Calculando amor entre *{nome_usuario}* & *{texto_recebido}*...\n\n"
            f"Chance de match: {porcentagem}%"
        )
    else:
        return "Chance de match: 0%"

def enviar_mensagem(texto, body):
    endpoint = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": body['message']['chat']['id'],
        "text": texto,
    }
    requests.get(endpoint, params)

