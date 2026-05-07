import os
def xor_logic(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

msg = input("Texto: ").encode()
key = os.urandom(len(msg))
print(f"Cifrado: {xor_logic(msg, key).hex()}\nDescifrado: {xor_logic(xor_logic(msg, key), key).decode()}")
