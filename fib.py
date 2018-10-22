import sys
p=0
q=1
r=10
if len(sys.argv) > 1:
    r = int(sys.argv[1])

for i in range(r):
    a=p+q
    print("%s" % a,end='')
    if i < r-1:
       print(", ", end='')
    p=q
    q=a

