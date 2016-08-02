#Sum of digits of the Number 210
n=210
sum=0
while n:
	sum+=n%10
	n//=10
print(sum)
