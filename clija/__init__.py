""" jinjable/clija/__init__.py 
"""

import typer
app = typer.Typer()
app_name = "clija"

# any @app functions need to be inmported here
# from jinjable.clija.cli import main
from clija.cli import main


def run():
    app(prog_name=app_name)

# end of file