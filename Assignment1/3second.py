#3 second to hh:mm:ss format
def convert(sec):
      hh=sec//3600
      mm=(sec//60)%60
      ss=sec%60
      return "%02i:%02i:%02i" % (hh, mm, ss)
      
print(convert(3668)) 

'''
Output :
01:01:08
'''
