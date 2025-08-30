def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        seen = set()
        out = ''
        for c in string[i: i + k]:
            if c in seen:
                continue
            seen.add(c)
            out += c
        print(out)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
AABCAAADA
3
AB
CA
AD
**********************************************************************

**********************************************************************

**********************************************************************

**********************************************************************

**********************************************************************
	
**********************************************************************

**********************************************************************
	
**********************************************************************
	
**********************************************************************
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
3
This line has junk text.  
121.18.19.20  
2001:0db8:0000:0000:0000:ff00:0042:8329 
import re
_octet = r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
IPv4   = re.compile(rf'^{_octet}\.{_octet}\.{_octet}\.{_octet}$')
IPv6   = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

def classify(addr):
    if IPv4.fullmatch(addr):
        return "IPv4"
    if IPv6.fullmatch(addr):
        return "IPv6"
    return "Neither"
    
N = int(input())
for _ in range(N):
    line = input()
    print(classify(line))
	
function main() {
    const regex4ipv4 = /^(((25[0-5])|(2[0-4]\d)|(1\d{2})|(\d{1,2}))\.){3}((25[0-5])|(2[0-4]\d)|(1\d{2})|(\d{1,2}))$/;
    const regex4ipv6 = /^(([0-9a-f]{1,4}):){7}([0-9a-f]{1,4})$/;
    for (let i = 1; i < inputLines.length; i++) {
        const str = inputLines[i];
        if (regex4ipv4.test(str)) {
            console.info('IPv4');
        } else if (regex4ipv6.test(str)) {
            console.info('IPv6');
        } else {
            console.info('Neither');
        }
    }
}

<?php
    $input = stream_get_contents($_fp);
    $lines = preg_split('/\R/', $input, -1, PREG_SPLIT_NO_EMPTY);
    array_shift($lines);
    $ipv4_pattern = '/^(([01]?[0-9]{0,2}|2[0-5]?[0-5]?)\.){3}([01]?[0-9]{0,2}|2[0-5]?[0-5]?)$/';
    $ipv6_pattern = '/^(([a-fA-F0-9]{1,4}):){7}[a-fA-F0-9]{1,4}$/';
    foreach($lines as $line) {
        $result = 'Neither';
        if (preg_match($ipv4_pattern, $line)) {
            $result = 'IPv4';
        } elseif (preg_match($ipv6_pattern, $line)) {
            $result = 'IPv6';
        }
        
        echo $result . PHP_EOL;
    }
