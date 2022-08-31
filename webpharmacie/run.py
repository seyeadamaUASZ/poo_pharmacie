import click
from flask_frozen import Freezer

from app import app
from app import db


# define custom command 
@app.cli.command()
def build():
    freezer = Freezer(app)
    freezer.freeze()


if __name__ == "__main__":

    db.create_all()
    app.run() 