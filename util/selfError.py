class InputError(Exception):
    def __init__(self,ErrorInfo) -> None:
        super().__init__(self)
        self.error = ErrorInfo
    def __str__(self) -> str:
        return self.error