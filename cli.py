import click
from flask.cli import with_appcontext
from flask import Blueprint
from app import app, db
from app.models import User

bp_cli = Blueprint('cli', __name__, cli_group=None)


@bp_cli.cli.command('init_db')
def initialize_database():
    """Initialize the SQLite database."""
    db.create_all()
    click.echo('Initialized the SQLite database!')


@bp_cli.cli.command('drop')
def drop_db():
    """Drops database tables"""
    if click.prompt("Are you sure you want to lose all your data?"):
        db.drop_all()
        click.echo('SQLite database was dropped!')


@bp_cli.cli.command('create')
def create_db():
    """Delete database """
    if click.prompt("Do you create a database?"):
        db.create_all()


@bp_cli.cli.command('recreate')
def recreate():
    """Rebuild the database """
    if click.prompt("Do you want to rebuild the database?"):
        db.drop_all()
        db.create_all()


@bp_cli.cli.command("add_user")
@click.argument("name", type=str)
@click.option('--email', prompt='Your email',
              help='The person email', type=str)
@click.option('--password', prompt='Your password',
              help='The person password', type=str)
def create_super_user(name, email, password):
    """Add user"""
    print("Now creating user", name, password)
    new_user = User(username=name, email=email, password=password)
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    click.echo(f'Account created for {name} !')


@bp_cli.cli.command()
@with_appcontext
@click.argument('parameter')
def echo(parameter):
    """
    Echo function with parameter
    """
    print("echo {}".format(parameter))
