package com.basic;
public class AddTwoMatrix {
    public static void main(String args[]) {
        int[][] first = { {1, 2}, {5, 10}, {2, 6} };
        int[][] second = { {2, 6}, {1, 2}, {5, 3} };
        int m = first.length;         // number of rows
        int n = first[0].length;      // number of columns
        int[][] sum = new int[m][n];
        System.out.println("Calculating sum of 2 matrices ...");
        for (int c = 0; c < m; c++) {
            for (int d = 0; d < n; d++) {
                sum[c][d] = first[c][d] + second[c][d];
            }
        }
        System.out.println("Sum of 2 matrices:");
        for (int c = 0; c < m; c++) {
            for (int d = 0; d < n; d++) {
                System.out.print(sum[c][d] + "\t");
            }
            System.out.println();
        }
    }
}
OUTPUT
Calculating sum of 2 matrices ...
Sum of 2 matrices:
3	8	
6	12	
7	9
******************************************************************
package com.basic;
import java.util.ArrayList;
public class ArrayListExample1 {
	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<>();
		list.add("John");
		list.add("David");
		list.add("Scott");
		list.add("Smith");
		System.out.println(list.size());
		for (String s : list)
		{
			System.out.println(s);
		}
	}
}
4
John
David
Scott
Smith
***********************************************
package com.basic;
public class EvenOrOddNumber {
	public static void main(String[] args) {
		int num = 10;
		if (num % 2 == 0)
		{
			System.out.println("Number is even number");
		}
		else
		{
			System.out.println("Number is odd number");
		}
	}
}
Number is even number
**************************************************
package com.basic;
public class BinarySearch {
	public static void main(String[] args) {
		int c, first, last, middle, n, search_element;
		int array[] = { 100, 200, 300, 400, 500 };
		search_element = 200;
		n = array.length;
		first = 0;
		last = n-1;
		middle = (first + last) / 2;
		while (first <= last)
		{
			if (array[middle] < search_element)
				first = middle + 1;
			else if (array[middle] == search_element)
			{
				System.out.println(search_element + " found at location "
						+ (middle + 1) + ".");
				break;
			} else
				last = middle - 1;
			middle = (first + last) / 2;
		}
		if (first > last)
			System.out.println(search_element + "isn't present in the list.\n");
	}
}
200 found at location 2.
*********************************************************************************
package com.basic;
public class EvenAndOddNumbersinArray {
	public static void main(String[] args) {
		int a[] = { 10, 20, 15, 3, 5, 7, 8, 2, 5, 7};
		int n = a.length;
		System.out.println("Odd Numbers");
		for (int i=0; i<n; i++)
		{
			if (a[i] % 2 != 0)
			{
				System.out.print(a[i] + " ");
			}
		}
		System.out.println();
		
		System.out.println("Even Numbers: ");
		for (int i=0; i<n; i++)
		{
			if (a[i] %2 == 0)
			{
				System.out.print(a[i] + " ");
			}
		}
	}
}
Odd Numbers
15 3 5 7 5 7 
Even Numbers: 
10 20 8 2 
*********************************************************************
package com.basic;
import java.util.ArrayList;
public class ArrayListExample2 {
	public static void main(String[] args) {
		ArrayList<Object> list = new ArrayList<>();
		list.add("Welcome");
		list.add(100);
		list.add(10.5);
		list.add('C');
		list.add(true);
		System.out.println(list.size());
		System.out.println(list.get(2));
		System.out.println("Before inserting:" + list);
		list.add(1, "selenium");
		System.out.println("After insertion:" + list);
		list.remove(3);
		System.out.println("After remove:" + list);
		for (Object i : list)
		{
			System.out.println(i);
		}
	}
}
10.5
Before inserting:[Welcome, 100, 10.5, C, true]
After insertion:[Welcome, selenium, 100, 10.5, C, true]
After remove:[Welcome, selenium, 100, C, true]
Welcome
selenium
100
C
true
***********************************************************************
package com.basic;
import java.util.Random;
public class GenerateRandonNumberssInGivenRange {
	public static void main(String[] args) {
		System.out.println("Randon integers between 0 and 50 using Random class :");
		Random random = new Random();
		for (int i=0; i<=5; i++)
		{
			System.out.print(random.nextInt(50)+ " ");
		}
		System.out.println("\nRandom integers between 0 and 50 using Math.random():");
		
		for (int i=0; i<5; i++) {
			System.out.print((int) (Math.random() * 50)+ " ");
		}
	}
}
Randon integers between 0 and 50 using Random class :
13 32 16 31 42 7 
Random integers between 0 and 50 using Math.random():
26 40 24 45 43 
**********************************************************************
import java.util.HashMap;
import java.util.Set;
class Main {
    public static void main(String[] args) {
        duplicateCharacterCount("Learn Java programming");
    }
    static void duplicateCharacterCount(String inputString) {
        HashMap<Character, Integer> charCountMap = new HashMap<>();
        char[] strArray = inputString.toLowerCase().toCharArray();
        for (char c : strArray) {
            if (c != ' ') {  // skip spaces
                charCountMap.put(c, charCountMap.getOrDefault(c, 0) + 1);
            }
        }
        System.out.println("Duplicate Characters in: " + inputString);
        for (char ch : charCountMap.keySet()) {
            if (charCountMap.get(ch) > 1) {
                System.out.println(ch + " : " + charCountMap.get(ch));
            }
        }
    }
}
Duplicate Characters in: Learn Java programming
a : 4
r : 3
g : 2
m : 2
n : 2
********************************************************************
package com.basic;
public class BubbleSort {
	public static void main(String[] args) {
		int n, c, d, temp;
		int array[] = {500, 300, 200, 400, 100 };
		n = array.length;
		System.out.println("Array before Bubble Sort");
		for (int i=0; i<n; i++)
		{
			System.out.print(array[i] + " ");
		}
		// Sorting
		temp = 0;
		for (int i=0; i<n; i++)
		{
			for (int j=1; j<(n-i); j++)
			{
				if (array[j-1] > array[j])
				{
					temp = array[j-1];
					array[j-1] = array[j];
					array[j] = temp;
				}
			}
		}
		System.out.println();
		System.out.println("Array After Bubble sort");
		for (int i=0; i<array.length; i++)
		{
			System.out.print(array[i] + " ");
		}
	}
}
Array before Bubble Sort
500 300 200 400 100 
Array After Bubble sort
100 200 300 400 500 
***********************************************************************
package com.basic;
import java.util.Scanner;
public class CountTheWords {
	public static void main(String[] args) {
		System.out.println("Enter the String: ");
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		int count = 1;
		for (int i=0; i<s.length()-1; i++)
		{
			if ((s.charAt(i) == ' ') && (s.charAt(i+1) != ' '))
			{
				count++;
			}
		}
		System.out.println("Number of words in a string = " +count);
	}
}
Enter the String: 
Candidate is low to average in Python skill
Number of words in a string = 8
**************************************************************************
package com.basic;
public class CountCharacterOccurance {
	public static void main(String[] args) {
		String s = "Java is java again and again";
		char c = 'a';
		int count = s.length() - s.replace("a", "").length();
		System.out.println("Number of occurances of a is : " + count);
	}
}
Number of occurances of a is : 9
**********************************************************************
package com.basic;
public class GreatestOfThreeNumbers {
	public static void main(String[] args) {
		int a = 50;
		int b = 100;
		int c = 20;
		if (a > b && a > c)
		{
			System.out.println("a is greatest");
		}
		else if (b > a && b > c)
		{
			System.out.println("b is greatest");
		}
		else
		{
			System.out.println("c is greatest");
		}
	}
}
b is greatest
*************************************************************
package com.basic;
public class IfElseCondition {
	public static void main(String[] args) {
		int age = 20;
		if (age >= 18)
		{
			System.out.println("Eligible for vote");
		} else
		{
			System.out.println("Not Eligible for vote");
		}
	}
}
Eligible for vote
******************************************************
package com.basic;
public class IntegerToStr {
	public static void main(String[] args) {
		int i = 123;
		String s = Integer.toString(i);
		System.out.println(s);
		s = String.valueOf(i);
		System.out.println(s);
	}
}
123
123
******************************************************
package com.basic;
public class LinearSearch {
	public static void main(String[] args) {
		int array[] = { 100, 200, 300, 400, 500 };
		int search_ele = 400;
		int c;
		for (c=0; c<array.length; c++)
		{
			if (array[c] == search_ele)
			{
				System.out.println(search_ele + " is present at location " + (c+1) + ".");
				break;
			}
		}
		if (c == array.length)
			System.out.println(search_ele + " isn't present in array.");
	}
}
400 is present at location 4.
************************************************************
package com.basic;
public class MaxMinElement {
	public static void main(String[] args) {
		int array[] = { 10, 100, 20, 50, 5, 60 };
		int max = array[0];
		for (int i=0; i<array.length; i++)
		{
			if (array[i] > max)
			{
				max = array[i];
			}
		}
		System.out.println("Max element in array: " + max);
		int min = array[0];
		for (int i=1; i<array.length; i++)
		{
			if (array[i] < min)
			{
				min = array[i];
			}
		}
		System.out.println("Min element in array: "+min);
	}
}
Max element in array: 100
Min element in array: 5
********************************************************
package com.basic;
public class DayOfWeek {
	public static void main(String[] args) {
		int day = 5;
		if (day == 1)
		{
			System.out.println("Sunday");
		} else if (day == 2)
		{
			System.out.println("Monday");
		} else if (day == 3)
		{
			System.out.println("Tuesday");
		} else if (day == 4)
		{
			System.out.println("Wednesday");
		} else if (day == 5)
		{
			System.out.println("Thursday");
		}else if (day == 6)
		{
			System.out.println("Friday");
		}else if (day == 7)
		{
			System.out.println("Saturdayday");
		}else 
		{
			System.out.println("Invalid week number");
		}
	}
}
Thursday
*************************************************************************************
package com.basic;
public class CountDigits {
	public static void main(String[] args) {
		int count = 0;
		int num = 123456;
		while (num != 0)
		{
			num /= 10;
			++ count;
		}
		System.out.println("Number of digits: " +count);
	}
}
Number of digits: 6
************************************************************************************
package com.basic;
public class NumberisPalindrome {
	public static void main(String[] args) {
		int lastDigit, sum=0, a;
		int inputNumber = 171;
		a = inputNumber;
		while (a > 0)
		{
			System.out.println("Inpput Number : " +a);
			lastDigit = a % 10;
			System.out.println("Last Digit: " +lastDigit);
			System.out.println("Digit: " + lastDigit + " was added to sum " + (sum * 10));
			sum = (sum * 10) + lastDigit;
			a = a / 10;
		}
		if (sum == inputNumber)
			System.out.println("Number is palindrome ");
		else 
			System.out.println("Number is not palindrome ");
	}
}
Inpput Number : 171
Last Digit: 1
Digit: 1 was added to sum 0
Inpput Number : 17
Last Digit: 7
Digit: 7 was added to sum 10
Inpput Number : 1
Last Digit: 1
Digit: 1 was added to sum 170
Number is palindrome 
*********************************************************************************
package com.basic;
public class StringPalindrome {
	public static void main(String[] args) {
		String s = "dad";
		int len = s.length();
		String rev = "";
		for (int i=len-1; i>=0; i--)
		{
			rev = rev + s.charAt(i);
		}
		System.out.println(rev);
		if (s.equals(rev))
		{
			System.out.println("Palindrone string");
		} else
		{
			System.out.println("Not palindrome string");
		}
	}
}
dad
Palindrone string
********************************************************************
package com.basic;
public class GreatestOfThreeNumbers {
	public static void main(String[] args) {
		int num = 10;
		if (num > 0)
		{
			System.out.println("Number is positive");
		} else
		{
			System.out.println("Number is Negative");
		}	
	}
}
Number is positive
************************************************************
package com.basic;
import java.util.ArrayList;
import java.util.HashSet;
public class RemoveDuplicateEle {
    public static void main(String[] args) {
        ArrayList<String> listWtDuplicateEle = new ArrayList<>();
        listWtDuplicateEle.add("JAVA");
        listWtDuplicateEle.add("J2EE");
        listWtDuplicateEle.add("JSP");
        listWtDuplicateEle.add("SERVLETS");
        listWtDuplicateEle.add("JAVA");
        listWtDuplicateEle.add("STRUTS");
        listWtDuplicateEle.add("JSP");
        System.out.println("ArrayList with duplicate elements:");
        System.out.println(listWtDuplicateEle);
        HashSet<String> set = new HashSet<>(listWtDuplicateEle);
        ArrayList<String> listWODuplicateEle = new ArrayList<>(set);
        System.out.println("ArrayList after removing duplicate elements:");
        System.out.println(listWODuplicateEle);
    }
}
ArrayList with duplicate elements:
[JAVA, J2EE, JSP, SERVLETS, JAVA, STRUTS, JSP]
ArrayList after removing duplicate elements:
[JAVA, SERVLETS, JSP, J2EE, STRUTS]
***************************************************************************
package com.basic;
public class RemoveJunk {
    public static void main(String[] args) {
    	String s = "å°?ç±³ä½“éªŒç‰ˆ latin string 01234567890";
    	String s1 = "@#$@#$@ testing #@$@#$@#$ Selenium !@#$@#$@# &&&& Java";
    	// Regular Expression: [^a-zA-Z0-9]
    	s = s.replaceAll("[^a-zA-Z0-9]", "");
    	System.out.println(s);
    	s1 = s1.replaceAll("[^a-zA-Z0-9]", "");
    	System.out.println(s1);
    	// s.replaceAll("[^a-zA-Z0-9\\s]", "")   \\s allows whitespace (spaces, tabs, newlines).
    	// s.replaceAll("[^\\p{L}\\p{N}]", "") \\p{L} = any kind of letter from any language \\p{N} = any kind of numeric digit
    }
}
latinstring01234567890
testingSeleniumJava
*****************************************************************************
package com.basic;
public class StrWithoutSpace {
    public static void main(String[] args) {
    	String str = " Core Java selenium automation oops   			programming ";
    	String strWOSpace = str.replaceAll("\\s", "");
    	System.out.println(strWOSpace);
    }
}
CoreJavaseleniumautomationoopsprogramming
*************************************************************************
package com.basic;
import java.util.Scanner;
public class ReverseChars {
    public static void main(String[] args) {
    	Scanner scan = new Scanner(System.in);
    	System.out.println("Please enter the string: ");
    	String original = scan.nextLine();
    	while (original.isEmpty() || original == null)
    	{
    		System.out.println("Please enter valid string which is not null empty");
    		original = scan.nextLine();
    	}
    	scan.close();
    	ReverseChars output = new ReverseChars();
    	String reverseChars = output.reverseCharacters(original);
    	System.out.println(reverseChars);
    }
    private String reverseCharacters(String originalString)
    {
    	String reverse = "";
    	for (int i = originalString.length() - 1; i >= 0; i--)
    	{
    		reverse = reverse + originalString.charAt(i);
    	}
    	return reverse;
    }
}
Please enter the string: 
GreatestOfThreeNumbers
srebmuNeerhTfOtsetaerG
**************************************************************
package com.basic;
import java.util.Scanner;
public class reverseEachWord {
    public static void main(String[] args) {
    	reverseEachWordOfString("Java Concept Of The Day");
    	reverseEachWordOfString("Java J2EE JSP Servlets Hibernate Struts");
    	reverseEachWordOfString("I am string not reversed");
    	reverseEachWordOfString("Reverse Me");
    }
    static void reverseEachWordOfString(String inputString)
    {
    	String[] words = inputString.split(" ");
    	String reverseString = "";
    	for (int i=0; i<words.length; i++)
    	{
    		String word = words[i];
    		String reverseWord = "";
    		for (int j=word.length() - 1; j >= 0; j--)
    		{
    			reverseWord = reverseWord + word.charAt(j);
    		}
    		reverseString = reverseString + reverseWord + " ";
    	}
    	System.out.println(inputString);
    	System.out.println(reverseString);
    	System.out.println("------------------------------------");
    }
}
Java Concept Of The Day
avaJ tpecnoC fO ehT yaD 
------------------------------------
Java J2EE JSP Servlets Hibernate Struts
avaJ EE2J PSJ stelvreS etanrebiH sturtS 
------------------------------------
I am string not reversed
I ma gnirts ton desrever 
------------------------------------
Reverse Me
esreveR eM 
------------------------------------
*********************************************************************************
public class ReverseNumbers {
    public static void main(String[] args) {
    	long num = 12345;
    	long rev = 0;
    	
    	while (num != 0)
    	{
    		rev = rev * 10 + num % 10;
    		num = num / 10;
    	}
    	System.out.println("Reversed num is: " +rev);
    	// With StringBuffer method
    	long num1 = 12345;
    	System.out.println(new StringBuffer(String.valueOf(num1)).reverse());
    }
}
Reversed num is: 54321
54321
***********************************************************
package com.basic;
import java.util.Scanner;
public class StringReverse {
    public static void main(String[] args) {
    	System.out.println("Enter the string: ");
    	Scanner sc = new Scanner(System.in);
    	String s = sc.nextLine();
    	int len = s.length();
    	String rev = "";
    	for (int i=len-1; i >= 0; i--)
    	{
    		rev = rev + s.charAt(i);
    	}
    	System.out.println(rev);
    	StringBuffer sf = new StringBuffer(s);
    	System.out.println(sf.reverse());
    }
}
Enter the string: 
StringBuffer
reffuBgnirtS
reffuBgnirtS
*********************************************************
package com.basic;
import java.util.Scanner;
public class SearchNumInArray {
    public static void main(String[] args) {
    	int a[] = { 10, 20, 30, 40, 50 };
    	int num = 30;
    	boolean flag = false;
    	for (int i : a)
    	{
    		if (num == i)
    		{
    			System.out.println("Element Found");
    			flag = true;
    			break;
    		}
    	}
    	if (flag == false)
    	{
    		System.out.println("Element Not Found");
    	}
    }
}
Element Found
*************************************************************
package com.basic;
import java.util.Scanner;
public class StrSearchInArray {
    public static void main(String[] args) {
    	String a[] = { "abc", "xyz", "pqr", "mno"};
    	String search_str = "xyz";
    	boolean flag = false;
    	for (String s : a)
    	{
    		if (search_str == s)
    		{
    			System.out.println("Element Found");
    			flag = true;
    			break;
    		}
    	}
    	if (flag == false)
    		System.out.println("Element Not Found");
    }
}
Element Found
*************************************************************
package com.basic;

