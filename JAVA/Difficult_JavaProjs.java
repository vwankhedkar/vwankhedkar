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


**********************************************************************************************


**********************************************************************************************
