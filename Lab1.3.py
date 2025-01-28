from pwn import *

host = '172.26.201.109'
port = 1111

r = remote(host, port)

def find_key(ciphertext, hint):
    for i in range(len(ciphertext) - len(hint) + 1):  
        guess = ciphertext[i : i + len(hint)]
        print(guess)

        key = (ord(guess[0]) - ord(hint[0])) % 26  
        print("Key: ",key)
        
        match=True
        for g,h in zip(guess, hint):
            decrypt_char =chr((ord(g) - ord('a') - key) % 26 + ord('a'))
            print("decrypt char:",decrypt_char)
            if decrypt_char != h:
                match=False
                break
        if match==True:
            return key
    
def decrypt(cipherText,key):
    result =""
    k = int(key)
    for char in cipherText:
        decrypt_char =chr((ord(char) - ord('a') - k) % 26 + ord('a'))
        result += decrypt_char
    return result

response = r.recvline().decode('utf-8')
r.sendline(b'3')
print(response+'3')

question = r.recvline().decode('utf-8')
print(question)

response = r.recvline().decode('utf-8')
print(response)
cipherText = response.split(':')[1].strip()
print(repr(cipherText))

response = r.recvline().decode('utf-8')
print(response)

response = r.recvline().decode('utf-8')
print(response)
hint = response.split(':')[1].strip()
print(repr(hint))

key = find_key(cipherText, hint)
print("Key:",key)

answer= decrypt(cipherText,key)
print(answer)

r.sendline(answer.encode('utf-8'))

response = r.recvline().decode('utf-8')
print(response)