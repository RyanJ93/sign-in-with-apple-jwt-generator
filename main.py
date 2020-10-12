from argparse import ArgumentParser
import jwt
import time


# Initialize the CLI arguments parser.
parser: ArgumentParser = ArgumentParser()
# Set up required arguments.
parser.add_argument('--team_id')
parser.add_argument('--key_id')
parser.add_argument('--private_key')
parser.add_argument('--client_id')
parser.add_argument('--out_dir')
# Parse user input.
args = parser.parse_args()
# Validate given arguments.
if not args.team_id:
    print('You must set a team ID!')
    exit(0)
if not args.key_id:
    print('You must set a key ID!')
    exit(0)
if not args.private_key:
    print('You must set a path to the private key file!')
    exit(0)
if not args.client_id:
    print('You must set a client ID!')
    exit(0)
# Generate a timestamp containing the maximum expire date allowed for the final JWT (6 months).
issued_timestamp: float = time.time()
expiration_timestamp: float = issued_timestamp + 15552000
# Load the private key from the given file.
with open(args.private_key, 'r') as file:
    private_key_contents: str = file.read()
# Generate the JWT.
jwt: str = jwt.encode({
    'iss': args.team_id,
    'iat': issued_timestamp,
    'exp': expiration_timestamp,
    'aud': 'https://appleid.apple.com',
    'sub': args.client_id
}, private_key_contents, algorithm='ES256', headers={
    'kid': args.key_id
})
if args.out_dir:
    # Write the generated JWT to a file (if a path has been given).
    destination_path: str = args.out_dir + '/loginWithApple.jwt'
    print('Saving JWT to ' + destination_path)
    with open(destination_path, 'w') as destination:
        destination.write(jwt.decode('ascii'))
    print('JWT generated and saved successfully!')
else:
    # Print out the generated JWT.
    print('JWT generated successfully! \n' + jwt.decode('ascii'))
