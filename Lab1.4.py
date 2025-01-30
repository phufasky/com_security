from pwn import *

host = '172.26.201.109'
port = 1111

r = remote(host, port)

def hex_to_byte(hex_str):
    return bytes.fromhex(hex_str)

def xor_byte(bytes1, bytes2):
    return bytes(a ^ b for a, b in zip(bytes1, bytes2))

response = r.recvline().decode('utf-8')
r.sendline(b'4')
print(response+'4')

question = r.recvline().decode('utf-8')
print(question)

response = r.recvline().decode('utf-8')
print(response)
cipherText_hex = response.split(":")[1].strip()
cipherText_byte = hex_to_byte(cipherText_hex)
print(cipherText_byte)

response = r.recvline().decode('utf-8')
print(response)
otp_hex = response.split(":")[1].strip()
otp_byte = hex_to_byte(otp_hex)
print(otp_byte)

plaintext_bytes = xor_byte(cipherText_byte, otp_byte)
plaintext = plaintext_bytes.decode('utf-8') 

print("Recovered Plaintext:",plaintext)

r.sendline(plaintext.encode('utf-8'))

response = r.recvline().decode('utf-8').strip()
print(response)
