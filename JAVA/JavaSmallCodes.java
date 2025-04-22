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
