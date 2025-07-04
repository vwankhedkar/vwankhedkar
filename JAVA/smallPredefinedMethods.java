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


**********************************************************************************


**********************************************************************************
**********************************************************************************


**********************************************************************************


**********************************************************************************


**********************************************************************************
**********************************************************************************


**********************************************************************************


**********************************************************************************


**********************************************************************************
