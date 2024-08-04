import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content


def getEnv(env_name: str):
    """
    The function `getEnv` retrieves an environment variable value, handling specific exceptions related
    to secret not found or notebook access errors.

    :param env_name: The `getEnv` function takes in a parameter `env_name` which is a string
    representing the name of the environment variable that you want to retrieve
    :type env_name: str
    :return: The function `getEnv` is returning the value of the environment variable with the name
    specified in the `env_name` parameter.
    """
    try:
        env = os.getenv(env_name)
    except env.SecretNotFoundError as e:
        print(f'Secret not found\n\nThis expects you to create a secret named {
              env_name} contained in a .env file')
        raise e
    except env.NotebookAccessError as e:
        print(f'You need to grant this notebook access to the {env_name}')
        raise e
    except Exception as e:
        # unknown error
        print(f"There was an unknown error. Ensure you have a secret {
              env_name} stored in .env and it's valid")
        raise e

    return env


def createModel():
    """
    The `createModel` function sets up a generative model with specified preset configurations and system
    instructions.
    :return: The `createModel` function is returning a GenerativeModel object that is configured with
    the specified API key, generation configuration, safety settings, and system instructions.
    """
    api_key = getEnv('GOOGLE_API_KEY')
    system_instruction = getEnv('SYS_INSTRUCTIONS')

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest',
                                  generation_config=generationConfig,
                                  safety_settings=safetySettings,
                                  system_instruction=system_instruction
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
        enum=[],
        required=["dialogue_and_narration", "inner_thoughts", "debug", "user"],
        properties={
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
                enum=[],
                required=["name", "pronouns"],
                properties={
                    'name': content.Schema(
                        type=content.Type.STRING,
                    ),
                    'gender': content.Schema(
                        type=content.Type.STRING,
                    ),
                    'also_known_as': content.Schema(
                        type=content.Type.ARRAY,
                        items=content.Schema(
                            type=content.Type.STRING,
                        ),
                    ),
                    'pronouns': content.Schema(
                        type=content.Type.STRING,
                    ),
                    'appearance': content.Schema(
                        type=content.Type.ARRAY,
                        items=content.Schema(
                            type=content.Type.STRING,
                        ),
                    ),
                    'inferences': content.Schema(
                        type=content.Type.ARRAY,
                        items=content.Schema(
                            type=content.Type.OBJECT,
                            properties={
                                'confidence_on_inference': content.Schema(
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
