#13 sum of series 1^1/1+2^2/2+3^3/3+.......
def sumOfSeries(n):
      sum=0
      for i in range(1,n+1):
            sum+=(i**i)//i
      return sum
