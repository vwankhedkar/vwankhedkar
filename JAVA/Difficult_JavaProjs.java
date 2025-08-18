package WebHandling;
import java.util.Arrays;
public class tryProgs2 {
    public void rotate(int[] nums, int k) {
        if (k > nums.length)
            k = k % nums.length;
        int[] result = new int[nums.length];
        for (int i = 0; i < k; i++) {
            result[i] = nums[nums.length - k + i];
        }
        int j = 0;
        for (int i = k; i < nums.length; i++) {
            result[i] = nums[j];
            j++;
        }
        System.arraycopy(result, 0, nums, 0, nums.length);
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        obj.rotate(arr, 3);

        // Print the rotated array
        System.out.println("Rotated array: " + Arrays.toString(arr));  ==> Rotated array: [5, 6, 7, 1, 2, 3, 4]
    }
}
**********************************************************************************************
package WebHandling;
import java.util.Arrays;
public class tryProgs2 {
    public static void rotate(int[] arr, int order) {
        if (arr == null || order < 0) {
            throw new IllegalArgumentException("Illegal argument!");
        }
        for (int i = 0; i < order; i++) {
            for (int j = arr.length - 1; j > 0; j--) {
                int temp = arr[j];
                arr[j] = arr[j - 1];
                arr[j - 1] = temp;
            }
        }
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        obj.rotate(arr, 4);
        // Print the rotated array
        System.out.println("Rotated array: " + Arrays.toString(arr));  ===> Rotated array: [4, 5, 6, 7, 1, 2, 3]
    }
}
**********************************************************************************************
package WebHandling;
import java.util.Arrays;
public class tryProgs2 {
    public static void rotate(int[] arr, int order) {
       order = order % arr.length;
       if (arr == null || order < 0) {
    	   throw new IllegalArgumentException("Illegal argument!");
       }
       int a = arr.length - order;
       reverse(arr, 0, a-1);
       reverse(arr, a, arr.length-1);
       reverse(arr, 0, arr.length-1);
    }
    public static void reverse(int[] arr, int left, int right) {
    	if (arr == null || arr.length == 1) {
    		return;
    	}
    	while (left < right) {
    		int temp = arr[left];
    		arr[left] = arr[right];
    		arr[right] = temp;
    		left++;
    		right--;
    	}
    }
    public static void main(String[] args) {
        tryProgs2 obj = new tryProgs2();
        int[] arr = {1, 2, 3, 4, 5, 6};
        obj.rotate(arr, 4);
        // Print the rotated array
        System.out.println("Rotated array: " + Arrays.toString(arr));  ===>    Rotated array: [3, 4, 5, 6, 1, 2]
    }
}
**********************************************************************************************
Merge 2 sorted arrays
import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] arr1 = {1, 3, 7};
        int[] arr2 = {7, 2, 5, 9};
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        int[] merged = new int[arr1.length + arr2.length];
        int i = 0, j = 0, k = 0;
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) {
                if (k == 0 || merged[k - 1] != arr1[i]) // avoid duplicates
                    merged[k++] = arr1[i];
                i++;
            } else if (arr1[i] > arr2[j]) {
                if (k == 0 || merged[k - 1] != arr2[j]) 
                    merged[k++] = arr2[j];
                j++;
            } else { // arr1[i] == arr2[j]
                if (k == 0 || merged[k - 1] != arr1[i])
                    merged[k++] = arr1[i];
                i++;
                j++;
            }
        }
        while (i < arr1.length) {
            if (k == 0 || merged[k - 1] != arr1[i])
                merged[k++] = arr1[i];
            i++;
        }
        while (j < arr2.length) {
            if (k == 0 || merged[k - 1] != arr2[j])
                merged[k++] = arr2[j];
            j++;
        }
        for (int x = 0; x < k; x++) {
            System.out.print(merged[x] + " ");
        }
    }
}
1 2 3 5 7 9 
**********************************************************************************************
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
class Main {
    public static void main(String[] args) {
        Set<Integer> set = new HashSet<>();
        int[] arr1 = {1, 3, 7};
        int[] arr2 = {7, 2, 5, 9};
        ArrayList<Integer> merged = new ArrayList<>();
        int i=0, j=0, k=0;
        while(i<arr1.length && j<arr2.length) {
            if (arr1[i] < arr2[j]) {
                merged.add(arr1[i]);
                i++;
            } else {
                merged.add(arr2[j]);
                j++;
            }
        }
        while (i < arr1.length) {
            merged.add(arr1[i]);
            j++;
        }
        while (j < arr2.length) {
            merged.add(arr2[j]);
            j++;
        }
        for (int num : merged) {
            set.add(num);
        }
        for (int num : set)
            System.out.print(num + " ");
    }
}    ===>    1 2 3 5 7 9
**********************************************************************************************


**********************************************************************************************
**********************************************************************************************


**********************************************************************************************
**********************************************************************************************


**********************************************************************************************
**********************************************************************************************


**********************************************************************************************
**********************************************************************************************


**********************************************************************************************
