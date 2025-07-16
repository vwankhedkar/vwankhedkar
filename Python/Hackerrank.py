import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real_part = self.real * no.real - self.imaginary * no.imaginary
        imag_part = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real_part, imag_part)

    def __truediv__(self, no):
        denominator = no.real ** 2 + no.imaginary ** 2
        real_part = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        imag_part = (self.imaginary * no.real - self.real * no.imaginary) / denominator
        return Complex(real_part, imag_part)

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            return "%.2f+0.00i" % self.real
        elif self.real == 0:
            return "0.00%+.2fi" % self.imaginary
        elif self.imaginary >= 0:
            return "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            return "%.2f-%.2fi" % (self.real, abs(self.imaginary))


if __name__ == '__main__':
    c = list(map(float, input("Enter first complex number (real imaginary): ").split()))
    d = list(map(float, input("Enter second complex number (real imaginary): ").split()))
    x = Complex(*c)
    y = Complex(*d)

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x.mod())
    print(y.mod())
Enter first complex number (real imaginary): 2 1
Enter second complex number (real imaginary): 5 6
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
**************************************************
