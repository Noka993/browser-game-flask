from flask_restx import Namespace, Resource, fields
from backend.models import Player
from backend.core.database import db

auth_namespace = Namespace(
    "auth", description="A namespace for authentication related operations"
)

login_schema = auth_namespace.model(
    "User",
    {
        "username": fields.String(required=True, description="The username"),
        "password": fields.String(required=True, description="The password"),
    },
)

@auth_namespace.route("/register")
class Register(Resource):
    @auth_namespace.expect(login_schema)
    def post(self):
        data = auth_namespace.payload
        username = data["username"]
        password = data["password"]

        new_player = Player(username=username, password=password)
        db.session.add(new_player)
        db.session.commit()

        return {"message": f"User {username} registered successfully"}, 201