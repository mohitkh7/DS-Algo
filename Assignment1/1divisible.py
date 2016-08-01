# 1.WAP to check the divisibilty
def isDivisible(a,b):
	#To check whether a is divisible by b or not
	if a%b==0:
		return True;	#Divisible
	else:
		return False;	#Non Divisible

num=int(input("Enter Any Number : "))
div=int(input("Enter Number with which divisibilty is to check : "))
print(isDivisible(num,div));
    
