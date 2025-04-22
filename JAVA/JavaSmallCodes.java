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
		// Declarations
		ArrayList<String> list = new ArrayList<>();
		list.add("John");
		list.add("David");
		list.add("Scott");
		list.add("Smith");
		System.out.println(list.size());
		
		// reading values from arraylist
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
		// Declararion
		ArrayList<Object> list = new ArrayList<>();
		// Adding values to array list
		list.add("Welcome");
		list.add(100);
		list.add(10.5);
		list.add('C');
		list.add(true);
		System.out.println(list.size());
		System.out.println(list.get(2));
		System.out.println("Before inserting:" + list);
		// Insert values into arraylist
		list.add(1, "selenium");
		System.out.println("After insertion:" + list);
		// remove values from arraylist
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
package com.basic;

import java.util.Arrays;

public class BinarySearch {

	public static void main(String[] args) {
		int array[] = { 10, 20, 30, 40, 50};
		System.out.println(Arrays.binarySearch(array, 30));
	}
}
2
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
