// Time Complexity: O(n) — We scan the entire array once.
// Space Complexity: O(1) — We use only a few extra variable
class Main {
    public static void main(String[] args) {
        int[] arr = {1,1,7,2,8,2,0,3,4,5,6,7,8,2};
        int min = arr[0];
        int max = arr[0];
        for (int i=1; i<arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
            if (arr[i] > max)
               max = arr[i];
        }
        System.out.println("Minimum is : "+min+", Maximum is : "+max);
    }
}    
-------------------------------------------------------------
// Time Complexity: O(n log n) — Due to sorting.
// Space Complexity: O(1) — Only two variables are used
import java.util.Arrays;
class Main {
    public static void main(String[] args) {
        int[] arr = {1,1,7,2,8,2,0,3,4,5,6,7,8,2};
        Arrays.sort(arr);
        System.out.println("Minimum is : "+arr[0]+", Maximum is : "+arr[arr.length-2]);
    }
}
OUTPUT ==>    Minimum is : 0, Maximum is : 8

*********************************************************************************
//Time Complexity: O(n) — Each element is swapped once.
//Space Complexity: O(1) — We are swapping elements in plac
class Main {
    public static void main(String[] args) {
        int[] arr = {1,1,7,2,8,2,3};
        int start=0, end=arr.length-1;
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
        for (int num : arr)
            System.out.print(num+" ");
    }
}    =====>        3 2 8 2 7 1 1 
*********************************************************************************
// Time Complexity: O(n) — We traverse the array once.
// Space Complexity: O(n) — Space is required for the frequency 
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {1,1,7,2,8,2,1};
        System.out.print("Count of each num : "+countFreq(arr));
    }
    public static Map<Integer,Integer> countFreq(int[] arr) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : arr) {
            freqMap.put(num, freqMap.getOrDefault(num,0)+1);
        }
        return freqMap;
    }
}
*********************************************************************************

*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
*********************************************************************************