public class SingleDimensionArray {

    public static void main(String[] args) {
    	int array[] = { 100, 200, 300, 400, 500, 600 };
    	System.out.println(array.length);
    	for (int i : array)
    	{
    		System.out.print(i + " ");
    	}
    	System.out.println("\nPrint except 400");
    	for (int i : array)
    	{
    		if (i == 400)
    		{
    			break;
    		}
    		System.out.print(i + " ");
    	}
    }
}
6
100 200 300 400 500 600 
Print except 400
100 200 300 
*******************************************************
package com.basic;
import java.util.Arrays;
public class SortArray {
    public static void main(String[] args) {
    	int data[] = { 4, 10, 2, 6, 1 };
    	Arrays.sort(data);
    	for (int c : data)
    	{
    		System.out.print(c + " ");
    	}
    	String data2[] = {"z", "a", "x"};
    	Arrays.sort(data2);
    	System.out.print("\n");
    	for (String c : data2)
    	{
    		System.out.print(c + " ");
    	}
    }
}
1 2 4 6 10 
a x z 
******************************************
package com.basic;
import java.util.Arrays;
public class StringOps {
    public static void main(String[] args) {
    	String s = "welcome";
    	System.out.println(s.length()); // length
    	String s1 = "welcome";
    	String s2 = " to java";
    	System.out.println(s1.concat(s2));
    	System.out.println("welcome".concat(" to java"));  	
    	s = "       welcome      ";
    	System.out.print(s);
    	System.out.println(s.trim());
    	System.out.println(s.charAt(4));
    	s = "welcome to java";
    	System.out.println(s.contains("java"));
    	System.out.println(s.contains("Java"));
    	s = "Selenium";
    	System.out.println(s.equals("SELENIUM"));
    	System.out.println(s.equalsIgnoreCase("SELENIUM"));   
    	s = "welcome to java";
    	System.out.println(s.replace('e', 'a'));
    	System.out.println(s.replace("java", "selenium"));
    	s = "Welcome";
    	System.out.println(s.substring(2, 4));
    	System.out.println(s.substring(4, 7));
    	s = "WelCome";
    	System.out.println(s.toLowerCase());
    	System.out.println(s.toUpperCase());
    }
}
7
welcome to java
welcome to java
       welcome      welcome
 
