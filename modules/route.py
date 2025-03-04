from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, decode_token, jwt_manager, create_refresh_token, set_access_cookies
from flask import jsonify, request
from flask_restful import Resource, reqparse
from modules import api, jwt, db, app


@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return ({"message": "expired token"}), 401

@jwt.invalid_token_loader
def handle_invalid(error):
    return ({"message": "invalid token", "error":error}), 401

api.add_resource()