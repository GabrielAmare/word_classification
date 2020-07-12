class CodeTemplate(str):
    _instances: dict = None

    def __init_subclass__(cls, **kwargs):
        cls._instances = {}

    def __new__(cls, content):
        if content in cls._instances:
            return cls._instances[content]
        else:
            instance = super().__new__(cls, content)
            cls._instances[content] = instance
            return instance
