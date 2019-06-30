# Pytecode

### The Challenge
This reversing challenges was a fun one. We were given a file, [**pytecode**](Pytecode.zip), which contains Python byte code. Byte code is generated from compiling a Python script, and it is loaded into the Python run-time and interpreted by a virtual machine, which is a piece of code that reads each instruction in the byte code and executes whatever operation is indicated.

The file given contains byte code that is basically checking that certain aspects of the flag are true, and failing if they are false. Once we have all the requirements for the flag, we can figure out what it is.

The byte code is actually pretty easy to read and understand once you get the hang of it. All the operations either push something onto the stack, pop something off of the stack, perform an operation on stack values, or call a function with the arguments on the stack. It's all stack baby!


### Tools and References
I didn't use any tools for this challenge. I just went through the byte code line by line and reversed it by hand, and I used [**this**](https://docs.python.org/3/library/dis.html) as a reference for the instructions.


### Interpreting the Byte Code
Here is the pytecode file that was given along with what the byte code interprets to:
```assembly
C0rr3ct func:
  6           0 LOAD_CONST               1 ('Wow!!!You so best^_^')	# If the flag is correct, print and exit
              3 PRINT_ITEM          
              4 PRINT_NEWLINE       
              5 LOAD_CONST               0 (None)
              8 RETURN_VALUE        

Ch3cking func:						# START HERE: checks that the flag is correct
  8           0 LOAD_CONST               1 (0)
              3 STORE_FAST               1 (check)

  9           6 LOAD_GLOBAL              0 (ord)
              9 LOAD_FAST                0 (flag)
             12 LOAD_CONST               1 (0)
             15 BINARY_SUBSCR   			# flag[0]    
             16 CALL_FUNCTION            1		# ord(flag[0])
             19 LOAD_CONST               2 (52)
             22 BINARY_ADD          			# ord(flag[0])+52
             23 LOAD_GLOBAL              0 (ord)
             26 LOAD_FAST                0 (flag)	
             29 LOAD_CONST               3 (-1)			
             32 BINARY_SUBSCR       			# flag[-1]
             33 CALL_FUNCTION            1		# ord(flag[-1])
             36 COMPARE_OP               3 (!=)		# ord(flag[0])+52 != ord(flag[-1])
             39 POP_JUMP_IF_TRUE        78		# Jump to fail if true, we want previous statement (and the rest of the
							# comparison operations to be false)
             42 LOAD_GLOBAL              0 (ord)			
             45 LOAD_FAST                0 (flag)
             48 LOAD_CONST               3 (-1)				
             51 BINARY_SUBSCR       			# flag[-1]
             52 CALL_FUNCTION            1		# ord(flag[-1])
             55 LOAD_CONST               4 (2)
             58 BINARY_SUBTRACT     			# ord(flag[-1])-2
             59 LOAD_GLOBAL              0 (ord)
             62 LOAD_FAST                0 (flag)
             65 LOAD_CONST               5 (7)
             68 BINARY_SUBSCR       			# flag[7]
             69 CALL_FUNCTION            1		# ord(flag[7])
             72 COMPARE_OP               3 (!=)		# ord(flag[-1])-2 != ord(flag[7])
             75 POP_JUMP_IF_FALSE       88		# Jump past fail (keep checking) if false, go to 88

 10     >>   78 LOAD_GLOBAL              1 (F41l)
             81 CALL_FUNCTION            0
             84 POP_TOP             
             85 JUMP_FORWARD           752 (to 840)

 11     >>   88 LOAD_FAST                0 (flag)
             91 LOAD_CONST               5 (7)
             94 SLICE+2             			# flag[0:7]
             95 LOAD_CONST               6 ('ISITDTU')
             98 COMPARE_OP               3 (!=)		# flag[0:7] != 'ISITDTU'
            101 POP_JUMP_IF_FALSE      120		# Jump past exiting program (keep checking) if false

 12         104 LOAD_GLOBAL              2 (sys)
            107 LOAD_ATTR                3 (exit)
            110 LOAD_CONST               1 (0)
            113 CALL_FUNCTION            1
            116 POP_TOP             
            117 JUMP_FORWARD           720 (to 840)

 13     >>  120 LOAD_FAST                0 (flag)
            123 LOAD_CONST               7 (9)
            126 BINARY_SUBSCR       			# flag[9]
            127 LOAD_FAST                0 (flag)
            130 LOAD_CONST               8 (14)
            133 BINARY_SUBSCR       			# flag[14]
            134 COMPARE_OP               3 (!=)		# flag[9] != flag[14]
            137 POP_JUMP_IF_TRUE       180		# Jump to fail if true
            140 LOAD_FAST                0 (flag)
            143 LOAD_CONST               8 (14)
            146 BINARY_SUBSCR       			# flag[14]
            147 LOAD_FAST                0 (flag)
            150 LOAD_CONST               9 (19)
            153 BINARY_SUBSCR       			# flag[19]
            154 COMPARE_OP               3 (!=)		# flag[14] != flag[19]
            157 POP_JUMP_IF_TRUE       180		# Jump to fail if true
            160 LOAD_FAST                0 (flag)
            163 LOAD_CONST               9 (19)
            166 BINARY_SUBSCR       			# flag[19]
            167 LOAD_FAST                0 (flag)
            170 LOAD_CONST              10 (24)
            173 BINARY_SUBSCR       			# flag[24]
            174 COMPARE_OP               3 (!=)		# flag[19] != flag[24]
            177 POP_JUMP_IF_FALSE      193		# Jump past exiting program (keep checking) if false

 14     >>  180 LOAD_FAST                1 (check)
            183 LOAD_CONST              11 (1)
            186 INPLACE_ADD         
            187 STORE_FAST               1 (check)
            190 JUMP_FORWARD           647 (to 840)

 15     >>  193 LOAD_GLOBAL              0 (ord)	
            196 LOAD_FAST                0 (flag)
            199 LOAD_CONST              12 (8)
            202 BINARY_SUBSCR       			# flag[8]
            203 CALL_FUNCTION            1		# ord(flag[8])
            206 LOAD_CONST              13 (49)
            209 COMPARE_OP               3 (!=)		# ord(flag[8]) != 49
            212 POP_JUMP_IF_TRUE       235		# Jump to fail if true
            215 LOAD_FAST                0 (flag)
            218 LOAD_CONST              12 (8)
            221 BINARY_SUBSCR       			# flag[8]
            222 LOAD_FAST                0 (flag)
            225 LOAD_CONST              14 (16)
            228 BINARY_SUBSCR       			# flag[16]
            229 COMPARE_OP               3 (!=)		# flag[8] != flag[16]
            232 POP_JUMP_IF_FALSE      245		# Jump past fail (keep checking) if false

 16     >>  235 LOAD_GLOBAL              1 (F41l)
            238 CALL_FUNCTION            0
            241 POP_TOP             
            242 JUMP_FORWARD           595 (to 840)

 17     >>  245 LOAD_FAST                0 (flag)
            248 LOAD_CONST              15 (10)
            251 LOAD_CONST               8 (14)
            254 SLICE+3             			# flag[10:14]
            255 LOAD_CONST              16 ('d0nT')
            258 COMPARE_OP               3 (!=)		# flag[10:14] != 'd0nT'
            261 POP_JUMP_IF_FALSE      277		# Jump past exiting (keep checking) if false

 18         264 LOAD_FAST                1 (check)
            267 LOAD_CONST              11 (1)
            270 INPLACE_ADD         
            271 STORE_FAST               1 (check)
            274 JUMP_FORWARD           563 (to 840)

 19     >>  277 LOAD_GLOBAL              4 (int)
            280 LOAD_FAST                0 (flag)
            283 LOAD_CONST              17 (18)
            286 BINARY_SUBSCR       			# flag[18]
            287 CALL_FUNCTION            1		# int(flag[18])
            290 LOAD_GLOBAL              4 (int)
            293 LOAD_FAST                0 (flag)
            296 LOAD_CONST              18 (23)		
            299 BINARY_SUBSCR       			# flag[23]
            300 CALL_FUNCTION            1		# int(flag[23])
            303 BINARY_ADD          			# int(flag[18])+int(flag[23])
            304 LOAD_GLOBAL              4 (int)
            307 LOAD_FAST                0 (flag)
            310 LOAD_CONST              19 (28)
            313 BINARY_SUBSCR       			# flag[28]
            314 CALL_FUNCTION            1		# int(flag[28])
            317 BINARY_ADD          			# int(flag[18])+int(flag[23])+int(flag[28])
            318 LOAD_CONST               7 (9)
            321 COMPARE_OP               3 (!=)		# int(flag[18])+int(flag[23])+int(flag[28]) != 9
            324 POP_JUMP_IF_TRUE       347		# Jump to fail if true
            327 LOAD_FAST                0 (flag)
            330 LOAD_CONST              17 (18)
            333 BINARY_SUBSCR       			# flag[18]
            334 LOAD_FAST                0 (flag)
            337 LOAD_CONST              19 (28)
            340 BINARY_SUBSCR       			# flag[28]
            341 COMPARE_OP               3 (!=)		# flag[28] != flag[18])
            344 POP_JUMP_IF_FALSE      357		# Jump past fail (keep checking) if false

 20     >>  347 LOAD_GLOBAL              1 (F41l)
            350 CALL_FUNCTION            0
            353 POP_TOP             
            354 JUMP_FORWARD           483 (to 840)

 21     >>  357 LOAD_FAST                0 (flag)	
            360 LOAD_CONST              20 (15)
            363 BINARY_SUBSCR       			# flag[15]
            364 LOAD_CONST              21 ('L')
            367 COMPARE_OP               3 (!=)		# flag[15] != 'L'
            370 POP_JUMP_IF_FALSE      386		# Jump past exit (keep checking) if false

 22         373 LOAD_FAST                1 (check)
            376 LOAD_CONST              11 (1)
            379 INPLACE_ADD         
            380 STORE_FAST               1 (check)
            383 JUMP_FORWARD           454 (to 840)

 23     >>  386 LOAD_GLOBAL              0 (ord)
            389 LOAD_FAST                0 (flag)
            392 LOAD_CONST              22 (17)
            395 BINARY_SUBSCR       			# flag[17]
            396 CALL_FUNCTION            1		# ord(flag[17])
            399 LOAD_CONST              23 (-10)
            402 BINARY_XOR          			# ord(flag[17])^-10
            403 LOAD_CONST              24 (-99)
            406 COMPARE_OP               3 (!=)		# ord(flag[17])^-10 != -99
            409 POP_JUMP_IF_FALSE      422		# Jump past fail (keep checking) if false

 24         412 LOAD_GLOBAL              1 (F41l)
            415 CALL_FUNCTION            0
            418 POP_TOP             
            419 JUMP_FORWARD           418 (to 840)

 25     >>  422 LOAD_GLOBAL              0 (ord)
            425 LOAD_FAST                0 (flag)
            428 LOAD_CONST              25 (20)
            431 BINARY_SUBSCR       			# flag[20]
            432 CALL_FUNCTION            1		# ord(flag[20])
            435 LOAD_CONST               4 (2)
            438 BINARY_ADD          			# ord(flag[20])+2
            439 LOAD_GLOBAL              0 (ord)
            442 LOAD_FAST                0 (flag)
            445 LOAD_CONST              26 (27)
            448 BINARY_SUBSCR       			# flag[27]
            449 CALL_FUNCTION            1		# ord(flag[27])
            452 COMPARE_OP               3 (!=)		# ord(flag[20])+2 != ord(flag[27])
            455 POP_JUMP_IF_TRUE       502		# Jump to exit if true
            458 LOAD_GLOBAL              0 (ord)	
            461 LOAD_FAST                0 (flag)
            464 LOAD_CONST              26 (27)
            467 BINARY_SUBSCR       			# flag[27]
            468 CALL_FUNCTION            1		# ord(flag[27])
            471 LOAD_CONST              27 (123)
            474 COMPARE_OP               4 (>)		# ord(flag[27]) > 123
            477 POP_JUMP_IF_TRUE       502		# Jump to exit if true
            480 LOAD_GLOBAL              0 (ord)
            483 LOAD_FAST                0 (flag)
            486 LOAD_CONST              25 (20)
            489 BINARY_SUBSCR       			# flag[20]
            490 CALL_FUNCTION            1		# ord(flag[20])
            493 LOAD_CONST              28 (97)
            496 COMPARE_OP               0 (<)		# ord(flag[20]) < 97
            499 POP_JUMP_IF_FALSE      515		# Jump past exit (keep checking) if false

 26     >>  502 LOAD_FAST                1 (check)
            505 LOAD_CONST              11 (1)
            508 INPLACE_ADD         
            509 STORE_FAST               1 (check)
            512 JUMP_FORWARD           325 (to 840)

 27     >>  515 LOAD_GLOBAL              0 (ord)
            518 LOAD_FAST                0 (flag)
            521 LOAD_CONST              26 (27)
            524 BINARY_SUBSCR       			# flag[27]
            525 CALL_FUNCTION            1		# ord(flag[27])
            528 LOAD_CONST              29 (100)
            531 BINARY_MODULO       			# ord(flag[27])%100
            532 LOAD_CONST               1 (0)
            535 COMPARE_OP               3 (!=)		# ord(flag[27])%100 != 0
            538 POP_JUMP_IF_FALSE      551		# Jump past fail (keep checking) if false

 28         541 LOAD_GLOBAL              1 (F41l)
            544 CALL_FUNCTION            0
            547 POP_TOP             
            548 JUMP_FORWARD           289 (to 840)

 29     >>  551 LOAD_FAST                0 (flag)
            554 LOAD_CONST              30 (25)
            557 BINARY_SUBSCR       			# flag[25]
            558 LOAD_CONST              31 ('C')
            561 COMPARE_OP               3 (!=)		# flag[25] != 'C'
            564 POP_JUMP_IF_FALSE      580		# Jump past exit (keep checking) if false

 30         567 LOAD_FAST                1 (check)
            570 LOAD_CONST              11 (1)
            573 INPLACE_ADD         
            574 STORE_FAST               1 (check)
            577 JUMP_FORWARD           260 (to 840)

 31     >>  580 LOAD_GLOBAL              0 (ord)
            583 LOAD_FAST                0 (flag)
            586 LOAD_CONST              32 (26)	
            589 BINARY_SUBSCR       			# flag[26]
            590 CALL_FUNCTION            1		# ord(flag[26])
            593 LOAD_CONST               4 (2)
            596 BINARY_MODULO       			# ord(flag[26])%2
            597 LOAD_CONST               1 (0)
            600 COMPARE_OP               3 (!=)		# ord(flag[26])%2 != 0
            603 POP_JUMP_IF_TRUE       675		# Jump to fail if true
            606 LOAD_GLOBAL              0 (ord)
            609 LOAD_FAST                0 (flag)
            612 LOAD_CONST              32 (26)
            615 BINARY_SUBSCR       			# flag[26]
            616 CALL_FUNCTION            1		# ord(flag[26])
            619 LOAD_CONST              33 (3)
            622 BINARY_MODULO       			# ord(flag[26])%3
            623 LOAD_CONST               1 (0)
            626 COMPARE_OP               3 (!=)		# ord(flag[26])%3 != 0
            629 POP_JUMP_IF_TRUE       675		# Jump to fail if true
            632 LOAD_GLOBAL              0 (ord)
            635 LOAD_FAST                0 (flag)
            638 LOAD_CONST              32 (26)
            641 BINARY_SUBSCR       			# flag[26]
            642 CALL_FUNCTION            1		# ord(flag[26])
            645 LOAD_CONST              34 (4)
            648 BINARY_MODULO       			# ord(flag[26])%4
            649 LOAD_CONST               1 (0)
            652 COMPARE_OP               3 (!=)		# ord(flag[26])%4 != 0
            655 POP_JUMP_IF_TRUE       675		# Jump to fail if true
            658 LOAD_FAST                0 (flag)
            661 LOAD_CONST              32 (26)
            664 BINARY_SUBSCR       			# flag[26]
            665 LOAD_ATTR                5 (isdigit)
            668 CALL_FUNCTION            0		# getattr(flag[26], isdigit)
            671 UNARY_NOT           			# !getattr(flag[26], isdigit)
            672 POP_JUMP_IF_FALSE      685		# Jump past fail (keep checking) if false

 32     >>  675 LOAD_GLOBAL              1 (F41l)
            678 CALL_FUNCTION            0
            681 POP_TOP             
            682 JUMP_FORWARD           155 (to 840)

 33     >>  685 LOAD_GLOBAL              4 (int)
            688 LOAD_FAST                0 (flag)
            691 LOAD_CONST              18 (23)
            694 BINARY_SUBSCR       			# flag[23]
            695 CALL_FUNCTION            1		# int(flag[23])
            698 LOAD_CONST              33 (3)
            701 COMPARE_OP               3 (!=)		# int(flag[23]) != 3
            704 POP_JUMP_IF_FALSE      720		# Jump past exiting (keep checking) if alse

 34         707 LOAD_FAST                1 (check)
            710 LOAD_CONST              11 (1)
            713 INPLACE_ADD         
            714 STORE_FAST               1 (check)
            717 JUMP_FORWARD           120 (to 840)

 35     >>  720 LOAD_FAST                0 (flag)
            723 LOAD_CONST              35 (22)
            726 BINARY_SUBSCR       			# flag[22]
            727 LOAD_FAST                0 (flag)
            730 LOAD_CONST              36 (13)
            733 BINARY_SUBSCR       			# flag[13]
            734 LOAD_ATTR                6 (lower)
            737 CALL_FUNCTION            0		# getattr(flag[13], lower)
            740 COMPARE_OP               3 (!=)		# getattr(flag[13], lower) != flag[22]
            743 POP_JUMP_IF_FALSE      756		# Jump past fail (keep checking) if false

 36         746 LOAD_GLOBAL              1 (F41l)
            749 CALL_FUNCTION            0
            752 POP_TOP             
            753 JUMP_FORWARD            84 (to 840)

 38     >>  756 LOAD_FAST                1 (check)
            759 POP_JUMP_IF_FALSE      772		# Go to 772

 39         762 LOAD_GLOBAL              1 (F41l)
            765 CALL_FUNCTION            0
            768 POP_TOP             
            769 JUMP_FORWARD             0 (to 772)

 40     >>  772 LOAD_CONST               1 (0)		
            775 STORE_FAST               2 (tmp)	# tmp = 0

 41         778 SETUP_LOOP              30 (to 811)	# Following code is equivalent to (for i in flag: tmp+=ord(i))
            781 LOAD_FAST                0 (flag)
            784 GET_ITER            			# iter(flag)
        >>  785 FOR_ITER                22 (to 810)	# iter(flag).next(), jump to 810 if no next()
            788 STORE_FAST               3 (i)		# i = iter(flag).next()

 42         791 LOAD_FAST                2 (tmp)
            794 LOAD_GLOBAL              0 (ord)
            797 LOAD_FAST                3 (i)
            800 CALL_FUNCTION            1		# ord(i)
            803 INPLACE_ADD         			# tmp + ord(i)
            804 STORE_FAST               2 (tmp)	# tmp = tmp + ord(i)
            807 JUMP_ABSOLUTE          785		# Loop back to 785
        >>  810 POP_BLOCK           			# End of loop

 43     >>  811 LOAD_FAST                2 (tmp)
            814 LOAD_CONST              37 (2441)
            817 COMPARE_OP               3 (!=)		# tmp != 2441
            820 POP_JUMP_IF_FALSE      833		# Jump to correct if false!

 44         823 LOAD_GLOBAL              1 (F41l)
            826 CALL_FUNCTION            0
            829 POP_TOP             
            830 JUMP_FORWARD             7 (to 840)

 46     >>  833 LOAD_GLOBAL              7 (C0rr3ct)	# Woo!
            836 CALL_FUNCTION            0
            839 POP_TOP             
        >>  840 LOAD_CONST               0 (None)
            843 RETURN_VALUE        

F41l func:
  3           0 LOAD_CONST               1 ('Bye!!!')
              3 PRINT_ITEM          
              4 PRINT_NEWLINE       

  4           5 LOAD_CONST               2 (0)
              8 RETURN_VALUE        

None
```

