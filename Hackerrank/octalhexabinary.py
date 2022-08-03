def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(number+1):
        print("{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}".format(i=i, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
OUTPUT:
3
 0  0  0  0
 1  1  1  1
 2  2  2 10
 3  3  3 11
