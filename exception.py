a = 1
z = 0

try:
   c = a / z

except Exception, e:
   print 'The following exception happened: ' + str(e)

finally:
   print 'Got to finally'


