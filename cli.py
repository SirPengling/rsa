from argparse import ArgumentParser, Namespace
import ast
from main import *

def encrypt(args):
  print(f"Encrypted: {rsa_encrypt(args.string, args.n, args.e)}")

def decrypt(args):
  print(f'Decrypted: {rsa_decrypt(ast.literal_eval(args.string), args.p, args.q, args.e)}')
  exit()

parser = ArgumentParser()

subparsers = parser.add_subparsers(help="Available commands")

encrypt_parser = subparsers.add_parser('encrypt')
encrypt_parser.add_argument('string')
encrypt_parser.add_argument('n')
encrypt_parser.add_argument('e')
encrypt_parser.set_defaults(func = encrypt)

decrypt_parser = subparsers.add_parser('decrypt')
decrypt_parser.add_argument('string')
decrypt_parser.add_argument('p')
decrypt_parser.add_argument('q')
decrypt_parser.add_argument('e')
decrypt_parser.set_defaults(func = decrypt)

args = parser.parse_args()
args.func(args)

print(rsa_encrypt(args.string, args.n, args.e))


