import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr1 = {1,2,3};
        int[] arr2 = {4,5,6};
        combinedArray(arr1, arr2);
    }
    public static void combinedArray(int[] arr1, int[] arr2) {
        int length = arr1.length + arr2.length;
        int[] newArr = new int[length];
        for (int i=0; i<arr1.length; i++) {
            newArr[i] = arr1[i];
        }
        for (int i=0; i<arr2.length; i++) {
            newArr[arr1.length+i] = arr2[i]; 
        }
        System.out.println("New combined Array is : "+Arrays.toString(newArr));
    }
}    ==>  New combined Array is : [1, 2, 3, 4, 5, 6]
***************************************************************************************
import java.util.*;
class Main {
    public static void main(String[] args) {
        int arr[] = {3, 6, 9, 5, 20, 43};
        minAndMax(arr);
    }
    public static void minAndMax(int[] arr) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int i=0; i<arr.length; i++) {
            if (arr[i] < min) 
               min = arr[i];
            if (arr[i] > max)
               max = arr[i];
        }
        System.out.println("Minimum num is array : "+min);
        System.out.println("Maximum num is array : "+max);
    }
}     Minimum num is array : 3
Maximum num is array : 43
***************************************************************************************
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] input = {1, 2, 3, 4, 5};
        int target = 5;
        findTarget(input, target);
    }
    public static void findTarget(int[] input, int target) {
        List<Integer> seen = new ArrayList<>();
        for (int i=0; i<input.length; i++) {
            int value = target-input[i];
            if (seen.contains(value)) {
               System.out.println("Given target: "+input[i] + " "+value);
        }
        seen.add(input[i]);
        }
    }
}
Given target: 3 2
Given target: 4 1
***************************************************************************************
import java.util.*;
class Main {
    public static void main(String[] args) {
        int arr[] = {1, 2, 2, 3, 1, 4, 5, 1};
        countOfElement(arr);
    }    
    public static void countOfElement(int[] arr) {
        for (int i=0; i<arr.length; i++) {
            boolean alreadyPresent=false;
            for (int j=0; j<i; j++) {
                if (arr[i] == arr[j]) {
                alreadyPresent = true;
                break;
            }
        }
        if (alreadyPresent) {
            continue;
        }
        int count=1;
        for (int j=i+1; j<arr.length; j++) {
            if (arr[i] == arr[j]) {
                count++;
            }
        }
        System.out.println("Occurance of : "+arr[i]+ " is "+count);
        }
    }
}
Occurance of : 1 is 3
Occurance of : 2 is 2
Occurance of : 3 is 1
Occurance of : 4 is 1
Occurance of : 5 is 1
***************************************************************************************
import java.util.*;
class Main {
    public static void main(String[] args) {
        int arr[] = {2, 5, 7, 8, 9, 6};
        int k=3;
        LargestDigit(arr, k);
    }    
    public static void LargestDigit(int[] arr, int k) {
       int result=0;
       for (int i=0; i<arr.length; i++) {
           for (int j=0; j<arr.length; j++) {
               if (arr[i] > arr[j]) {
                   int temp = arr[i];
                   arr[i] = arr[j];
                   arr[j] = temp;
               }
           }
       }
        for (int num : arr)
            System.out.print(num + " ");
        result = arr[arr.length-k];
        System.out.println("\nKth Largest digit is : "+result);
    }
}
9 8 7 6 5 2 
Kth Largest digit is : 6
***************************************************************************************
import java.util.*;
class Main {
    public static void main(String[] args) {
        removeDuplicateChar("My name is Vaishali");
    }    
    public static void removeDuplicateChar(String input) {
       StringBuilder result = new StringBuilder();
       Set<Character> seen = new HashSet<>();
       for (int i=0; i<input.length(); i++) {
           char currentChar = input.charAt(i);
           if (!seen.contains(currentChar)) {
               seen.add(currentChar);
               result.append(currentChar);
           }
       }
       System.out.println("After removing duplicates : "+result.toString());
    }
}    After removing duplicates : My nameisVhl
***************************************************************************************
import java.util.*;
class Main {
    public static void main(String[] args) {
        int input[] = {4, 19, 3, 4, 16, 16, 19};
        System.out.println("2nd large digit is : "+secondLargest(input));
    }    
    public static int secondLargest(int[] input) {
       int largest = 0;
       int secondLarge = 0;
       for (int i=0; i<input.length; i++) {
           if (input[i] > largest) {
               secondLarge = largest;
               largest = input[i];
           }  
           else if(input[i]>secondLarge && input[i]<largest) {
               secondLarge = input[i];
           }
       }
            return secondLarge;
    }
}    2nd large digit is : 16
***************************************************************************************
import java.util.*;
class Main {
    public static void main(String[] args) {
        int input[] = {1, 4, 5, 4, 3, 0, 3, 2, 0, 1};
        System.out.println("After shifting values : "+shiftToLast(input, 0));
    }    
    public static String shiftToLast(int[] input, int shiftVal) {
       for (int i=0; i<input.length; i++) {
           for (int j=i+1; j<input.length; j++) {
               if (input[i] == shiftVal) {
                   int temp = input[i];
                   input[i] = input[j];
                   input[j] = temp;
               }
           }
       }
       return Arrays.toString(input);
    }
}    After shifting values : [1, 4, 5, 4, 3, 3, 2, 1, 0, 0]
***************************************************************************************
***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************
***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************
***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************
***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************

***************************************************************************************
