from pwn import *

host = '172.26.201.109'
port = 1111

r = remote(host, port)

def encrypt(plainText, mapping):
    return "".join(mapping.get(char, char) for char in plainText)

def decrypt(cipherText, reverse_mapping):
    return "".join(reverse_mapping.get(char, char) for char in cipherText)

response = r.recvline().decode('utf-8')
r.sendline(b'2')
print(response + '2')

question = r.recvline().decode('utf-8')
print(question)

blank = r.recvline()

originaAlpha = r.recvline().decode('utf-8').strip()
print(originaAlpha)

blank = r.recvlines(2)

mapAlpha = r.recvline().decode('utf-8').strip()  
print(mapAlpha)

blank = r.recvline()

response = r.recvline().decode('utf-8').strip()  
print(response)
plainText = response.split(": ")[1].strip()  
print("Plain Text:",plainText)

mapping = {orig: map for orig, map in zip(originaAlpha, mapAlpha)}
reverse_mapping = {x: y for y, x in mapping.items()}
#print(mapping)
cipherText = encrypt(plainText, mapping)
print("Answer:",cipherText)

r.sendline(cipherText.encode('utf-8'))

p = r.recvuntil(b': ')
response = r.recvline().decode('utf-8').strip()  
print(response)

x = r.recvuntil(b': ').decode('utf-8')
#print(x)

cipherText = response.split(": ")[1].strip()  
print("CipherText:",cipherText)

answer = decrypt(cipherText, reverse_mapping)
print("Answer:",answer)

r.sendline(answer.encode('utf-8'))

response = r.recvline().decode('utf-8')
print(response)

r.close()
