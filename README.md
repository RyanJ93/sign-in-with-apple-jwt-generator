#Sign in with Apple JWT generator

A simple CLI script that allows you to generate the JWT token required by the sign in with Apple's API.

## Usage

Install the required dependency: `jwt`, then launch the `main.py` script in your CLI, here's the list of the required arguments:

- *--team_id*: The team ID.
- *--key_id*: The key ID provided by Apple.
- *--private_key*: The path to the file containing the private key provided by Apple (*.p8).
- *--client_id*: The client ID.
- *--out_dir*: The path to the directory where the file containing the JWT token will be saved in.

Based upon this great and useful [repo by addisonwebb](https://github.com/addisonwebb/Apple-JWT-Generator).

Requires Python 3.7+.
