from pwn import *

def test(s1, s2):
    for i in range(len(s1)-len(s2)):
        x = xor(s1[i:i+len(s2)], s2)
        if all(c in string.printable for c in x):
            print x

ct = '49380d773440222d1b421b3060380c3f403c3844791b202651306721135b6229294a3c3222357e766b2f15561b35305e3c3b670e49382c295c6c170553577d3a2b791470406318315d753f03637f2b614a4f2e1c4f21027e227a4122757b446037786a7b0e37635024246d60136f7802543e4d36265c3e035a725c6322700d626b345d1d6464283a016f35714d434124281b607d315f66212d671428026a4f4f79657e34153f3467097e4e135f187a21767f02125b375563517a3742597b6c394e78742c4a725069606576777c314429264f6e330d7530453f22537f5e3034560d22146831456b1b72725f30676d0d5c71617d48753e26667e2f7a334c731c22630a242c7140457a42324629064441036c7e646208630e745531436b7c51743a36674c4f352a5575407b767a5c747176016c0676386e403a2b42356a727a04662b4446375f36265f3f124b724c6e346544706277641025063420016629225b43432428036f29341a2338627c47650b264c477c653a67043e6766152a485c7f33617264780656537e5468143f305f4537722352303c3d4379043d69797e6f3922527b24536e310d653d4c33696c635474637d0326516f745e610d773340306621105a7361654e3e392970687c2e335f3015677d4b3a724a4659767c2f5b7c16055a126820306c14315d6b59224a27311f747f336f4d5974321a22507b22705a226c6d446a37375761423a2b5c29247163046d7e47032244377508300751727126326f117f7a38670c2b23203d4f27046a5c5e1532601126292f577776606f0c6d0126474b2a73737a41316362146e581d7c1228717664091c'.decode('hex')
salt = "WeAreDe1taTeam"

ct = xor(salt, ct)
       
l = [[] for i in range(30)]
for i in range(0, 30):
    for j in range(i, len(ct), 30):
        l[i].append(ct[j])
     
for i in l:
    print repr(''.join(i)), '\n\n'

m = l[0]
     
l2 = [[] for i in range(len(string.printable))]
for i in range(len(string.printable)):
    for j in range(len(m)):
        x = xor(string.printable[i], m[j])
        l2[i].append(x)
    
for j in l2:
    print ''.join(j)
    
for j in l2:
    x = ''.join(j)
    if all(c in string.printable for c in x):
        print x    
    
for x in string.printable:
    y = bin(ord(x))[2:]
    print x, '0'*(8-len(y))+y
    
    
key = ['*']*30    
    
for x, i in enumerate(l):
    print x, repr(''.join(i)), '\n\n'
    
key[0] = '1'
key[1] = 'v'
key[2] = 'l'
key[4] = 'u'
key[5] = 'm'
key[6] = 'v'
key[7] = 't'
key[9] = 'O'
key[10] = 'o'
key[12] = 'n'
key[13] = 'u'
key[14] = 't'
key[15] = 'g'
key[16] = 'u'
key[17] = 'n'
key[19] = 'o'
key[21] = 'O'
key[22] = 't'
key[23] = 'g'
key[24] = 'm'
key[26] = 'c'
key[27] = 'l'
''.join(key)
xor(ct, ''.join(key))    

key[11] = ' '
key[25] = '0'
key[18] = ' '    
key[0] = '_'
key[8] = 'O'
key[11] = ' '
key[29] = 'S'
key[28] = ' '
key[25] = '0'
key[18] = ' '
key[11] = '&'
key[15] = '&'
key[9] = 'j'
key[18] = 't'
key[23] = '0'
key[20] = 'j'
key[11] = '1'
xor(ct, key)
key = 'de1ctf{W3lc0m3tOjo1nu55un1ojOt3m0cl3W}'
pt = 'In faith I do not love thee with mine eyes,For they in thee a thousand errors note;But tis my heart that loves what they despise,Who in despite of view is pleased to dote.Nor are mine ears with thy tongues tune delighted;Nor tender feeling to base touches prone,Nor taste, nor smell, desire to be invitedTo any sensual feast with thee alone.But my five wits, nor my five senses canDissuade one foolish heart from serving thee,Who leaves unswayed the likeness of a man,Thy proud heart`s slave and vassal wretch to be.Only my plague thus far I count my gain,That she that makes me sin awards me pain.'
