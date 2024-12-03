# RSA Encrypt/Decrypt
Encrypt or Decrypt using RSA encryption.
### Usage
`./cli.exe [command] [message] [n] [e]`
#### Commands
* `encrypt`: encrypt a message
* `decrypt`: decrypt a message
#### Message
Message must be a string.
#### public / private key
* for `encrypt`: N = p * q
* for `decrypt`: two arguments p and q, both of which are large primes
