l = 99

enc_flag = 'vdDby72W15O2qrnJtqep0cSnsd3HqZzbx7io27C7tZi7lanYx6jPyb2nsczHuMec'.decode('base64')
flag = ''
  
for c in enc_flag:
    flag += chr(ord(c) - l)
    
print flag.decode('base64')
