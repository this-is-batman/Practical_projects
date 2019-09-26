# find the cost required to cover W*H tile where cost is entered by the user

def find_cost(W,H):
    n = input("Enter the cost: ")
    return int(n)*W*H

if __name__=='__main__':
    print(f'The cost is {find_cost(10,20)}')