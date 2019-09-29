# use collatz conjecture to find how many steps it takes to reach 1

def find_steps(n):
    steps=0
    while n!=1:
        if n%2==0:
            n = n/2
            steps += 1
        else:
            n = 3*n + 1
            steps += 1
    return steps

if __name__=='__main__':
    n = input("Enter the number: \n")
    print(f'The number of steps starting from {n} to reach 1 is {find_steps(int(n))}')

