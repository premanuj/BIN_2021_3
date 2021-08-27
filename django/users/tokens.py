from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int) -> str:
        return super()._make_hash_value(user, timestamp)

activation = UserToken()