true
false
false
true
walcoma to java
welcome to selenium
lc
ome
welcome
WELCOME
*************************************************************
package com.basic;
import java.util.Arrays;
public class GreatestOfThreeNumbers {
    public static void main(String[] args) {
    	String a = "Hello";
    	String b = "World";
    	System.out.println("Before swapping");
    	System.out.println("The value of a is: " +a);
    	System.out.println("The value of b is: " +b);
    	a = a + b;
    	b = a.substring(0, a.length() - b.length());
    	a = a.substring(b.length());
    	System.out.println("The value of a and b after swapping is: ");
    	System.out.println("The value of a is: " +a);
    	System.out.println("The value of a is: " +b);
    }
}
Before swapping
The value of a is: Hello
The value of b is: World
The value of a and b after swapping is: 
The value of a is: World
The value of a is: Hello
******************************************************************************
package com.basic;
import java.util.Arrays;
public class ArrayEleSum {
    public static void main(String[] args) {
    	int[] array = { 10, 20, 30, 40, 50, 10 };
    	int sum = 0;
    	for (int num : array)
    	{
    		sum = sum + num;
    	}
    	System.out.println("Sum of array elements is: " + sum);
    }
}
Sum of array elements is: 160
*********************************************************************
package com.basic;
import java.util.Arrays;
public class SwapValues {
    public static void main(String[] args) {
    	int x = 5;
    	int y = 10;
    	int t;
    	t = x;
    	x = y;
    	y = t;
    	System.out.println("x = " + x + " and y = " +y);
    	// using + operator
    	x = x + y;
    	y = x - y;
    	x = x - y;
    	System.out.println("x = " + x + " and y = " +y);
    	// using * operator
    	x = x * y;
    	y = x / y;
    	x = x / y;
    	System.out.println("x = " + x + " and y = " +y);
    }
}
x = 10 and y = 5
x = 5 and y = 10
x = 10 and y = 5
****************************************************
package com.basic;
import java.util.Arrays;
public class SwitchStmt {
    public static void main(String[] args) {
    	int day = 10;
    	switch (day)
    	{
    	case 1:
    		System.out.println("Sunday");
    		break;
    	case 2:
    		System.out.println("Monday");
    		break;
    	case 3:
    		System.out.println("Tuesday");
    		break;
    	case 4:
    		System.out.println("Wedday");
    		break;
    	case 5:
    		System.out.println("Thursday");
    		break;
    	case 6:
    		System.out.println("Friday");
    		break;
    	case 7:
    		System.out.println("Saturday");
    		break;
    	default:
    		System.out.println("Invalid week number");
    	}
    }
}
Invalid week number
********************************************************************
package com.basic;
import java.util.Arrays;
public class TwoDimArray {
    public static void main(String[] args) {
    	int a[][] = new int[3][2];
    	a[0][0] = 100;
    	a[0][1] = 200;
    	a[1][0] = 300;
    	a[1][1] = 400;
    	a[2][0] = 500;
    	a[2][1] = 600;
    	System.out.println(a.length);
    	System.out.println(a[0].length);
    	
    	for (int r[] : a)
    	{
    		for (int c : r)
    		{
    			System.out.println(c);
    		}
    	}
    }
}
3
2
100
200
300
400
500
600
************************************************************
package com.basic;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class WordCharLineCount {

    public static void main(String[] args) {
    	BufferedReader reader = null;
    	int charCount = 0;
    	int wordCount = 0;
    	int lineCount = 0;
    	try
    	{
    		reader = new BufferedReader(new FileReader("C:\\Java-Selenium-Train\\eclipse-workspace\\MyJavaProgs\\src\\com\\basic\\BubbleSort.java"));
    		String currentLine = reader.readLine();
    		while (currentLine != null)
    		{
    			lineCount++;
    			String[] words = currentLine.split(" ");
    			wordCount = wordCount + words.length;
    			for (String word : words)
    			{
    				charCount = charCount + word.length();
    			}
    			currentLine = reader.readLine();
    		}
    		System.out.println("Number of Chars in A file: " + charCount);
    		System.out.println("Number of Words in A file: " + wordCount);
    		System.out.println("Number of Lines in A file: " + lineCount);
    	}
    	catch (IOException e)
    	{
    		e.printStackTrace();
    	}
    	finally
    	{
    		try
    		{
    			reader.close();
    		}
    		catch (IOException e)
    		{
    			e.printStackTrace();
    		}
    	}
    }
}
Number of Chars in A file: 576
Number of Words in A file: 100
Number of Lines in A file: 37
********************************************************************
package com.basic;
public class ArrayProgs {

