from urllib.parse import urlparse
from urllib.parse import parse_qs
from datetime import datetime

import pyotp
import pyqrcode
import typer
from pyzbar.pyzbar import decode
from PIL import Image


class GenTotp:
    @staticmethod
    def gen_totp(auth_key):
        try:
            # generating TOTP codes with PyOTP
            totp = pyotp.TOTP(auth_key)
            time_remaining = totp.interval - datetime.now().timestamp() % totp.interval
            return totp, time_remaining
        except Exception as err:
            typer.echo("Error: Could not decode provided Auth Key -")
            typer.echo(err)
            raise typer.Exit(code=1)

    @staticmethod
    def decode_qr_code(file):
        try:
            decode_qr = decode(Image.open(file))
            qr_text = decode_qr[0].data.decode('ascii')
            totp = pyotp.parse_uri(qr_text)
            time_remaining = totp.interval - datetime.now().timestamp() % totp.interval
            return totp, time_remaining
        except Exception as err:
            typer.echo("Error: Could not decode provided QR code Image-")
            if str(err) == "list index out of range":
                typer.echo("Image does not contain QR code")
            else:
                typer.echo(err)
            raise typer.Exit(code=1)

        # parsed_url = urlparse(qr_text)
        # try:
        #     captured_value = parse_qs(parsed_url.query)['secret'][0]
        #     return captured_value
        # except KeyError:
        #     typer.echo("No secret found in provided google authenticator QR code")
        #     raise typer.Exit(code=1)
