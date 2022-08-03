import string
alpha = string.ascii_lowercase
def print_rangoli(size):
    for i in range(n):
        s = "-".join(alpha[i:n])
        print(s)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
a-b-c
b-c
c

import string
alpha = string.ascii_lowercase
L = []
def print_rangoli(size):
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
    print('\n'.join(L[:0:-1] + L))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
OUTPUT:
10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
