def rsa_encrypt(string, n, e):
  output = []
  for i in string:
    output.append(pow(ord(i), int(e), int(n)))
  return output

def rsa_decrypt(input, p, q, e):
  # m = pow(c, d, n)
  output = ''
  for i in range(len(input)): 
    output += chr(pow(input[i], pow(int(e), -1, (int(p) - 1) * (int(q) - 1)), int(p) * int(q)))
  return output
