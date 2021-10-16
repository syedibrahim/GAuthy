import binascii
import time
from datetime import datetime, timedelta
from pathlib import Path

import click
import typer
from gen_totp import GenTotp

app = typer.Typer(help="CLI tool to generate google authenticator TOTP.")

auth_key_help = "Provide Authenticator Key for which TOTP needs to be generated"


@app.command()
def generate(auth_key: str = typer.Option(None, "--key", "-k", metavar="Authenticator_Key", help=auth_key_help),
             qr_code: Path = typer.Option(
                 None, "--qr", "-q",
                 exists=True,
                 file_okay=True,
                 dir_okay=False,
                 writable=False,
                 readable=True,
                 resolve_path=True,
             ),
             current: bool = typer.Option(False, "--current", "-c")):
    """
    Cli Tool to generate Google Authenticator TOTP

    Usage: python gauthy [--key/-k Authenticator_Key|--qr/-q Path_To_Qr_Image] [--current/-c]
    \f
    :param current:
    :param qr_code:
    :param auth_key:
    :return:
    """
    if (not auth_key and not qr_code) or (auth_key and qr_code):
        typer.echo("Error: Requires command line option either ['--key' / '-k'] or ['--qr' / '-q']")
        typer.echo("Usage: python gauthy [--key/-k Authenticator_Key|--qr/-q Path_To_Qr_Image] [--current/-c]")
        raise typer.Exit(code=1)
    try:
        while True:
            click.clear()
            if auth_key:
                totp, validity = GenTotp.gen_totp(auth_key)
            elif qr_code:
                totp, validity = GenTotp.decode_qr_code(qr_code)
            if current:
                typer.echo(f"{totp.now()}")
                typer.echo(f"Valid for: {round(validity,2)}s")
                raise typer.Exit()
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
    except binascii.Error as err:
        typer.echo("Error - Unable to generate TOTP")
        typer.echo(f"Exception type - binascii.Error \nError message - {err}")
        raise typer.Exit(code=1)


if __name__ == '__main__':
    app(prog_name="GAuthy")
