from datetime import datetime

import pyotp


class GenTotp:
    @staticmethod
    def gen_totp(auth_key):
        # generating TOTP codes with PyOTP
        totp = pyotp.TOTP(auth_key)
        time_remaining = totp.interval - datetime.now().timestamp() % totp.interval
        return totp, time_remaining
