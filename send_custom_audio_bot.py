from flask import Flask, request
from gtts import gTTS  # necessário instalar a lib! (pip3.8 install --user gTTS)
import requests

app = Flask(__name__)

# ATENÇÃO - NINGUÉM ALÉM DE VOCÊ DEVE SABER ESSE TOKEN
BOT_TOKEN = "SEU_TOKEN_AQUI"  # NÃO SUBIR PARA O GITHUB

@app.route('/nova-mensagem', methods=["POST"])
def new_message():
    # pegar a mensagem que o telegram enviou
    body = request.json
    app.logger.info(f"Chegou uma nova mensagem: {body}")
    # processar a mensagem
    nome_audio_salvo = text_to_speech(body)
    # enviar mensagem respondendo o usuário
    if nome_audio_salvo:
        enviar_audio(nome_audio_salvo, body)
    else:
        enviar_mensagem("Só trabalho com textos, xuxu", body)
    # falar para o telegram que tudo ocorreu bem :)
    return {"ok": True}

def text_to_speech(body):
    if 'text' in body['message']:
        AUDIO_FILE_NAME = "audio.mp3"
        texto = body['message']['text']
        speech = gTTS(text=texto, lang="pt-br", slow=False)
        speech.save(AUDIO_FILE_NAME)
        return AUDIO_FILE_NAME

def enviar_audio(nome_arquivo, body):
    with open(nome_arquivo, 'rb') as audio:
        endpoint = f'https://api.telegram.org/bot{BOT_TOKEN}/sendAudio'
        params = {"chat_id":  body["message"]["from"]["id"] }
        requests.get(endpoint, params, files={'audio': audio})

def enviar_mensagem(texto, body):
    endpoint = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": body['message']['chat']['id'],
        "text": texto,
    }
    requests.get(endpoint, params)