	public static void main(String[] args) {
		int[] arr = {1,2,3,4,5,6,7,8,2,1,2};
		int target = 6;
		for (int i=0; i<arr.length-2; i++)
		{
			if (arr[i] + arr[i+1] + arr[i+2] == target)
			{
				System.out.println("Variable with values are: " + arr[i]+" "+arr[i+1]+" "+arr[i+2]);
			}
		}
	}

}
Variable with values are: 1 2 3
**************************************************************************
package com.basic;

public class ArrayProgs {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 2, 5, 6, 7, 8, 2, 1, 2};
        int start = 0;
        int max_start = 0;
        int max_end = 0;
        int sum = arr[0];
        int max_sum = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] - arr[i - 1] == 1) {
                sum += arr[i];
            } else {
                if (sum > max_sum) {
                    max_sum = sum;
                    max_start = start;
                    max_end = i - 1;
                }
                // reset start and sum
                start = i;
                sum = arr[i];
            }
        }

        // Final check after loop ends
        if (sum > max_sum) {
            max_sum = sum;
            max_start = start;
            max_end = arr.length - 1;
        }

        System.out.println("Maximum sum consecutive sequence is from index " + max_start + " to " + max_end);
        System.out.print("Elements are: ");
        for (int i = max_start; i <= max_end; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\nMaximum Sum: " + max_sum);
    }
}
Maximum sum consecutive sequence is from index 5 to 8
Elements are: 5 6 7 8 
Maximum Sum: 26
****************************************************************
package com.basic;

