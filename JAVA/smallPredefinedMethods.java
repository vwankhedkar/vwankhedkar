package com.tryPrograms;
public class StringProgs {
    public static void main(String[] args) {
       String original = "Automation";
       String reversed = new StringBuilder(original).reverse().toString();
       System.out.println("Reversed String is: " + reversed);
    }
}
Reversed String is: noitamotuA
**********************************************************************************
package com.tryPrograms;
public class StringProgs {
    public static void main(String[] args) {
       String str = "madam";
       boolean isPalindrome = true;
       for (int i=0; i<=str.length()/2; i++) {
    	   if (str.charAt(i) != str.charAt(str.length()-i-1)) {
    		   isPalindrome = false;
    		   break;
    	   }
       }
       System.out.print("String " + str + " Is palindrome " + isPalindrome);
    }
}
String madam Is palindrome true
**********************************************************************************
package com.tryPrograms;
public class StringProgs {
    public static void main(String[] args) {
       String str = "Automation World";
       str = str.toLowerCase();
       int vowels=0, consonents=0;
       for (int i=0; i<str.length(); i++) {
    	   char ch = str.charAt(i);
    	   if (ch >= 'a' && ch <= 'z') {
    		   if (ch == 'a' || ch=='e' || ch=='i' || ch=='o' || ch=='u') {
    		   vowels ++;
    	   } else {
    		   consonents ++;
    	   }
       }
     }
     System.out.print("Consonents : " + consonents + " and Vowels : " + vowels);
  }
}
Consonents : 8 and Vowels : 7
**********************************************************************************
package com.tryPrograms;
import java.util.HashMap;
public class StringProgs {
    public static void main(String[] args) {
       String str = "automation";
       HashMap<Character, Integer> charCount = new HashMap<>();
       for (char ch : str.toCharArray()) {
    	   if (charCount.containsKey(ch)) {
    		   charCount.put(ch, charCount.get(ch)+1);
    	   } else {
    		   charCount.put(ch, 1);
    	   }
       }
       System.out.println(charCount);
  }
}
{a=2, t=2, u=1, i=1, m=1, n=1, o=2}
**********************************************************************************
package com.tryPrograms;
public class StringProgs {
    public static void main(String[] args) {
       int n = 10;
       int a=0, b=1;
       System.out.print(a+" "+b+" ");
       for (int i=2; i<n; i++) {
    	   int c = a+b;
    	   System.out.print(c+" ");
    	   a=b;
    	   b=c;
       }
  }
}
0 1 1 2 3 5 8 13 21 34 
**********************************************************************************
package com.tryPrograms;
public class StringProgs {
    public static void main(String[] args) {
       int num=5;
       int factorial1=1;
       for (int i=1;i<=num;i++) {
    	   factorial1 *= i;
       }
     int factorial2 = factorialRecursive(num);
     System.out.println("Factoarial of "+num+":"+factorial1+" (loop)");
     System.out.println("Factoarial of "+num+":"+factorial2+" (recursive)");
  }
    public static int factorialRecursive(int n) {
    	if (n==0 || n==1) return 1;
    	return n*factorialRecursive(n-1);
    }
}
Factoarial of 5:120 (loop)
Factoarial of 5:120 (recursive)
**********************************************************************************


**********************************************************************************


**********************************************************************************
**********************************************************************************


**********************************************************************************


**********************************************************************************


**********************************************************************************
