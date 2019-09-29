# enter two integers a and b and return the output a^b in log(N) time

def exp_fast(a,b):
    if b<0:
        return exp_fast(1/a,-b)
    if b==0:
        return 1
    if b==1:
        return a
    if b%2==0:
        return exp_fast(a*a,b/2)
    else:
        return a*exp_fast(a*a,(b-1)/2)
    

if __name__=='__main__':
    a= input("Enter the value of a: \n")
    b = input("Enter the value of b: \n")
    print(f'{a} raised to the power {b} is {exp_fast(int(a),int(b))}')        



    