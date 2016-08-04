#WAP to find pythogan triplet whose sum is a+b+=8
#this is also project euler problem 9
#mathblog.dk

s=1000
for a in range(1,s/3):
  for b in range(1,s/2):
    c=s-(a+b)
    if c**2==a**2+b**2:
      print(a,b,c)
#output 200 375 425
    
  
