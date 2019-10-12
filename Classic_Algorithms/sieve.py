# we need to implement the sieve of erastothenes tp find all the primes below 10*10^6
# 0 means composite 1 means prime

# the function below finds all the primes upto n here 1 is not a prime
def sieve_rule(n):
    flag=[0,0,1,1] #here 2 and 3 are the first primes
    for i in range(4,n):
        is_prime=1
        for divisor in range(2,int(n/2)):
            if i%divisor==0 and i!=divisor:
                is_prime=0
                break
            else:
                is_prime=1
        if is_prime==1:
            flag.append(1)
        else:
            flag.append(0)
    
    for count,i in enumerate(flag):
        if i==1:
            print(count, end=' ')
        


    

