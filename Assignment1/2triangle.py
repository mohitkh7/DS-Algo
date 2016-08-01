#2 WAP to check whether traingle is right angle or not
import math
def isRightTriangle(a,b,c):
      if a>b and a>c:
            if pow(a,2)==pow(b,2)+pow(c,2):
                  return True
      elif b>a and b>c:
            if pow(b,2)==pow(a,2)+pow(c,2):
                  return True
      else :
            if pow(c,2)==pow(a,2)+pow(b,2):
                  return True
      return False
      
print(isRightTriangle(3,4,5))
      
