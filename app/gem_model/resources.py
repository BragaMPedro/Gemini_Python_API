import os
import google.generativeai as genai
from google.generativeai import GenerativeModel
from google.ai.generativelanguage_v1beta.types import content

api_key = os.getenv('GOOGLE_API_KEY')
system_instruction = os.getenv('SYS_INSTRUCTIONS')

def configureGenai():
    genai.configure(api_key=api_key)

def getModel() -> GenerativeModel:
    configureGenai();
    model = genai.GenerativeModel(model_name = 'gemini-1.5-pro-latest',
                                generation_config = generationConfig,
                                safety_settings = safetySettings,
                                system_instruction = system_instruction
                              )
    return model

generationConfig = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
  "response_schema": content.Schema(
    type=content.Type.OBJECT,
    properties = {
      'response': content.Schema(
        type=content.Type.OBJECT,
        properties = {
          'dialogue_and_narration': content.Schema(
            type=content.Type.STRING,
          ),
          'inner_thoughts': content.Schema(
            type=content.Type.STRING,
          ),
          'debug': content.Schema(
            type=content.Type.BOOLEAN,
          ),
          'user': content.Schema(
            type=content.Type.OBJECT,
            properties = {
              'name': content.Schema(
                type=content.Type.STRING,
              ),
              'gender': content.Schema(
                type=content.Type.STRING,
              ),
              'also_known_as': content.Schema(
                type=content.Type.ARRAY,
                items = content.Schema(
                  type=content.Type.STRING,
                ),
              ),
              'pronouns': content.Schema(
                type=content.Type.STRING,
              ),
              'appearance': content.Schema(
                type=content.Type.ARRAY,
                items = content.Schema(
                  type=content.Type.STRING,
                ),
              ),
              'inferences': content.Schema(
                type=content.Type.ARRAY,
                items = content.Schema(
                  type=content.Type.OBJECT,
                  properties = {
                    'confidence': content.Schema(
                      type=content.Type.STRING,
                    ),
                    'description': content.Schema(
                      type=content.Type.STRING,
                    ),
                  },
                ),
              ),
            },
          ),
        },
      ),
    },
  ),
}

safetySettings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]