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
}    ==>    Count of each num : {1=3, 2=2, 7=1, 8=1}
*********************************************************************************
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {7, 3, 2, 9, 0, 6, 7, 3, 1, 2, 9, 0, 6, 4, 8, 5, 1};
        rearrangeArray(arr);  // call the method
    }
    public static void rearrangeArray(int[] arr) {
        Arrays.sort(arr);  // sort first
        int[] result = new int[arr.length];
        int left = 0, right = arr.length - 1;
        for (int i = 0; i < arr.length; i++) {
            if (i % 2 == 0) {
                result[i] = arr[right--];  // pick largest remaining
            } else {
                result[i] = arr[left++];   // pick smallest remaining
            }
        }
        System.arraycopy(result, 0, arr, 0, arr.length);
        System.out.println(Arrays.toString(result));
    }
}    --->    [9, 0, 9, 0, 8, 1, 7, 1, 7, 2, 6, 2, 6, 3, 5, 3, 4]
// Time Complexity: O(n log n) — Due to sorting.
// Space Complexity: O(n) — We use an extra array for rearrangin
*********************************************************************************
// Time Complexity: O(n) — We traverse the array once.
// Space Complexity: O(1) — No extra space required.
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 0, 2, 5, 0, 1, 0, 7, 0};
        int sum=0;
        for (int num : arr) {
            sum += num;
        }
        System.out.print("Sum of numbers : "+sum);
    }
}   Sum of numbers : 27
*********************************************************************************
// Time Complexity: O(n) — Each element is reversed a constant number of times.
// Space Complexity: O(1) — In-place modification
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 0, 2, 5, 0, 1, 0, 7, 0};
        int[] result;
        result = rotateArray(arr, 5);
        System.out.print("Rotated array : "+Arrays.toString(result));
    }
    public static int[] rotateArray(int[] arr, int k) {
        int n = arr.length;
        k = k % n;
        reverse(arr, 0 , k-1);
        reverse(arr, k , n-1);
        reverse(arr, 0 , n-1);
        return arr;
    }
    public static void reverse(int[] arr, int start, int end) {
        while(start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}    ==>    Rotated array : [0, 1, 0, 7, 0, 8, 4, 0, 2, 5]
*********************************************************************************
// Time Complexity: O(n) — We reuse the sum calculation.
// Space Complexity: O(1) — Only constant space used
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 0, 2, 5, 0, 1, 0, 7, 0};
        double result;
        result = (double)sumOfArray(arr)/arr.length; ;
        System.out.print("Sum of array : "+result);
    }
    public static int sumOfArray(int[] arr) {
        int sum = 0;
        for (int num : arr) {
        sum += num;
        }
        return sum;
    }
}    ==>        Sum of array : 2.7
*********************************************************************************
// Time Complexity: O(n log n) — Sorting the array.
// Space Complexity: O(1) — Sorting is done in place
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 0, 2, 5, 0, 1, 0, 7, 0};
        double result;
        result = findMedian(arr) ;
        System.out.print("Sum of array : "+result);
    }
    public static double findMedian(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        if (n % 2 == 0) {
            return (arr[n/2-1] + arr[n/2])/2.0;
        } else {
            return arr[n / 2];
          }
    }  
}    ===>        Sum of array : 1.5
*********************************************************************************
// Time Complexity: O(n) — Copying the entire array.
// Space Complexity: O(n) — Extra space for the new arra
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 0, 2, 5, 0, 1, 0, 1, 7, 0};
        int[] result = addElement(arr, 6);
        System.out.println("Array after adding element: " + Arrays.toString(result));
    }
    public static int[] addElement(int[] arr, int ele) {
        int[] newArr = new int[arr.length + 1];
        System.arraycopy(arr, 0, newArr, 0, arr.length);
        newArr[arr.length] = ele;  
        return newArr;
    }
}  ==>   Array after adding element: [8, 4, 0, 2, 5, 0, 1, 0, 1, 7, 0, 6]
*********************************************************************************
// Time Complexity: O(n) — We traverse the array and use a set.
// Space Complexity: O(n) — Set and list both take linear space
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 7, 2, 5, 0, 1, 0, 1, 7, 0};
        List<Integer> result = findRepeating(arr);
        System.out.println("Array after adding element: " + result);
    }
    public static List<Integer> findRepeating(int[] arr) {
        Set<Integer> seen = new HashSet<>();
        List<Integer> repeating = new ArrayList<>();
        for (int num : arr) {
            if (!seen.add(num)) {
                repeating.add(num);
            }
        }
        return repeating;
    }
}    ==>    Array after adding element: [0, 1, 7, 0]
*********************************************************************************
// Time Complexity: O(n) — Two passes: one to count, another to filter.
// Space Complexity: O(n) — HashMap to store counts.
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {8, 4, 7, 2, 5, 0, 1, 0, 1, 7, 0};
        List<Integer> result = findNonRepeating(arr);
        System.out.println("Array after adding element: " + result);
    }
    public static List<Integer> findNonRepeating(int[] arr) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : arr) {
            countMap.put(num, countMap.getOrDefault(num,0)+1);
        }
        List<Integer> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer>entry : countMap.entrySet()) {
            if (entry.getValue() == 1) {
                result.add(entry.getKey());
            }
        }
        return result;
    }
}    ==>        Array after adding element: [2, 4, 5, 8]
*********************************************************************************
// Time Complexity: O(n) — Traverse the array once.
// Space Complexity: O(n) — Map takes linear space.
import java.util.*;
class Main {
    public static void main(String[] args) {
        // Each element is a pair {a, b}
        int[][] arr = {
            {1, 2},
            {3, 4},
            {5, 9},
            {2, 1},
            {4, 3},
            {6, 7}
        };

        List<int[]> result = findSymmetricPairs(arr);
        System.out.println("Symmetric pairs: ");
        for (int[] pair : result) {
            System.out.println(Arrays.toString(pair));
        }
    }
    public static List<int[]> findSymmetricPairs(int[][] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        List<int[]> result = new ArrayList<>();

        for (int[] pair : arr) {
            int first = pair[0], second = pair[1];

            // If we already have the reverse pair (b, a)
            if (map.containsKey(second) && map.get(second) == first) {
                result.add(new int[]{second, first});
            } else {
                map.put(first, second);
            }
        }
        return result;
    }
}    ==>        Symmetric pairs: 
[1, 2]
[3, 4]
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
    
