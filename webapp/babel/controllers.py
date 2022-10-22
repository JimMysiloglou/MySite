from flask import Blueprint, session, redirect, url_for, request

babel_blueprint = Blueprint(
    'babel',
    __name__,
    url_prefix="/babel"
)

@babel_blueprint.route('/<string:locale>')
def index(locale):
    session['locale'] = locale
    next_link = request.args.get('next')
    return redirect(next_link) if next_link else redirect(url_for('main.index'))