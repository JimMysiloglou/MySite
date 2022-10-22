import logging
import click
import os

log = logging.getLogger(__name__)




def register(app):

    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language."""
        if os.system('pybabel extract -F babel/babel.cfg -k _l -o babel/messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system(f'pybabel init -i babel/messages.pot -d webapp/translations -l {lang}'):
            raise RuntimeError('init command failed')
        os.remove('babel/messages.pot')

    @translate.command()
    def update():
        """Update all languages."""
        if os.system('pybabel extract -F babel/babel.cfg -k _l -o babel/messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel update -i babel/messages.pot -d webapp/translations'):
            raise RuntimeError('update command failed')
        os.remove('babel/messages.pot')

    @translate.command()
    def compile():
        """Compile all languages."""
        if os.system('pybabel compile -d webapp/translations'):
            raise RuntimeError('compile command failed')
