from rest_framework.authtoken.models import Token

def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        return Token.objects.create(user=instance)
    return None