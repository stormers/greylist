#!/usr/bin/env python
from flask import Flask, g, jsonify
from flask.ext.script import Manager
from api.app import create_app
from api.models import db, User, Server

manager = Manager(create_app)


@manager.command
def createdb(testdata=False):
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        if testdata:
            servers = ['Server01', 'Server02']
            for name in servers:
                c = Server(name=name)
                db.session.add(c)

            u = User(username='storm', password='storm')
            db.session.add(u)
            db.session.commit()


@manager.command
def adduser(username):
    """Register a new user."""
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt='Confirm: ')
    if password != password2:
        import sys
        sys.exit('Error: passwords do not match.')
    db.create_all()
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    print('User {0} was registered successfully.'.format(username))


@manager.command
def test():
    from subprocess import call
    call(['nosetests', '-v',
          '--with-coverage', '--cover-package=api', '--cover-branches',
          '--cover-erase', '--cover-html', '--cover-html-dir=cover'])


if __name__ == '__main__':
    manager.run()

