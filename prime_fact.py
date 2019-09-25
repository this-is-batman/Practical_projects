# find all the prime factors of an entered number

def is_prime(n):
    flag=0 # flag to show this is prime
    for i in range(2,int((n/2))+1):
        if n%i==0:
            flag=1
            break
    return flag

def find_prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0 and 0==is_prime(i): #find all the factors which are prime
            print(i)
    if 0==is_prime(n):
        print(n)

if __name__=='__main__':
    n=input("Enter the number: ")
    find_prime(int(n))