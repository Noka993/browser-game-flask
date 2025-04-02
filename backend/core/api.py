from flask_restx import Api
from backend.apis.auth import auth_namespace

api = Api(
    title="Strategic game",
    version="1.0",
    description="API for a strategic game",
    authorizations={
        'APIKeyHeader': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }
)

api.add_namespace(auth_namespace, path='/auth')