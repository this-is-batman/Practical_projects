# find prime number until user chooses to stop asking for the next one
# enter 1 to say yes 0 for no

def is_prime(n):
    flag=0 # flag to show this is prime
    for i in range(2,int((n/2))+1):
        if n%i==0:
            flag=1
            break
    return flag

def find_prime():
    current_prime=2 #since 2 is the first prime number
    while 1:
        n = input("Do you want to find the next prime? ")
        if 1==int(n):
            while(1 == is_prime(current_prime)):
                current_prime+=1
            print(f'The next prime is {current_prime}')
            current_prime+=1
        else:
            print("Thank you for your patience!")
            break

if __name__ == '__main__':
    find_prime()