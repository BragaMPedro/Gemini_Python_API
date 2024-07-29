from typing import TypedDict, Optional

class Response(TypedDict, total=False):
    dialogue_and_narration: Optional[str]
    inner_thoughts: Optional[str]
    debug: Optional[bool]
    user: Optional[dict]

class ResponseDTO:
    """
    DTO para armazenar a resposta do modelo.
    """

    def __init__(self, text: Optional[str] = None, thoughts: Optional[str] = None, debug: Optional[bool] = None):
        """
        Inicializa um objeto ResponseDTO.

        Args:
            text: Diálogos e narração da resposta.
            thoughts: Pensamentos internos do modelo.
            debug: Indica se a resposta está em modo de depuração.
        """

        self.text = text
        self.thoughts = thoughts
        self.debug = debug

    def __init__(self, response: Response):
        """
        Inicializa um objeto ResponseDTO a partir de um objeto Response.

        Args:
            response: Um objeto Response.
        """
        self.text = response.get('dialogue_and_narration')
        self.thoughts = response.get('inner_thoughts')
        self.debug = response.get('debug')
        self.user = response.get('user')
