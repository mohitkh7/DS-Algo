#Sum of factorial series
def fact(n):
      fact=1
      for i in range(1,n+1):
            fact*=i
      return fact
def sum(n):
      sum=0
      while n:
            sum+=fact(n)
            n-=1
      return sum
