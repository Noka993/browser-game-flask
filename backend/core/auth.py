from flask_jwt_extended import JWTManager
from backend.models import Player

jwt = JWTManager()


@jwt.user_identity_loader
def user_identity_lookup(user):
    print(user)
    return user


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return Player.query.filter_by(username=identity).one_or_none()
