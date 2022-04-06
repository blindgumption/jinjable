""" jinjable/clija/cli.py 
"""

import typer 
from clija import app


@app.callback(invoke_without_command=True)
def main(configfile: str = typer.Option(None,
        "-c", "--configfile")
) -> None:
    if configfile:
        typer.echo(f'config file is {configfile}')
    else:
        typer.echo('no config file')


## end of file 