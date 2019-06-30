Move with the keys a->left, d->right, s->down, w->up to go to the treasure hidden in the matrix

nc 35.222.74.110 5555

root@kali:~/Documents/CTF-Writeups/ISITDTU/Web# nc 35.222.74.110 5555

	//=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+//
	//'####::'######::'####:'########:'########::'########:'##::::'##://
	//. ##::'##... ##:. ##::... ##..:: ##.... ##:... ##..:: ##:::: ##://
	//: ##:: ##:::..::: ##::::: ##:::: ##:::: ##:::: ##:::: ##:::: ##://
	//: ##::. ######::: ##::::: ##:::: ##:::: ##:::: ##:::: ##:::: ##://
	//: ##:::..... ##:: ##::::: ##:::: ##:::: ##:::: ##:::: ##:::: ##://
	//: ##::'##::: ##:: ##::::: ##:::: ##:::: ##:::: ##:::: ##:::: ##://
	//'####:. ######::'####:::: ##:::: ########::::: ##::::. #######:://
	//....:::......:::....:::::..:::::........::::::..::::::.......::://
	//.............................................30.06.2019.........//
	//=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+//
				Welcome to my Matrix!!!				
	>>>Your mission is to find your way to the treasure hidden in this matrix !!!<<<
		
//=+=+=+=+=+=+=//
// 1. Caculate //
// 2. Go       //
// 3. Exit     //
//=+=+=+=+=+=+=//
		
Your choice: 
>>> 1
Enter your way: wasd
Write input to matrix --> Start position: matrix[0][0]
[['w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's']
 ['a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd']
 ['s' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w']
 ['d' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a']
 ['w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's']
 ['a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd']
 ['s' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w']
 ['d' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a']
 ['w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's']
 ['a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd']
 ['s' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w']
 ['d' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a']
 ['w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's']
 ['a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd']
 ['s' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w']]

Read value from matrix --> Start position: matrix[0][0] --> wdsawdsawdsawdsdwasdwasdwasdwasawdsawdsawdsawasdwasdwasdwasdwdsawdsawdsawdsdwasdwasdwasdwasawdsawdsawdsawasdwasdwasdwasdwdsawdsawdsawdsdwasdwasdwasdwasawdsawdsawdsawasdwasdwasdwasdwdsawdsawdsawdsdwasdwasdwasdwasawdsawdsawdsaw

Write value to matrix --> Start position: matrix[14][14]
[['w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's']
 ['a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'd' 'w' 'a' 's' 'd' 'w' 'd']
 ['s' 'a' 'w' 'a' 's' 'd' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w']
 ['a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'a']
 ['w' 'd' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'a' 'w' 'd' 's']
 ['d' 'w' 'a' 's' 'd' 'w' 'd' 's' 'a' 'w' 'd' 's' 'd' 'w' 'd']
 ['s' 'a' 'w' 'a' 's' 'a' 'w' 'a' 's' 'd' 'w' 'a' 's' 'a' 'w']
 ['a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'd' 's' 'd' 'w' 'a' 's' 'a']
 ['w' 'd' 's' 'a' 'w' 'a' 's' 'a' 'w' 'a' 's' 'd' 'w' 'd' 's']
 ['d' 'w' 'a' 's' 'd' 'w' 'd' 's' 'a' 'w' 'a' 's' 'd' 'w' 'd']
 ['s' 'a' 'w' 'd' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w']
 ['a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'a']
 ['w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's']
 ['d' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd' 's' 'a' 'w' 'd']
 ['s' 'a' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w' 'a' 's' 'd' 'w']]

Read value from matrix --> Start position: matrix[0][0], matrix[1][0] --> wdsawdsawdsawdssawasdwdsawdsawwdsdwasdwasawdssawasawasdwasawwdsawasawasdwdssawdsdwasdwasdwwasdwasdwasdwassawasdwasdwasdwawdsawdsdwasdwdasdwasdwasdwasadwasdwdsawdsdwdasdwasdwdsdwasadwasdwdsawasdwdasdwasdwasdwasadwdsawdsawdsawd

Write value to matrix --> Start position: matrix[0][14]
[['s' 'a' 'd' 's' 'w' 's' 's' 'a' 'w' 's' 's' 's' 'a' 'd' 'w']
 ['a' 'a' 's' 's' 'a' 'a' 'a' 'd' 'w' 'd' 'a' 'a' 'a' 'w' 's']
 ['d' 'w' 'w' 'd' 'd' 'w' 's' 'w' 'w' 'w' 's' 'w' 'w' 'w' 'd']
 ['a' 'a' 'd' 'a' 'w' 'w' 'a' 'a' 'a' 'a' 'd' 'a' 'a' 'd' 'd']
 ['w' 's' 's' 's' 's' 'a' 'a' 's' 'w' 's' 's' 's' 'w' 's' 's']
 ['s' 'd' 'a' 'd' 'a' 'd' 's' 's' 'd' 'w' 'a' 'a' 'd' 'd' 'd']
 ['d' 'd' 's' 'd' 'w' 'w' 'w' 'd' 'd' 'w' 'd' 'w' 'w' 'w' 's']
 ['w' 'w' 'w' 'd' 'w' 'a' 'd' 'a' 'w' 'w' 'd' 's' 'a' 'd' 'a']
 ['d' 'a' 'a' 'd' 'w' 'a' 's' 's' 's' 'a' 'a' 's' 'a' 's' 's']
 ['s' 'w' 's' 's' 's' 'd' 's' 'd' 'd' 'd' 's' 's' 's' 'w' 'd']
 ['d' 'd' 'a' 'd' 'd' 'd' 'a' 'd' 'w' 'w' 'w' 'd' 'd' 'a' 'a']
 ['w' 'w' 'w' 's' 'w' 'w' 'w' 's' 'w' 'a' 'a' 'a' 'w' 'w' 'w']
 ['w' 'd' 'd' 'a' 'd' 'd' 'd' 'a' 'd' 'd' 's' 's' 's' 'a' 'w']
 ['a' 'd' 's' 's' 's' 'w' 'a' 's' 's' 'w' 's' 'd' 'd' 'd' 's']
 ['d' 'w' 's' 'a' 'a' 'a' 'a' 's' 'a' 'a' 'a' 'a' 'w' 'w' 'w']]

Read value from matrix --> Start position: matrix[0][0] --> sadaasdwwaadwsssdaddswwwdaaswsddawwwwddadsdwsswssaaddwawwssadaddwwdwadwassddddswwaddsswaaasawadwswwaaaaswssdwdddawssssddadwwswdadassasasssdaawswadassswaawdwwdsaasdsswwdaaadsswsdaaaadwawswwdaddwssdddwwsadaassswddaawwwsawddswww

Not equal wsssddddaddsssssdddssdddwsdsdsdsdsssssddsdddssaadsddsddssddsddddsdsssdssdsdssdsdsdwsssdsdddsddddwsddddsdswsssdsdsddsssddsswwdssdssdddswddddsdwddswsasdssdddsdwdddsssddsddwsssdssdddswddsdsssdwwsdssdddawsdddsdwdsdsssssssddsddsdw
You fail!!!

//=+=+=+=+=+=+=//
// 1. Caculate //
// 2. Go       //
// 3. Exit     //
//=+=+=+=+=+=+=//
		
Your choice: 
>>> 2
Your position >>> matrix[0][0]
Input your way: wasd
Checking...
Lenght key invalid!!!
