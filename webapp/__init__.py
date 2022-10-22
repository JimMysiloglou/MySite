from flask import Flask
import os


def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)
    

    from .main import create_module as main_create_module
    from .babel import create_module as babel_create_module
    
    main_create_module(app)
    babel_create_module(app)

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

    

    return app