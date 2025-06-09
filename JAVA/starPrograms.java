package com.tryPrograms;

public class Try1 {
    public static void main(String[] args) {
        int n=5;
        for (int row=0; row<n; row++) {
        	System.out.println("* ".repeat(n));
        }
    }
}
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n=5;
        for (int row=1; row<=n; row++) {
        	System.out.print("  ".repeat(n-row));
        	System.out.println("* ".repeat(row));
        }
    }
}
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n=5;
        for(int row=n; row>=1; row--) {
        	System.out.print("  ".repeat(n-row));
        	System.out.println("* ".repeat(row));
        }
    }
}
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n=5;
        for (int row=1; row<=n; row++) {
        	System.out.println("* ".repeat(row));
        }
    }
}
* 
* * 
* * * 
* * * * 
* * * * * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n=5;
        for (int row=n; row>=1; row--) {
        	System.out.println("* ".repeat(row));
        }
    }
}
* * * * * 
* * * * 
* * * 
* * 
* 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n=5;
        for (int row=1; row<=n; row++) {
        	System.out.print("  ".repeat(n-row));
        	System.out.println("* ".repeat(2* row-1));
        }
    }
}
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n=5;
        for (int row=n; row>=1; row--) {
        	System.out.print("  ".repeat(n-row));
        	System.out.println("* ".repeat(2* row-1));
        }
    }
}
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n = 5;
        for (int row=1; row<=n; row++) {
        	System.out.print("  ".repeat(n-row));
        	System.out.println("* ".repeat(2*row-1));
        }
        for (int row=n-1; row>=1; row--) {
        	System.out.print("  ".repeat(n-row));
        	System.out.println("* ".repeat(2*row-1));
        }
    }
}
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n = 5;
        for (int row=n; row>=1; row--) {
        	System.out.print("  ".repeat(n-row));
        	System.out.println("* ".repeat(2*row-1));
        }
        for (int row=2; row<=n; row++) {
        	System.out.print("  ".repeat(n-row));
        	System.out.println("* ".repeat(2*row-1));
        }
    }
}
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n = 5;
        for (int row=1; row<=n; row++) {
        	System.out.print("* ".repeat(row));
        	System.out.print("  ".repeat(n*2 - row*2));
        	System.out.println("* ".repeat(row));
        }
        for (int row=n-1; row>=1; row--) {
        	System.out.print("* ".repeat(row));
        	System.out.print("  ".repeat(n*2 - row*2));
        	System.out.println("* ".repeat(row));
        }
    }
}
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n = 5;
        for (int row=1; row<n*2; row++) {
        	for (int col=1; col<n*2; col++) {
        		System.out.print(
        				(row == col || row+col == n*2)
        				? "*"
        				: "  ");
        	}
        	System.out.println();
        }
    }
}
*              *
  *          *  
    *      *    
      *  *      
        *        
      *  *      
    *      *    
  *          *  
*              *
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n = 5;
        for (int row=1; row<n*2; row++) {
        	for (int col=1; col<=n*2; col++) {
        		System.out.print(
        					    (row==n || col==n)
        					    ?"*"
        					    :" ");
        	}
        	System.out.println();
        }
    }
}
    *     
    *     
    *     
    *     
**********
    *     
    *     
    *     
    *  
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n = 5;
        for (int row=1; row<=n; row++) {
        	for (int col=1; col<=n; col++) {
        		System.out.print(
        				        ((row==n || col==5)
        				        || (row==1) || (col==1))
        						? "* "
        						: "  ");
        	}
        	System.out.println();
        }
    }
}
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n = 5;
        for (int row=0; row<n; row++) {
        	for (int col=1; col<=n*2 - 1; col++) {
        		System.out.print(
        				        (col == n-row || col == n+row
        				        || row == n-1)
        				        ? "* "
        				        : "  ");
        	}
        	System.out.println();
        }
    }
}
        *         
      *   *       
    *       *     
  *           *   
* * * * * * * * * 
==========================================================================================
package com.tryPrograms;
public class Try1 {
    public static void main(String[] args) {
        int n = 5;
        for (int row=0; row<n; row++) {
        	for (int col=1; col<=n*2 - 1; col++) {
        		System.out.print(
        				(col == n-row || col == n+row)?"* ": " ");
        	}
        	System.out.println();
        }
        for (int row=n-2; row>=0; row--) {
        	for (int col=1; col < n*2-1; col++) {
        		System.out.print(
        				(col==n-row || col==n+row) ? "* " : " ");
        	}
        	System.out.println();
        }
    }
}
    *     
   *  *    
  *    *   
 *      *  
*        * 
 *      * 
  *    *  
   *  *   
    *  
==========================================================================================

==========================================================================================

==========================================================================================

==========================================================================================

==========================================================================================

==========================================================================================

==========================================================================================

==========================================================================================
