class UserDoesNotExistException(Exception):

    def __init__(self, login: str):
        self.login = login
        super().__init__(f"User with login '{login}' does not exist.")
