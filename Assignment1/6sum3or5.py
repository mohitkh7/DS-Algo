#6 sum of multiples of 3 or 5 till 100
sum=0
for i in range(1,101):
      if i%3==0 or i%5==0:
            sum+=i
print(sum)

#output 2418
