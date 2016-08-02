#7Sum of first three digit of sum till 100
def noOfDigit(n):
      dig=0
      while n:
            dig+=1
            n//=10
      return dig

sum=0
for i in range(1,101):
      sum+=i
print(sum)
print(sum//(10*(noOfDigit(sum)-3)))
