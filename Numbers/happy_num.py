# program to check whether a number is happy or not

def squaresum(n):
    squaresum=0
    while n:
        squaresum += (n%10) * (n%10)
        n = int(n/10)
    return squaresum

def isHappy(n):
    slow=n
    fast=n
    while True:
        slow = squaresum(slow)
        fast = squaresum(squaresum(fast))
        if slow!=fast:
            continue
        else:
            break
    return slow==1


if __name__=='__main__':
    n =input("Enter the integer: ")
    if isHappy(int(n)):
        print(f'{n} is a happy number.')
    else:
        print(f'{n} is not a happy number.')
    
    # code to print the first 8 happy numbers
    count=0
    index=1
    while count !=8:
        if isHappy(index):
            print(f'{index} is the {count+1}th happy number')
            count+=1
            index+=1
        else:
            index+=1
    

