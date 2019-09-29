# addition,multiplication,negation, inverse of complex numbers
class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

def add_complex(c1, c2):
    return Complex(c1.real+c2.real,c1.imaginary+c2.imaginary)

def sub_complex(c1,c2):
    return Complex(c1.real-c2.real,c1.imaginary-c2.imaginary)

def get_negation(c1):
    return Complex(-c1.real,-c1.imaginary)

def get_inverse(c1):
    denom = c1.real*c1.real + c1.imaginary*c1.imaginary
    return Complex(float(c1.real/denom),-float(c1.imaginary/denom))

   