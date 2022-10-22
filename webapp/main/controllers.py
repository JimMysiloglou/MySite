from flask import Blueprint, redirect, render_template, flash, url_for
from flask_babel import _

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/my_journey/')
def my_journey():
    return render_template('my_journey.html')

@main_blueprint.route('/blog/')
def blog():
    return redirect("https://jimmysiloglou.github.io/blog/")

@main_blueprint.route('/portfolio/')
def prortfolio():
    return redirect("https://jimmysiloglou.github.io/blog/")


@main_blueprint.route("/contact/")
def contact():
    
    return render_template("contact.html")

@main_blueprint.route("/contact_success/")
def contact_success():
    return render_template("contact_success.html")

@main_blueprint.app_errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403

@main_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@main_blueprint.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500