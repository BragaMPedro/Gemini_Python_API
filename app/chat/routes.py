# app/chat/routes.py
import json
from flask import Flask
from flask import request, jsonify

from . import chat
from .services import enviar_mensagem
from .models import CustomJSONEncoder

app = Flask(__name__)
base_route = "/chat"


@app.get(base_route)
def get_chat():
    # getChatHistory

    return jsonify("Requisição completada; endpoint em construção"), 200


@app.post(base_route)
def post_chat():
    data = request.get_json()
    prompt = data.get('prompt')

    try:
        res_json = enviar_mensagem(chat, prompt)
        return res_json.toJsonStr(), 200
    except Exception as e:
        return jsonify({'req_data': prompt, 'error': str(e)}), 500


@app.delete(f'{base_route}/renew')
def reset_chat():
    # chat = model.start_chat(history=[])

    return jsonify("Requisição completada; endpoint em construção"), 204
