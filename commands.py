#!/usr/bin/python3

import click
from flask.cli import with_appcontext

from extensions import db


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()


# @click.command(name='create_admin')
# @with_appcontext
# def create_admin():
#     admin = Admin(
#         firstname='John',
#         lastname='Doe',
#         email='johndoe@x.com',
#         password_hash='pbkdf2:sha256:150000$nZ0avKRm$d27c8501a7b0df8c7059f669c33ec46957109151872c817b9d08ec41324d744d'
#     )

#     db.session.add(admin)
#     db.session.commit()


# @click.command(name='create_speech')
# @with_appcontext
# def create_speech():
#     speech1 = CeoAddress(
#         ceo_welcome_address='This is important dummy data. Do not delete only upload a new version'
#     )
#     db.session.add(speech1)

#     speech2 = speech1 = CeoAddress(
#         ceo_welcome_address='This is important dummy data. Do not delete only upload a new version'
#     )
#     db.session.add(speech2)

#     db.session.commit()
