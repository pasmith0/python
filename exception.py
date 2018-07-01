a = 1
z = 0

try:
   c = a / z

except Exception, ex :
   print ('The following exception happened: ' + str(ex))

finally:
   print ('Got to finally')


