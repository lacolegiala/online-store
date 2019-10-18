## Installing the app

First, create Python virtual environment.

`python3 -m venv venv`

Next, activate it.

`source venv/bin/activate`

Install dependencies.

`pip install -r requirements.txt`

If you face this error when installing dependencies

`ld: library not found for -lssl`

try this:

```bash
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
```
Then try to install dependencies again.



