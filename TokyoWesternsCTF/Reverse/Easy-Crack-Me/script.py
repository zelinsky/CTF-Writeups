# coding: utf-8
import sys
flag = ['*'] * 0x27
def p():
    print ''.join(flag)
    
flag[0:6] = 'TWCTF{'
flag[-1] = '}'
flag[31] = '4'
flag[23] = '2'
flag[12] = '7'
flag[11] = '8'
flag[7] = 'f'
flag[0x25] = '5'
p()

    

# Loop1
# loop through 'a-f', find first occurance, got to next letter, add 1 to count of that letter/index
# count number of occurences of '012...def', store count at rpb - 0xe0
#strcmp edx=num of chars, rdi=string, esi=substring

h = '0123456789abcdef'
c = '3220321331131223'
d = {}
for i in range(len(h)):
    d[h[i]] = int(c[i])

print "Loop 1: Counts"
print d
    
testflag = "TWCTF{00011224445567778889abbbcddeefff}"
print testflag

# for each index, (for i = 0..3, sub_index = index*4+6+i, add byte to var_1a8h (starts at 0), xor var_1a4h (starts at 0) with byte)
# var_1a8h is sum of 4 bytes, var_1a4h is xor of 4 bytes
print "\nLoop2:\nIndexes\nSum Xor"
for i in range(8):
    var_1a8h = 0
    var_1a4h = 0
    for j in range(4):
        x = (i*4)+6+j
        sys.stdout.write(str(x) + ' ')
 	var_1a8h += ord(testflag[x])
	var_1a4h ^= ord(testflag[x])
    print '\n', hex(var_1a8h), hex(var_1a4h)
#Sums at rbp-0x160
#Xors at rbp-0x140
    
# for each index, (for i = 0...3, sub_index = index+6+i*8, add byte to var_198h (starts at 0), xor byte with var_194h (starts at 0))
print "\nLoop3:\nIndexes\nSum Xor"
for i in range(8):
    var_198h = 0
    var_194h = 0
    for j in range(4):
	x = i+6+(j*8)
        sys.stdout.write(str(x) + ' ')
        var_198h += ord(testflag[x])
	var_194h ^= ord(testflag[x])
    print '\n', hex(var_198h), hex(var_194h)
#Sums at rbp-0x120
#Xors at rbp-0x100

#Answers at 0x400f40
l2sums = [0x015e, 0x00da, 0x012f, 0x0131, 0x0100, 0x0131, 0x00fb, 0x0102]
l2xors = [0x52, 0x0c, 0x01, 0x0f, 0x5c, 0x05, 0x53, 0x58]
l3sums = [0x0129, 0x0103, 0x012b, 0x0131, 0x0135, 0x010b, 0x00ff, 0x00ff]
l3xors = [0x01, 0x57, 0x07, 0x0d, 0x0d, 0x53, 0x51, 0x51]


# Loop4
#Memory at 0x400fc0
#80: a-f
#ff: 0-9

alpha = {0: 1,
 1: 1,
 2: 0,
 3: 1,
 4: 0,
 5: 0,
 6: 0,
 7: 0,
 8: 1,
 9: 0,
 10: 0,
 11: 1,
 12: 1,
 13: 0,
 14: 0,
 15: 1,
 16: 0,
 17: 0,
 18: 1,
 19: 0,
 20: 1,
 21: 1,
 22: 0,
 23: 0,
 24: 0,
 25: 0,
 26: 1,
 27: 0,
 28: 0,
 29: 0,
 30: 1,
 31: 0}


# Loop5

for i in range(16):
    print (i+3)*2
    print ''
    
# Compare those indexes to 0x488

from z3 import *
s = Solver()
flag = [ BitVec('b%i' % i, 32) for i in range(0, 39)]
s.add(flag[0] == ord('T')) 
s.add(flag[1] == ord('W')) 
s.add(flag[2] == ord('C')) 
s.add(flag[3] == ord('T')) 
s.add(flag[4] == ord('F')) 
s.add(flag[5] == ord('{')) 
s.add(flag[-1] == ord('}'))
for i in range(8):
    indexes = []
    for j in range(4):
        x = (i*4)+6+j
        indexes.append(x)
    s.add(flag[indexes[0]] + flag[indexes[1]] + flag[indexes[2]] + flag[indexes[3]] == l2sums[i])
    s.add(flag[indexes[0]] ^ flag[indexes[1]] ^ flag[indexes[2]] ^ flag[indexes[3]] == l2xors[i])
    
for i in range(8):
    indexes = []
    for j in range(4):
        x = i+6+(j*8)
        indexes.append(x)
    s.add(flag[indexes[0]] + flag[indexes[1]] + flag[indexes[2]] + flag[indexes[3]] == l3sums[i])
    s.add(flag[indexes[0]] ^ flag[indexes[1]] ^ flag[indexes[2]] ^ flag[indexes[3]] == l3xors[i])
    
for i in range(6, 38):
    if alpha[i-6]:
        s.add(flag[i] >= 97)
        s.add(flag[i] <= 102)
    else:
        s.add(flag[i] >= 48)
        s.add(flag[i] <= 57)
        

cs = {'a': 1, 'c': 1, 'b': 3, 'e': 2, 'd': 2, 'f': 3, '1': 2, '0': 3, '3': 0, '2': 2, '5': 2, '4': 3, '7': 3, '6': 1, '9': 1, '8': 3}

counters = []
for idx, val in enumerate(h):
    counters.append(IntVector('count'+val, 40))
    
for counter in counters:
    s.add(counter[0] = 0)

for idx,  counter in enumerate(counters):
    s.add(counter[0] == 0)
    for i in range(39):
        s.add(If(flag[i]==ord(h[idx]),counter[i+1]==counter[i]+1,counter[i+1]==counter[i]))
    s.add(counter[39] == cs[h[idx]])

s.check()
mod = s.model()
flag_plain = ''
for i in range(39):
    x = mod[flag[i]].as_long()
    flag_plain += chr(x)
    
print flag_plain
