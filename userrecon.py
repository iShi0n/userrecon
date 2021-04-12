import requests


class Result:
    def __init__(self, exists: bool, status_code: int, username: str) -> None:
        self.exists = exists
        self.status_code = status_code
        self.username = username

class UserRecon:
    def __init__(self, username) -> None:
        self.username = username

    def check_all(self):
        functions = list(filter(lambda item: (item.startswith("check_") and item != "check_all"), dir(self)))
        functions = [getattr(self, f) for f in functions]
        
        for f in functions:
            ...

    def check_facebook(self) -> bool:
        response = requests.get("https://m.facebook.com/"+self.username)
        
        return Result(True if response.status_code == 200 else False, response.status_code, self.username)

    def check_tiktok(self) -> bool:
        response = requests.get("https://www.tiktok.com/@"+self.username)
        
        return Result(True if response.status_code == 200 else False, response.status_code, self.username)

