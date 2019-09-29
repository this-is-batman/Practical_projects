# build a coin flip simulator 0 for heads and 1 for tails
# say y to toss a coin and anything else to exit
import random
def coin_flip():
    heads=0
    tails=0
    while 1:
        n = input("Flip a coin?\n")
        if n=='y':
            out = random.randint(0,1)
            if out==1:
                print("Congratulations you have landed a tail.")
                tails +=1
            else:
                print("Congratulations you have landed a head.")
                heads +=1
        else:
            break
    print(f'The number of heads was {heads} and the number of tails was {tails}.')

if __name__=='__main__':
    coin_flip()