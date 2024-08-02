import os
import google.generativeai as genai
from google.generativeai import GenerativeModel
from google.ai.generativelanguage_v1beta.types import content

def getEnv(env_name: str):
  try:
    env = os.getenv(env_name)
  except env.SecretNotFoundError as e:
    print(f'Secret not found\n\nThis expects you to create a secret named {env_name} in Colab\n\nVisit https://makersuite.google.com/app/apikey to create an API key\n\nStore that in the secrets section on the left side of the notebook (key icon)\n\nName the secret {env_name}')
    raise e
  except env.NotebookAccessError as e:
    print(f'You need to grant this notebook access to the {env_name} secret in order for the notebook to access Gemini on your behalf.')
    raise e
  except Exception as e:
    # unknown error
    print(f"There was an unknown error. Ensure you have a secret {env_name} stored in Colab and it's a valid key from https://makersuite.google.com/app/apikey")
    raise e

  return env

def createModel() -> GenerativeModel:
  api_key = getEnv('GOOGLE_API_KEY')
  system_instruction = getEnv('SYS_INSTRUCTIONS')
  
  genai.configure(api_key=api_key)
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