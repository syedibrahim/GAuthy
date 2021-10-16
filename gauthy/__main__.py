import time
from datetime import datetime, timedelta

import click
import typer
from gen_totp import GenTotp

app = typer.Typer(help="CLI tool to generate google authenticator TOTP.")


@app.command()
def generate(auth_key: str = typer.Option(..., "--key", "-k")):
    try:
        while True:
            click.clear()
            totp, validity = GenTotp.gen_totp(auth_key)
            prev_totp = typer.style(
                f"{totp.at(for_time=datetime.now() - timedelta(seconds=30))}", fg=typer.colors.RED, dim=True)
            curr_totp = typer.style(
                f"{totp.now()}", fg=typer.colors.BRIGHT_GREEN, bold=True)
            next_totp = typer.style(
                f"{totp.at(for_time=datetime.now() + timedelta(seconds=30))}", fg=typer.colors.BLUE, dim=True)
            typer.echo(f"PREV\t\tCURRENT\t\tNEXT")
            typer.echo(f"{prev_totp}\t\t{curr_totp}\t\t{next_totp}")
            with typer.progressbar(
                    range(int(validity)), label="Token Validity") as progress:
                for value in progress:
                    time.sleep(1)
            time.sleep(0.05)
    except KeyboardInterrupt:
        typer.echo("Goodbye...")
        exit(0)


if __name__ == '__main__':
    app(prog_name="GAuthy")
