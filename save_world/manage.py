import os
from flask.cli import FlaskGroup
from application import create_app

app = create_app("production")

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    print("db url = {}".format(app.config['SQLALCHEMY_DATABASE_URI']))
    app.db.drop_all()
    app.db.create_all()
    app.db.session.commit()

if __name__ == "__main__":
    cli()
