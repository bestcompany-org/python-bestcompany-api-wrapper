class BestcompanyApi:
    def __init__(
        self,
        api_key: str = None,
        **kwargs
    ):
        self.config = {"api_key": api_key}

    def create(self, **kwargs):
        return self(**kwargs)

    @property
    def api_key(self):
        return self.config["api_key"]

    @api_key.setter
    def api_key(self, value):
        self.config["api_key"] = value
