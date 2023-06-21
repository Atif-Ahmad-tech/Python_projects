a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
# def mul_cipher(key,text):
# 	for i in text:
# 		pos=a.index(i)
# 		new_pos=pos*key
# 		if new_pos>=26:
# 			new=new_pos%26
# 			new_text=a[new]
# 			print(new_text,end="")
# 		else:
# 			print(a[new_pos],end="")
   
# def mul_decipher(key,text):
# 	for j in text:
# 		loop=int(input("enter number of loops in {}:".format(j)))
# 		if loop == 0: #check if there is any loops
# 			pos=a.index(a)
# 			while true:
# 				new_pos=pos/key
# 				if new_pos%26==0: #check if new_pos is divisible or not
# 					new=new_pos%26
# 					print(a[new])
# 					break
# 				else:
# 					pos+26
# 		else:	#check if there is any loops
# 			for k in range(1,loop+1):
# 				pos=a.index(j)
# 				pos+26
# 			new_pos=pos/key
# 			print(a[new_pos])

				

# text=input("Enter a message:")
# key=int(input("Enter a key:"))
# op=input("enter 1 to cipher or 2 to decipher:")
# if op=="1":
# 	mul_cipher(key,text.lower())
# else:
# 	mul_decipher(key,text.lower())

	