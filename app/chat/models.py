import json
from typing import TypedDict, Optional


class Response(TypedDict, total=False):
    dialogue_and_narration: Optional[str]
    inner_thoughts: Optional[str]
    debug: Optional[bool]
    user: Optional[dict]

# The `ResponseDTO` class in Python defines attributes for text, thoughts, debug, and user, with
# methods for initialization and JSON conversion.


class ResponseDTO:

    def __init__(self, text: Optional[str] = None, thoughts: Optional[str] = None, debug: Optional[bool] = None):
        """
        This Python function initializes an object with optional text, thoughts, and debug attributes.

        :param text: The `text` parameter in the `__init__` method is a string that represents some text
        data. It has an optional type annotation `Optional[str]`, which means it can either be a string
        or `None` if no value is provided
        :type text: Optional[str]
        :param thoughts: The `thoughts` parameter in the `__init__` method is a string that represents
        any thoughts or additional information related to the object being initialized. It is an
        optional parameter, meaning it can be provided when creating an instance of the class, but it
        defaults to `None` if not specified
        :type thoughts: Optional[str]
        :param debug: The `debug` parameter in the `__init__` method is an optional boolean parameter.
        It is used to specify whether debugging information should be displayed or not. If `debug` is
        set to `True`, additional debugging information may be printed or logged during the execution of
        the program. If `
        :type debug: Optional[bool]
        """
        self.text = text
        self.thoughts = thoughts
        self.debug = debug

    def __init__(self, response: Response):
        """
        This Python function initializes attributes based on a ResponseDTO object.

        :param response: The `response` parameter is expected to be an object of type `Response`. It is
        used to initialize the attributes `text`, `thoughts`, `debug`, and `user` of the class instance.
        The `response` object is expected to have the following keys: `dialogue_and_narration`, `inner_thoughts`, `debug`, `user`
        :type responseDTO: ResponseDTO
        """
        self.text = response.get('dialogue_and_narration')
        self.thoughts = response.get('inner_thoughts')
        self.debug = response.get('debug')
        self.user = response.get('user')

    def toJsonStr(self):
        """
        The `toJson` function converts an object to a JSON string using the object's `__dict__` attribute.
        :return: The `toJson` method is returning a JSON representation of the object using the `json.dumps`
        function.
        """
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ResponseDTO):
            return obj.__dict__
        return super().default(obj)
