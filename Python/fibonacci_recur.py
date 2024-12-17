def find_sum(n):
    if n==1:
        return 1
    return n + find_sum(n-1)

def fib(n):
    # 0,1,1,2,3,5,8 <-- fibonacci numbers
    # --------------
    # 0,1,2,3,4,5,6 <-- index
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

if __name__=='__main__':
    print(find_sum(5))
    print(fib(10))

def fibbo(n):
    a, b = 0, 1
    if n < 1:
        print("Invalid num")
    elif n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    elif (n > 2):
        for _ in range(n-2):
            c = a + b
            a, b = b, c
            print(c)
fibbo(int(input("Enter number: ")))
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\moveZeros.py 
Enter number: 10
1
2
3
5
8
13
21
34
