# generate the fibonacci sequence upto the Nth number taken from input
fib=[] #empty list
def find_fib(n):
    fib.append(0)
    fib.append(1)
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib

if __name__=='__main__':
    n = input('Enter the value of N: \n')
    list1 = find_fib(int(n))
    print(f'The Fibonacci sequence upto the {n}th number is: \n')
    for i in list1:
        print(i)