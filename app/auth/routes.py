from flask import jsonify
from .resources import (
    UserLogin,
    UserLogoutAccess,
    UserLogoutRefresh,
    UserRegistration,
    AllUsers,
    TokenRefresh,
    SecretResource,
)


def initialize_routes(api):
    api.add_resource(UserRegistration, "/registration")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserLogoutAccess, "/logout/access")
    api.add_resource(UserLogoutRefresh, "/logout/refresh")
    api.add_resource(TokenRefresh, "/token/refresh")
    api.add_resource(AllUsers, "/users")
    api.add_resource(SecretResource, "/secret")

