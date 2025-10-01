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
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr={1, 2, 3, 4, 2, 5, 6, 7, 8, 2, 1, 2};
        int target = 6;
        for (int i=0; i<arr.length-2; i++) {
            if (arr[i]+arr[i+1]+arr[i+2]==target)
                System.out.println(target+" sum generated by consecuting 3 numbers: "+arr[i]+" "+arr[i+1]+" "+arr[i+2]);
        }
    }
}    6 sum generated by consecuting 3 numbers: 1 2 3
***************************************************************************************
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr={1, 2, 3, 4, 2, 5, 6, 7, 8, 2, 1, 2};
        int start=0;
        int max_start=0;
        int max_end=0;
        int sum=0;
        int max_sum=arr[0];
        for (int i=1; i<arr.length-1; i++) {
            if (arr[i]-arr[i-1]==1) {
               sum = sum + arr[i];
            }
            else {
               if (sum > max_sum) {
                   max_sum = sum;
                   max_start = start;
                   max_end=i-1;
               }
        start = i; //reset as consecutive sequesnce not found
        }
    }
    if (sum > max_sum) {
        max_sum=sum;
        max_start = start;
        max_end = arr.length-1;
    }
    System.out.print("consecutive sequence with max sum: ");
    for (int k=max_start; k<=max_end; k++) {
         System.out.print(arr[k]+" ");
    }
}
}    consecutive sequence with max sum: 5 6 7 8 
***************************************************************************************
// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
        int[] arr={1, 2, 3, 4, 2, 5, 6, 7, 8, 2, 1, 3};
        System.out.println("Consecutive sequences in array with sum == 6 are : ");
        for (int i=0; i<arr.length; i++) {
            int sum=0;
            for (int j=i; j<arr.length; j++) {
                sum = sum + arr[j];
                if (sum == 6) {
                    for (int k=i; k<=j; k++) {
                        System.out.print(arr[k]);
                        if (k<j) System.out.print(", ");
                    }
                    System.out.println();
                }
                else
                   if (sum > 6)
                       break;
            }
        }
    }
}        Consecutive sequences in array with sum == 6 are : 
1, 2, 3
4, 2
6
2, 1, 3
***************************************************************************************
import java.lang.reflect.Array;
import java.util.ArrayList;
class Main {
    public static void main(String[] args) {
        int[] arr={1, 2, 3, 4, 2, 5, 6, 7, 8, 2, 1, 3};
        int target=9;
        ArrayList<ArrayList<Integer>> output = new ArrayList<>();
        ArrayList<Integer> current = new ArrayList<>();
        findsequences(arr, 0, 0, target, output, current);
        System.out.println("Nonseq num generating sum == "+target);
        for (ArrayList<Integer> a:output) {
            System.out.print(a + " "); }
    }
    static void findsequences(int[] arr, int index, int sum, int target, ArrayList<ArrayList<Integer>> output, ArrayList<Integer> current) {
        if(sum==target) { 
            output.add(new ArrayList<>(current)); 
            return; 
        }
        if (index >= arr.length || sum > target) { 
            return; } 
        current.add(arr[index]); 
        findsequences(arr,index+1,sum+arr[index],target,output,current); 
        current.remove(current.size()-1); 
        findsequences(arr,index+1,sum,target,output,current); 

    }
}
Nonseq num generating sum == 9
[1, 2, 3, 2, 1] [1, 2, 3, 2, 1] [1, 2, 3, 3] [1, 2, 4, 2] [1, 2, 4, 2] [1, 2, 2, 1, 3] [1, 2, 5, 1] 
[1, 2, 6] [1, 2, 2, 1, 3] [1, 3, 4, 1] [1, 3, 2, 2, 1] [1, 3, 2, 3] [1, 3, 5] [1, 3, 2, 3] 
[1, 4, 2, 2] [1, 4, 1, 3] [1, 2, 5, 1] [1, 2, 6] [1, 2, 2, 1, 3] [1, 5, 2, 1] [1, 5, 3] [1, 6, 2] 
[1, 7, 1] [1, 8] [2, 3, 4] [2, 3, 2, 2] [2, 3, 1, 3] [2, 4, 2, 1] [2, 4, 2, 1] [2, 4, 3] [2, 2, 5] 
[2, 2, 2, 3] [2, 5, 2] [2, 6, 1] [2, 7] [3, 4, 2] [3, 4, 2] [3, 2, 1, 3] [3, 5, 1] [3, 6] [3, 2, 1, 3] 
[4, 2, 2, 1] [4, 2, 3] [4, 5] [4, 2, 3] [2, 5, 2] [2, 6, 1] [2, 7] [5, 1, 3] [6, 2, 1] [6, 3] [7, 2] [8, 1] 
***************************************************************************************
import java.util.Arrays;   // Brute force approach
class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 0, 6},
            {7, 8, 9}
        };
        int rows = matrix.length;
        int cols = matrix[0].length;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    for (int k = 0; k < rows; k++) {
                        if (matrix[k][j] != 0) {
                            matrix[k][j] = -1;
                        }
                    }
                    for (int c = 0; c < cols; c++) {
                        if (matrix[i][c] != 0) {
                            matrix[i][c] = -1;
                        }
                    }
                }
            }
        }
        // Second pass: replace -1 with 0
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == -1) {
                    matrix[i][j] = 0;
                }
            }
        }
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
[1, 0, 3]
[0, 0, 0]
[7, 0, 9]
***************************************************************************************
import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 0, 6},
            {7, 8, 9}
        };

        int rows = matrix.length;
        int cols = matrix[0].length;

        boolean[] rowZero = new boolean[rows];
        boolean[] colZero = new boolean[cols];

        // Pass 1: mark rows and cols
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    rowZero[i] = true;
                    colZero[j] = true;
                }
            }
        }

        // Pass 2: update matrix
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (rowZero[i] || colZero[j]) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Print result
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
[1, 0, 3]
[0, 0, 0]
[7, 0, 9]
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
