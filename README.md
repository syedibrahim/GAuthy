# GAuthy

Cli based Google Authenticator TOTP Generator

## Prerequisites

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
###Usage:
```commandline
python gauthy [--key/-k Authenticator_Key|--qr/-q Path_To_Qr_Image] [--file/-f Storage_File] [--current/-c]
```
### To generate TOTP using Authenticator Key
```commandline
python gauthy -k YOURAUTHKEYHERE
python gauthy --key YOURAUTHKEYHERE
```
---
### To generate TOTP using Authenticator QR code Image
```commandline
python gauthy -q path/to/image
python gauthy --qr path/to/image
```
### To load TOTPs from text file
```commandline
python gauthy -f path/to/file
python gauthy --file path/to/file
```
### Other options
1. To display just current TOTP
- Use **_-c / --curent_** flag to display just current TOTP
- Example: 
```commandline
python gauthy -q path/to/image --current
python gauthy --key YOURAUTHKEYHERE -c
```
---
### For help
```commandline
 python gauthy --help
```
