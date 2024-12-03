
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
