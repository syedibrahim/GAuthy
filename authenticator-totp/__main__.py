import pyotp


def main():
    # generating TOTP codes with PyOTP
    totp = pyotp.TOTP('base32secret3232')
    print(totp.now())


if __name__ == '__main__':
    main()
