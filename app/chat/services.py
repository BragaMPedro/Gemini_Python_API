from flask import json
from google.generativeai import ChatSession
from .models import ResponseDTO


def enviar_mensagem(chat: ChatSession, prompt: str):
    response_gem = chat.send_message(prompt)

    res_json = json.loads(response_gem.text)
    response_dto = ResponseDTO(res_json.get('response'))

    response_dto.text.replace('~', '\~') if hasattr(
        response_dto, 'text') else response_dto.text
    response_dto.thoughts.replace('~', '\~') if hasattr(
        response_dto, 'thoughts') else response_dto.thoughts

    return response_dto