### What We Know

```python
* ord(flag[0])+52 == ord(flag[-1])
* ord(flag[-1]-2 == ord(flag[7])
* flag[0:7] == 'ISITDTU'
* flag[9] == flag[14] == flag[19] == flag[24] (after filling the rest of the flag in, it's apparent that these should be '_')
* ord(flag[8]) = 49 (flag[8] == '1')
* flag[8] == flag[16]
* flag[10:14] == 'd0nT'
* int(flag[18]) + int(flag[23] + int(flag[28]) == 9
* flag[18] == flag[28] (flag[18] == flag[23 == flag[28] == '3')
* flag[15] == 'L'
* ord(flag[17])^-10 == -99 (flag[17] == 'k')
* ord(flag[20])+2 == ord(flag[27])
* ord(flag[27]) <= 123
* ord(flag[20]) >= 97
* ord(flag[27])%100 = 0 (flag[27] == d; flag[20] == b)
* flag[25] == 'C'
* ord(flag[26])%2,3,4 == 0 (ord(flag[26]) is a multiple of 24)
* flag[26] is a int (flag[26] == '0')
* int(flag[23]) == 3
* flag[22] == flag[13].lower() (flag[22] == 't')
* sum of ord(i) for i in flag == 2441 (with only one character missing at this point, ord(flag[21]) has to be 58, flag[21] == ':')
```


### The Flag
Using what we know has to be true about the flag, we can figure out what it is:
```
ISITDTU{1_d0nT_L1k3_b:t3_C0d3}
```