public class ArrayProgs {

	public static void main(String[] args) {
		int[] arr = {1, 2, 3, 4, 2, 5, 6, 7, 8, 2,1,2};  
        int start=0;  
        int max_start=0;  
        int max_end=0; 
        int sum=0;  
        int max_sum=arr[0];  

        for(int i=1;i<arr.length-1;i++)  
        {  
            if(arr[i]-arr[i-1]==1)  
            {  
               sum=sum+arr[i];  
            }  
            else {  
                if(sum>max_sum)  
                {  
                    max_sum=sum;  
                    max_start=start;  
                    max_end=i-1;  
                }  
                start=i; // reset i as consecutive sequence not found  
                sum = arr[i]; // reset sum to current element
            }
        }

        // Check after loop ends
        if (sum > max_sum) {
            max_sum = sum;
            max_start = start;
            max_end = arr.length - 1;
        }

        System.out.print("Max consecutive increasing sequence with max sum: ");
        for (int i = max_start; i <= max_end; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("\nMax Sum: " + max_sum);
	}
}
Max consecutive increasing sequence with max sum: 5 6 7 8 
Max Sum: 26
**********************************************************
package com.basic;

import java.util.ArrayList;

public class ArrayProgs {
	    public static void main(String[] args) {
	        int[] arr = {1, 2, 3, 4, 2, 5, 6, 7, 8, 2, 1, 3};
	        int target = 6;

	        ArrayList<ArrayList<Integer>> output = new ArrayList<>();
	        ArrayList<Integer> current = new ArrayList<>();

	        findSequences(arr, 0, 0, target, output, current);

	        System.out.println("Subsequences that sum to " + target + ":");
	        for (ArrayList<Integer> seq : output) {
	            System.out.println(seq);
	        }
	    }

