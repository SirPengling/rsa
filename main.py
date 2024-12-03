
def rsa_encrypt(string, p, q, e):
    output = []
    for i in string:
        output.append(pow(ord(i), int(e), int(p) * int(q)))
    return output
def rsa_decrypt(input, p, q, e):
    # m = pow(c, d, n)
    output = ""
    for i in range(len(input)):
        output += chr(pow(input[i], pow(e, -1, (p - 1) * (q - 1)), p * q))
    return output
if __name__ == "__main__":
    # if input("Encrypt or decrypt?").lower() == "encrypt":
    #     print(rsa_encrypt(input("\nMessage to encrypt: "), input("\nLarge prime 1: "), input("\nLarge prime 2: "), input("\nEncryption exponent: ")))
    print(f"Encrypted: {rsa_encrypt('Hi!', 61, 53, 17)}")
    print(f"Decrypted: {rsa_decrypt([3000, 3179, 1853], 61, 53, 17)}")