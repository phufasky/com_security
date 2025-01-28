from pwn import *

host = '172.26.201.109'
port = 1111

r = remote(host, port)

def decrypt(cipherText,key):
    result =""
    k = int(key)
    for char in cipherText:
        decrypt_char =chr((ord(char) - ord('a') - k) % 26 + ord('a'))
        result += decrypt_char
    return result

def encrypt(plainText,key):
    result =""
    k = int(key)
    for char in plainText:
        encrypt_char =chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        result += encrypt_char
    return result

response = r.recvline().decode('utf-8')
r.sendline(b'1')
print(response+'1')

question = r.recvline().decode('utf-8')
print(question)

c = r.recvuntil(b': ')
cipherText = r.recvline().decode('utf-8')
cipherText = cipherText.strip()
print("Cipher Text:",cipherText)

k = r.recvuntil(b':')
key = r.recvline().decode('utf-8')
print("Key:",key)

answer = decrypt(cipherText,key)
print(answer)

r.sendline(answer.encode('utf-8'))

response = r.recvline().decode('utf-8')
print(response)

p = r.recvuntil(b': ')
plainText = r.recvline().decode('utf-8')
plainText = plainText.strip()
print("Plain Text:",plainText)

k = r.recvuntil(b':')
key = r.recvline().decode('utf-8')
print("Key:",key)

answer = encrypt(plainText,key)
print(answer)

r.sendline(answer.encode('utf-8'))

response = r.recvline().decode('utf-8')
print(response)

r.close


