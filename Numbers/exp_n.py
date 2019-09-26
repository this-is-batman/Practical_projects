# Find e to the Nth digit
import math

def get_digit_after_e():
    n = input("Enter the number of digits you want to enter after decimal?\n")
    if int(n)>20:
        print("The hard limti is 20 after decimal in e.")
        exit(-1)
    str = '{:0.'+n+'f}'
    print(str.format(math.e))

if __name__=='__main__':
    get_digit_after_e()