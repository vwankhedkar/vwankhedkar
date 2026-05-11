evotix
public class Main {
    public static void main(String[] args) {
        // Given constraints
        int largePackageSize = 10;
        int smallPackageSize = 3;
        int totalSpace = 13;

        // Calculate maximum large packages possible using integer division
        int numLargePackages = totalSpace / largePackageSize;
        
        // Calculate remaining space after taking maximum large packages
        int remainingSpace = totalSpace % largePackageSize;
        
        // Calculate how many small packages fit in the remaining space
        int numSmallPackages = remainingSpace / smallPackageSize;
        
        // Calculate wasted space (if any)
        int spaceUsed = (numLargePackages * largePackageSize) + (numSmallPackages * smallPackageSize);
        int wastedSpace = totalSpace - spaceUsed;

        // Output results
        System.out.println("Total Space Available: " + totalSpace);
        System.out.println("Maximum Large Packages (10 units): " + numLargePackages);
        System.out.println("Small Packages (3 units): " + numSmallPackages);
        System.out.println("Wasted Space: " + wastedSpace);
    }
}
Total Space Available: 13
Maximum Large Packages (10 units): 1
Small Packages (3 units): 1
Wasted Space: 0
--------------------------------------------------------------------------------------------------------------
