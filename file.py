myfile = open('myfile.txt' , 'w')

try:
   myfile.write('hello');
   myfile.write('something else')
except:
   print 'Some exception happened'
finally:
   myfile.close()



