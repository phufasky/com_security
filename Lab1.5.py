from pwn import *

host = '172.26.201.109'
port = 1111

r = remote(host, port)

def encrypt (plainText,key):
    answer = ""
    for p,k in zip(plainText,key):
        print (p+":",k)
        plainText = ord(p)-ord('a')
        key = ord(k)-ord('a')
        print('plainText=',plainText,'Key=',key)
        x = (plainText+key)%26
        print(x)
        encrypt_char = chr(x+ord('a'))
        print(encrypt_char)
        answer += encrypt_char
    return answer

def decrypt(cipherText,key):
    answer = ""
    for c,k in zip(cipherText,key):
        print (c+":",k)
        cipherText = ord(c)-ord('a')
        key = ord(k)-ord('a')
        print('cipherText:',cipherText,' key:',key)
        x = (cipherText+26-key)%26
        print(x)
        decrypt_char = chr(x+ord('a'))
        print(decrypt_char)
        answer += decrypt_char
    return answer

response = r.recvline().decode('utf-8')
r.sendline(b'5')
print(response + '5')

question = r.recvline().decode('utf-8')
print(question)

blank = r.recvlines(9)

response = r.recvline().decode('utf-8')
print(response)
plainText = response.split(':')[1].strip()

response = r.recvline().decode('utf-8')
print(response)
key = response.split(':')[1].strip()

answer = encrypt(plainText,key)
print("CipherText:",answer)

r.sendline(answer.encode('utf-8'))
response=r.recvline().decode('utf-8').strip()
print(response)

response=r.recvline().decode('utf-8').strip()
print(response)
cipherText = response.split(':')[1].strip()

response=r.recvline().decode('utf-8').strip()
print(response)
key = response.split(':')[1].strip()

answer = decrypt(cipherText,key)
print(answer)

r.sendline(answer.encode('utf-8'))
response=r.recvline().decode('utf-8').strip()
print(response)







