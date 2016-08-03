#17 Date validation
def isLeapYear(n):
      if n%4==0 and n%100!=0 or n%400==0:
            return True
      return False


def isDate(dd,mm,yy):
      #checking year
      if yy<0:
            return False
      else:
            #Making Array of days in month
            if isLeapYear(yy):
                  days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
            else:
                  days=[0,31,29,31,30,31,30,31,31,30,31,30,31]
                  
            #checking month      
            if mm<1 and mm>12:
                  return True

            #checking day
            if dd>0 and dd<=days[mm]:
                  return True
            else:
                  return False
