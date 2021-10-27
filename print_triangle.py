if __name__ == '__main__':
    n = 5
    for i in range(n):
        print("* " * i)
Output ------>
* 
* *
* * *
* * * *

if __name__ == '__main__':
    n = 5
    for i in range(n):
        print(" " * (n-i)+ "* " * i)
    for i in range(n):
        print(" " * i + "* " * (n-i))
Output ------>
    * 
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
 if __name__ == '__main__':
    n = 5
    for i in range(n):
        print(" " * (n-i-1)+ "* " * (i+1))
    for i in range(n):
        print(" " * (i+1) + "* " * (n-i-1))
    * 
   * * 
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
    
if __name__ == '__main__':
    n = 5
    for i in range(n):
        print(" " * (n-i-1)+ (str(i+1) + " ") * (i+1))
    for i in range(n):
        print(" " * (i+1) + (str(n-i-1)+ " ") *(n-i-1))
OUTPUT --> 
    1 
   2 2 
  3 3 3
 4 4 4 4
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
    
 if __name__ == "__main__":
	n = 5
	for i in range(n):
		print( " " * (n-i-1), end = "")
		for j in range(i+1):
			print( j+1, end = " " )
		print()
	for i in range(n-1):
		print (" " * (i+1), end = "")
		for j in range(n-i-1):
			print( j+1, end = " ")
		print() 
    
 OUTPUT -->
    1 
   1 2 
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
        
if __name__ == "__main__":
	n = 5
	for i in range(n-1):
		print (" " * (i+1), end = "")
		for j in range(n-i-1):
			print( j+1, end = " ")
		print() 
    
OUTPUT --> 
 1 2 3 4 
  1 2 3
   1 2
    1
