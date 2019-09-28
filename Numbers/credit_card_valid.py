# check whether upon entering a 16 digit number it is a valid credit card number or not
# in this case we apply Luhn's algo to verify the last digit
import re
def validate_number(n):
    sum=0
    i=0
    matchObj = re.match('\d{16}',n)
    if not matchObj:
        print("Please enter a valid 16 digit card number.")
    else:
        print("Processing.....")
        for digits in n:
            if i%2==0:
                if len(str(2*int(digits)))==1:
                    sum += 2*int(digits)
                    i+=1
                else:
                    dsum=0
                    for d in str(2*int(digits)):
                        dsum += int(d)
                    sum += dsum
                    i+=1
            else:
                sum=sum+int(digits)
                i+=1    
        if sum%10==0:
            print("The credit card number is valid.")
        else:
            print("Invalid Number please try again!")

    

if __name__=='__main__':
    n = input("Enter the credit card number: ")
    validate_number(n)