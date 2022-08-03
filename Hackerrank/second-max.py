if __name__ == '__main__':
    n = int(input())
    a = input().split()
    l = list(set(a))
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print(l[-2])
    OUTPUT:
    5
    2 3 6 6 5
    5
