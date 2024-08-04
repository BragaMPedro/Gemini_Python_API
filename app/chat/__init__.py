from gem_model.resources import (getEnv, createModel)

model = createModel()
scenario = getEnv('SCENARIO')

chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": [
            f"(considere a seguinte cena como a cena inicial: {scenario})",
        ],
    },
    {
        "role": "model",
        "parts": [
            "(Entendido, a interpretação vai continuar a partir da cena inicial descrita)",
        ],
    }
])
