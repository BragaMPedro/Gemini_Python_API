#app/chat/routes.py
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.get('/chat')
def get_chat():
    return jsonify("chegou aqui tudo certinho"), 200

@app.post('/chat')
def post_chat(prompt: str):
  data = request.get_json()
  prompt = data.get('prompt')

  try:
    #   res_json = enviar_mensagem(prompt)

      return jsonify("Seu prompt foi: "+prompt), 200
  except Exception as e:
      return jsonify({'error': str(e)}), 500
