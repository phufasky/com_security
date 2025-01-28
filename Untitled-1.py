from pwn import *

host = '172.26.201.109'
port = 2223

r = remote(host, port)

chal_bytes = r.recvuntil(b': ')
chal_str = chal_bytes.decode('utf-8')
print(chal_str)

num1 = r.recvuntil(b",")
num1_str = num1.decode('utf-8')
num1_str = num1_str[:-1]
print(num1_str)

num2 = r.recvline()
num2_str = num2.decode('utf-8')
num2_str = num2_str[:-1]
print(num2_str)

num1 = int(num1_str)
num2 = int(num2_str)
answer = num1 + num2
print(answer)


# Send the answer back to the server
r.sendline(str(answer))
print("Answer sent to server.")

# Receive the server's response
response = r.recvline().decode('utf-8')
print("Server Response:", response)

r.close

