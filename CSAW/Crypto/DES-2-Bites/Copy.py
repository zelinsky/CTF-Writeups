from Crypto.Cipher import DES
import binascii

IV = '13371337'

def getNibbleLength(offset):	
	if str(offset)[0]=="9":
		return len(str(offset))+1
	return len(str(offset))

def duck(aChr):
	try:
		return int(aChr)
	except:
		return "abcdef".index(aChr)+11

def encodeText(plainText,offset):
	hexEncoded = plainText.encode("hex")
	nibbleLen = getNibbleLength(offset)
	output = ""
	for i in range(0,len(hexEncoded),2):
		hexByte = hexEncoded[i:i+2]
		try: 
			output += str(duck(hexByte[0]) + offset).rjust(nibbleLen,"0")
			output += str(duck(hexByte[1]) + offset).rjust(nibbleLen,"0")
		except:
			continue
	return output

def padInput(input):
	bS = len(input)/8
	if len(input)%8 != 0:
		return input.ljust((bS+1)*8,"_")	
	return input
	
def desEncrypt(input,key):
	cipher = DES.new(key, DES.MODE_OFB, IV)
	msg = cipher.encrypt(padInput(input))
	return msg
		
def createKey(hex,fileName):
	with open(fileName, 'wb') as f:
		f.write(binascii.unhexlify(hex))

def createChallenge():
	createKey("0101010101010101","key1")
	createKey("FEFEFEFEFEFEFEFE","key2")

	plainText = open('test.txt').read()
	key1 = open('key1').read()

	byte = desEncrypt(plainText,key1)
	key2 = open('key2').read()

	cipherText = desEncrypt(byte,key2)
        print repr(cipherText)
	cipherText = encodeText(binascii.hexlify(cipherText),9133337)
	with open('test.enc', 'w') as f:
		f.write(cipherText)

weakkeys = ['01'*8, 'fe'*8, 'e0'*4+'f1'*4, '1f'*4+'0e'*4, '0'*16, 'f'*16, 'e1'*4+'f0'*4, '1e'*4+'0f'*4]
weakkeys = map(lambda x: x.decode('hex'), weakkeys)


with open('test.enc', 'r') as f:
    enc_data = f.read().strip()
    
dec_data = ''
    
l = 'abcdef'
    
for i in range(0, len(enc_data), 8):
    h = int(enc_data[i:i+8])
    h -= 9133337
    if h >= 11:
        h = l[h-11]
    else:
        h = str(h)
    dec_data+=h
    

ct = dec_data.decode('hex').decode('hex')


for k1 in weakkeys:
    for k2 in weakkeys:
	c1 = DES.new(k1, DES.MODE_OFB, IV)
	c2 = DES.new(k2, DES.MODE_OFB, IV)
        apt = c2.decrypt(ct)
        pt = c1.decrypt(apt)
        print k1.encode('hex'), k2.encode('hex'), pt
