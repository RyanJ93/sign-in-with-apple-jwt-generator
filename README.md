# Sign in with Apple JWT generator

A simple CLI script that allows you to generate the JWT token required by the sign in with Apple's API.

## Usage

First you need to install all the required dependencies: you can install them from the requirements.txt file running the following command in the project's main directory:
```bash
pip install -r requirements.txt
```
You may need to use pip3 rather than pip according to your Python environment, please note that this script requires Python version 3.7 or greater to work.

Once dependencies have been installed you can launch the `main.py` script in your CLI, here's the list of the required arguments:

- *--team_id*: The team ID.
- *--key_id*: The key ID provided by Apple.
- *--private_key*: The path to the file containing the private key provided by Apple (*.p8).
- *--client_id*: The client ID.
- *--out_dir*: The path to the directory where the file containing the JWT token will be saved in.

Based upon this great and useful [repo by addisonwebb](https://github.com/addisonwebb/Apple-JWT-Generator).
