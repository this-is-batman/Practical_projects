# Find PI to the nth digit
import math

def get_digit_after_pi():
    n = input("Enter the number of digits after decimal of pi that you want to keep?\n")
    if int(n)>20:
        print("The hard limit is 20 digits after decimal in pi.")
        exit(-1)
    str = '{:0.'+ n +'f}'
    print(str.format(math.pi))

if __name__ == "__main__":
     get_digit_after_pi()
