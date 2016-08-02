""" Types Of number
1. Prime - only two factors 19
2. palindrome - reverse is equal 43534
3. armstrong - cube of individual digit sum is equal to no 371
4. emirp - prime whose reverse is also prime but not palindromic prime 13
5. perfect no. - whose sum of divisors equal to itself 6
"""
def isPrime(n):
      fact=0;
      for i in range(2,n):
            if not(n%i):
                  fact+=1
      if fact==0 and n!=1:
            return True
      else:
            return False

def reverse(n):
      rev=0
      while n:
            rev=rev*10+n%10
            n//=10
      return rev

def isPalindrome(n):
      if reverse(n)==n:
            return True
      else:
            return False
def isArmstrong(n):
      copy=n
      change=0
      while n:
            change+=(n%10)**3
            n//=10
      if copy==change:
            return True
      else:
            return False
def isEmirp(n):
      if isPrime(n) and isPrime(reverse(n)) and not isPalindrome(n):
            return True
      else:
            return False
      
def isPerfect(n):
      sum=0
      for i in range(1,n):
            if not (n%i):
                  sum+=i
      if sum==n:
            return True
      else:
            return False

