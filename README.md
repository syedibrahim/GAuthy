# GAuthy

---
Cli based Google Authenticator TOTP Generator

## Prerequisites

---
1. Requires **Python 3.6+**
2. Install requirements from _**requirements.txt**_
```commandline
pip install -r requirements.txt
```
3.Install **zbar** package
```commandline
pip install zbar
```
For mac user
```commandline
brew install zbar
```
## How to

---
### To generate TOTP using Authenticator Key
```commandline
python gauthy -k YOURAUTHKEYHERE
python gauthy --key YOURAUTHKEYHERE
```
### To generate TOTP using Authenticator QR code Image
```commandline
python gauthy -q path/to/image
python gauthy --qr path/to/image
```
### For help
```commandline
 python gauthy --help
```
