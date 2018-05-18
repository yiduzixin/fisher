"""
Created by 逗蛆 on 2018/5/7

"""
from flask import Flask
from app.models.book import db

__author__ = "逗蛆"


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