	    static void findSequences(int[] arr, int index, int sum, int target,
	                              ArrayList<ArrayList<Integer>> output,
	                              ArrayList<Integer> current) {
	        if (sum == target) {
	            output.add(new ArrayList<>(current));
	            return;
	        }

	        if (index >= arr.length || sum > target) {
	            return;
	        }

	        // Include current element
	        current.add(arr[index]);
	        findSequences(arr, index + 1, sum + arr[index], target, output, current);

	        // Backtrack and exclude current element
	        current.remove(current.size() - 1);
	        findSequences(arr, index + 1, sum, target, output, current);
	    }
	}
Subsequences that sum to 6:
[1, 2, 3]
[1, 2, 2, 1]
[1, 2, 2, 1]
[1, 2, 3]
[1, 3, 2]
[1, 3, 2]
[1, 4, 1]
[1, 2, 2, 1]
[1, 2, 3]
[1, 5]
[1, 2, 3]
[2, 3, 1]
[2, 4]
[2, 2, 2]
[2, 1, 3]
[3, 2, 1]
[3, 2, 1]
[3, 3]
[4, 2]
[4, 2]
[2, 1, 3]
[5, 1]
[6]
[2, 1, 3]
***********************************************************
package com.basic;

import java.util.*;

public class ArrayProgs {
	    public static void main(String[] args) {
	        int[] arr = {1, 2, 3, 4, 2, 5, 6, 7, 8, 2, 1, 3};
	        int target = 6;

	        for (int i = 0; i < arr.length; i++) {
	            int sum = 0;

	            for (int j = i; j < arr.length; j++) {
	                sum += arr[j];

	                if (sum == target) {
	                    printSubarray(arr, i, j);
	                } else if (sum > target) {
	                    break;
	                }
	            }
	        }
	    }

