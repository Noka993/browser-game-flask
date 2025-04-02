from flask_restx import Namespace, Resource, fields
from backend.models import Player
from backend.core.database import db
from flask_jwt_extended import create_access_token

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
    

@auth_namespace.route("/login")
class Login(Resource):
    @auth_namespace.expect(login_schema)
    def post(self):
        player = Player.query.filter_by(
            username=auth_namespace.payload["username"]
        ).first()
        if not player:
            return {"message": "User not found"}, 404
        if player.password != auth_namespace.payload["password"]:
            return {"message": "Invalid credentials"}, 401
        
        access_token = create_access_token(identity=player.id)
        return {"access_token": access_token}, 200