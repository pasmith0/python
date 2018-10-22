#!/opt/local/bin/python3
import sys

# Problem from Cardinal Peak

def fib(n):
    p=0
    q=1
    a=0

    print("00 ", end='')
    if n > 0:
        print("01 ", end='')
    for i in range(1,n):
        a=p+q
        print("%02d " % a, end='')
        p=q
        q=a

def main():
    stop = 10
    print("      ", end='')
    for n in range(0,stop):
        print("%02d " % n,  end='')
    print("")
    for n in range(0,stop):
        print("n=%02d: "% n, end='')
        fib(n)
        print("")

if __name__ == "__main__":
    main()