	    private static void printSubarray(int[] arr, int start, int end) {
	        for (int k = start; k <= end; k++) {
	            System.out.print(arr[k]);
	            if (k < end) System.out.print(", ");
	        }
	        System.out.println();
	    }
	}
1, 2, 3
4, 2
6
2, 1, 3
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public String reverseString(String input) {
	    return new StringBuilder(input).reverse().toString();
	    }
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        String s = "Java Programming";
        String result = obj.reverseString(s);
        System.out.println("Reversed String is : " + result);	======>		Reversed String is : gnimmargorP avaJ
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public boolean isPalindrome(String str) {
	    return str.equals(new StringBuilder(str).reverse().toString());
	}
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        String s = "malayalam";
        Boolean result = obj.isPalindrome(s);
        System.out.println("Is string palindrome : " + result);		===>	Is string palindrome : true
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public static int factorial(int n) {
	    if (n == 1) return 1;
	    return n * factorial(n-1);
	    }
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        int num = 5;
        System.out.println("Factorial of number is : " + obj.factorial(num));	====>	Factorial of number is : 120
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public static void fibonacci(int count) {
	    int a=0, b=1;
	    for (int i=0; i<count; i++) {
	    	System.out.print(a + " ");
	    	int sum = a+b;
	    	a=b;
	    	b=sum;
	    }
	}
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        int num = 9;
        obj.fibonacci(num);		=====>		0 1 1 2 3 5 8 13 21 
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public static boolean primeCheck(int num) {
	    if (num<=1) return false;
	    for (int i=2; i<Math.sqrt(num);i++) {
	    	if (num % i == 0) return false;
	    }
	    return true;
	}
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        int num = 7;
        System.out.println("Is number prime: "+obj.primeCheck(num));	=====>	Is number prime: true
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public static void SwapNumbers(int a, int b) {
		System.out.println("Before: a= "+ a +",b="+b);
		a = a + b;
		b = a - b;
		a = a - b;
		System.out.println("After: a= "+ a +",b="+b);
	}
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        int a=4, b=5;
        obj.SwapNumbers(a, b);
    }
}
Before: a= 4,b=5
After: a= 5,b=4
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public static int countDigits(int n) {
		int count=0;
		while(n!=0) {
			n /= 10;
			count++;
		}
		return count;
	}
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        System.out.println("countDigits: "+obj.countDigits(12346788));	=====>	countDigits: 8
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public static int reverseNumber(int num) {
		int rev=0;
		while (num!=0) {
			rev = rev * 10 + num % 10;
			num /= 10;
		}
	return rev;
	}
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        System.out.println("Reverse number: "+obj.reverseNumber(12346788));	===>	Reverse number: 88764321
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public static int sumOfDigits(int num) {
		int sum = 0;
		while (num != 0)  {
			sum += num % 10;
			num /= 10;
		}
	return sum;
	}
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        System.out.println("sumOfDigits: "+obj.sumOfDigits(1234));	===>	sumOfDigits: 10
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public static boolean isArmstrong(int num) {
		int temp=num, sum=0, digits=0;
		while (temp != 0)  {
			digits++;
			temp /= 10;
		}
		temp = num;
		while (temp != 0) {
			sum += Math.pow(temp%10, digits);
			temp /= 10;
		}
		return sum == num;
	}
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
        System.out.println("sumOfDigits: "+obj.isArmstrong(153));	===>	sumOfDigits: true
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public static int LargestInArray(int[] arr) {
		int max = arr[0];
		for (int i:arr) {
			if (i > max) max = i;
		}
	return max;
	}
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
    	int[] arr = {11,2,33,5,68,7,8,22};
        System.out.println("LargestInArray is: "+obj.LargestInArray(arr));	====>	LargestInArray is: 68
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {   
	public static int LinearSearch(int[] arr,int key) {
		for (int i=0; i<arr.length;i++) {
			if (arr[i] == key) return i;
		}
	return -1;
	}
    public static void main(String[] args) {
    	tryProgs2 obj = new tryProgs2();
    	int[] arr = {11,2,33,5,68,7,8,22};
        System.out.println("Number present at location is: "+obj.LinearSearch(arr, 22));	==>	Number present at location is: 7
    }
}
*********************************************************************************
package WebHandling;
public class tryProgs2 {
    public static int binarySearch(int[] arr, int key) {
        int low = 0, high = arr.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (arr[mid] == key) return mid;
            if (arr[mid] < key) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        int[] arr = {1, 22, 33, 56, 68, 77, 89, 99};
        int result = obj.binarySearch(arr, 56);
        if (result != -1) {
            System.out.println("Number present at location is: " + (result + 1)); // 1-based index
        } else {
            System.out.println("Number not found in array.");
        }
    }
}		====>		Number present at location is: 4
*********************************************************************************
package WebHandling;
public class tryProgs2 {
    public static boolean EvenOdd(int n) {
        return (n %2 == 0);
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        int num = 66;
        System.out.println("Number is even or not: "+ EvenOdd(num));
    }
}	====>		Number is even or not: true
*********************************************************************************
package WebHandling;
public class tryProgs2 {
    public static void MultiplicationTable(int n) {
        for (int i=0; i<10; i++) {
        	System.out.println(n+"x"+i+"="+(n*i));
        }
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        obj.MultiplicationTable(5);
    }
}
5x0=0
5x1=5
5x2=10
5x3=15
5x4=20
5x5=25
5x6=30
5x7=35
5x8=40
5x9=45
*********************************************************************************
package com.tryPrograms;
public class Try1 {
    public void finalize() { System.out.println("Object is garbage collected...");}
    public static void main(String[] args) {
    	Try1 s1 = new Try1();
       	Try1 s2 = new Try1();
    	s1 = null;
    	s2 = null;
    	System.gc();
    }
}
Object is garbage collected...
Object is garbage collected...
*********************************************************************************
package com.tryPrograms;
import java.util.Arrays;
public class Try1 {
    public static void main(String[] args) {
    	int[] nums = {1,2,3,4,5,6,7};
    	int k = 3;
    	if (k > nums.length) {
    		k = k % nums.length;  }
    	int[] result = new int[nums.length];	
    	for (int i=0; i<k; i++) {
    		result[i] = nums[nums.length-k+i];
    	}
    	int j = 0;
    	for (int i=k; i<nums.length; i++) {
    		result[i] = nums[j];
    		j++;
    	}
    	System.arraycopy(result, 0, nums, 0, nums.length);
    	System.out.println(Arrays.toString(nums));
    }
}   ====>	[5, 6, 7, 1, 2, 3, 4]
*********************************************************************************
package com.tryPrograms;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
public class WordCountFile {
	public static void main(String[] args) {
		System.out.println("Enter Number to reverse : ");
		Scanner sc = new Scanner(System.in);
		long num = sc.nextLong();
		long rev = 0;
		while (num != 0) {
			rev = rev * 10 + num % 10;
			num = num / 10;
		}
		int num1 = 98756;
		System.out.println("Reverse of number is w/o inbuild method is: "+rev);
		System.out.println("Reverse of number is with inbuild method is: "+new StringBuffer(String.valueOf(num1)).reverse());
	}

}
Enter Number to reverse : 
643743
Reverse of number is w/o inbuild method is: 347346
Reverse of number is with inbuild method is: 65789
*********************************************************************************
package com.tryPrograms;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Try1 {
    public static void main(String[] args) {
    	Scanner scanner = new Scanner(System.in);
    	int n = Integer.parseInt(scanner.nextLine());
    	Pattern pattern = Pattern.compile("^(\\d{1,3})[- ](\\d{1,3})[- ](\\d{4,10})");
    	for (int i=0; i<n; i++) {
    		Matcher matcher = pattern.matcher(scanner.nextLine());
    		if (matcher.find()) {
    			System.out.print("CountryCode="+matcher.group(1));
    			System.out.print(",LocalAreaCode="+matcher.group(2));
    			System.out.print(",Number="+matcher.group(3));
    		}
    	}
    }
}
2
1 877 2638277
91-011-23413627
CountryCode=1,LocalAreaCode=877,Number=2638277
CountryCode=91,LocalAreaCode=011,Number=23413627
*********************************************************************************
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter first String : ");
        String str1 = scanner.nextLine();
        System.out.print("Enter second String : ");
        String str2 = scanner.nextLine();
        System.out.println("Before swapping:str1 = "+str1+",str2 = "+str2);
        str1 = str1 + str2;
        str2 = str1.substring(0,str1.length()-str2.length());
        str1 = str1.substring(str2.length());
        System.out.println("After swapping:str1= "+str1+", str2="+str2);
    }
}
Enter first String : Hello
Enter second String : World
Before swapping:str1 = Hello,str2 = World
After swapping:str1= World, str2=Hello
*********************************************************************************
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: "); 
        String input = scanner.nextLine();
        String doubledString = doubleCharacters(input); 
        System.out.println("Doubled characters: " + doubledString);
    }
    public static String doubleCharacters(String str) {
        StringBuilder doubled = new StringBuilder();
        for (int i=0; i<str.length(); i++) {
            char ch = str.charAt(i);
            doubled.append(ch).append(ch);
        }
        return doubled.toString();
    }
}
Enter a string: hello
Doubled characters: hheelllloo
*********************************************************************************
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        String input = "Hello World"; 
        VowelConsonantCount(input); 
    }
    public static void VowelConsonantCount(String str) {
        int vowels=0, consonents=0;
        str = str.toLowerCase();
        for (char c : str.toCharArray()) {
            if (c>='a' && c<='z') {
                if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
                   vowels++;
                else
                   consonents++;
            }
        }
        System.out.println("Vowels : "+vowels);
        System.out.println("Consonents : "+consonents);
    }
}
Vowels : 3
Consonents : 7
*********************************************************************************
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        String str1 = "listen"; 
        String str2 = "silent"; 
        System.out.println("Are strings Anagrams : "+areAnagrams(str1,str2)); 
    }
static boolean areAnagrams(String str1, String str2) { 
    if(str1.length() != str2.length()) 
         return false; 
    int[] charCount = new int[256]; 
    for( int i = 0; i < str1.length(); i++) { 
        charCount[str1.charAt(i)]++; 
        charCount[str2.charAt(i)]--; 
    } 
    for ( int count : charCount) { 
        if ( count !=0 ) 
            return false; 
    } 
    return true;
   }
}     Are strings Anagrams : true
*********************************************************************************
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        String str = "abc"; 
        permute(str, ""); 
    }
static void permute(String str, String prefix) { 
    if (str.length() == 0) {
        System.out.println(prefix);
    } else {
        for (int i=0;i<str.length();i++) {
            String rem = str.substring(0,i) + str.substring(i+1);
            permute(rem,prefix+str.charAt(i));
        }
     }
   }
}
abc
acb
bac
bca
cab
cba
*********************************************************************************
*********************************************************************************

*********************************************************************************

*********************************************************************************

*********************************************************************************

*********************************************************************************

*********************************************************************************

*********************************************************************************
