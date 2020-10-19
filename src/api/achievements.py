from models import User


class Achievement:
    def __init__(self, user: User):
        self.user = user

    def achieved(self) -> bool:
        pass

    def process(self):
        pass


class EarlyBird(Achievement):
    ICON = "🌅"

    pass


class Helpful(Achievement):
    ICON = "🤝"
    pass
