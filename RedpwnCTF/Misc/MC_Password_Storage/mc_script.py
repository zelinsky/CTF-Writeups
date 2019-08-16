from Crypto.Util.number import *

with open('enc_password', 'r') as f:
    enc_password_bits = f.read().strip()

with open('key', 'r') as f:
    key_bits = f.read().strip()
   
len(enc_password_bits) 
len(key_bits)
      
192 / 11
x = 18
        
def bit_xor(a, b):
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

    
for i in range(len(key_bits)):
    if i != 0:
        key_bits = key_bits[1:] + key_bits[0]
    key_stretch = key_bits * x
    p_bits = bit_xor(enc_password_bits, key_stretch)
    p_dec = int(p_bits, 2)
    password = long_to_bytes(p_dec)
    print password

