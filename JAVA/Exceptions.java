package com.tryPrograms;
public class TryCatchFinallyDemo {
    public static void main(String[] args) {
        try {
            int a = 10, b = 0;
            int result = a / b;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {  // ✅ Corrected spelling here
            System.out.println("Exception caught: " + e.getMessage());
        } finally {
            System.out.println("Cleanup done: This block always executes.");
        }
    }
}
Exception caught: / by zero
Cleanup done: This block always executes.
***************************************************************************
package com.tryPrograms;
public class ThrowExample {
    public static void main(String[] args) {
        int age=15;
        if (age < 18) {
        	throw new ArithmeticException("Access denied - you must ne at 18 years old");
        }
        System.out.println("Access granted - you are old enough");
    }
}
Exception in thread "main" java.lang.ArithmeticException: Access denied - you must ne at 18 years old
	at com.tryPrograms.StringProgs.main(StringProgs.java:7)
***************************************************************************
package com.tryPrograms;
import java.io.IOException;
public class StringProgs {
	public static void checkFile() throws IOException {
		throw new IOException("File Not Found!");
	}
    public static void main(String[] args) {
        try {
        	checkFile();
        } catch (IOException e) {
        	System.out.print("Caught Exception: " + e.getMessage());
        }
    }
}
Caught Exception: File Not Found!
***************************************************************************
Example: Custom Checked Exception
package com.tryPrograms;
class AgeTooLowException extends Exception {
	public AgeTooLowException(String message) {
		super(message);
	}
}
public class customExceptions {
	public static void validateAge(int age) throws AgeTooLowException {
		if (age < 18) {
			throw new AgeTooLowException("Age must be at least 18.");
		}
		System.out.println("Valid age!");
	}
    public static void main(String[] args) {
        try {
        	validateAge(16);
        } catch (AgeTooLowException e) {
        	System.out.print("Caught Exception: " + e.getMessage());
        }
    }
}
Caught Exception: Age must be at least 18.
***************************************************************************
Example: Custom Unchecked Exception
package com.tryPrograms;
class InvalidInputException extends RuntimeException {
	public InvalidInputException(String message) {
		super(message);
	}
}
public class StringProgs {
	public static void processInput(int number) {
		if (number <= 0) {
			throw new InvalidInputException("Number must be greater than zero.");
		}
		System.out.println("Processing number : " + number);
	}
    public static void main(String[] args) {
        processInput(-5);
    }
}
Exception in thread "main" com.tryPrograms.InvalidInputException: Number must be greater than zero.
	at com.tryPrograms.StringProgs.processInput(StringProgs.java:10)
	at com.tryPrograms.StringProgs.main(StringProgs.java:15)
***************************************************************************
Example: Checked Exception
package com.tryPrograms;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
public class StringProgs {
    public static void main(String[] args) {
        try {
            FileReader file = new FileReader("data.txt");
            BufferedReader fileInput = new BufferedReader(file);
            System.out.println(fileInput.readLine());
            fileInput.close();
        } catch (IOException e) {
            System.out.print("Caught checked exception: " + e.getMessage());
        }
    }
}
Caught checked exception: data.txt (The system cannot find the file specified)
***************************************************************************
package com.tryPrograms;
public class StringProgs {
    public static void main(String[] args) {
        try {
        	int[] arr = new int[5];
        	arr[5] = 10 / 0;
        } catch (ArithmeticException e) {
        	System.out.println("Arithmetic Exception : " + e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
        	System.out.println("Array Index Out Of Bounds Exception : " + e.getMessage());
        } catch (Exception e) {
        	System.out.println("General Exception : " + e.getMessage());
        }
    }
}
Arithmetic Exception : / by zero
***************************************************************************
package com.tryPrograms;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
public class StringProgs {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new FileReader("file1.txt"));
            BufferedWriter bw = new BufferedWriter(new FileWriter("file2.txt"));
        ) {
            String line;
            while ((line = br.readLine()) != null) {
                bw.write(line);
                bw.newLine(); // Add a newline after each line
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

***************************************************************************
  
