class Test {
    public static void main(String[] args){
        int x = 10;
        int y = ++x;
        System.out.println(y);
    }
}
OUTPUT - 11

class Test {
    public static void main(String[] args){
        int x = 10;
        int y = ++(++x);
        System.out.println(y);
    }
}
OUTPUT - ERROR!
/tmp/F9Xh5qtOhY/Test.java:7: error: unexpected type
        int y = ++(++x);
                   ^
  required: variable
  found:    value

class Test {
    public static void main(String[] args){
        int x = 10;
        x++;
        System.out.println(x);
    }
}
OUTPUT - 11

class Test {
    public static void main(String[] args){
        int x = 10;
        x++;
        System.out.println(x);
    }
}
output - b

class Test {
    public static void main(String[] args){
        double x = 10.5;
        x++;
        System.out.println(x);
    }
}
output - 11.5

class Test {
    public static void main(String[] args){
        boolean x = true;
        x++;
        System.out.println(x);
    }
}
output - ERROR!
/tmp/zOgwEQx0kK/Test.java:7: error: bad operand type boolean for unary operator '++'

class Test {
    public static void main(String[] args){
        byte x = 10;
        x++;
        System.out.println(x);
    }
}
output - 11

class Test {
    public static void main(String[] args){
        byte x = 10;
        x + 1;
        System.out.println(x);
    }
}
output - ERROR!
/tmp/JtdPqJJ3af/Test.java:7: error: not a statement

class Test {
    public static void main(String[] args){
        byte x = 10;
        byte y = 20;
        byte z = x + y;
        System.out.println(z);
    }
}
OUTPUT - /tmp/BrQ4lL21Qk/Test.java:8: error: incompatible types: possible lossy conversion from int to byte
[In Java, the arithmetic operations (+, -, *, /) involving byte, short, or char automatically promote the values to int before performing the operation. As a result, the sum of x and y is of type int, which cannot be directly assigned to a byte without explicit casting because int has a larger range]

class Test {
    public static void main(String[] args){
        byte x = 10;
        byte y = 20;
        int z = x + y;
        System.out.println(z);
    }
}
output - 30

class Test {
    public static void main(String[] args){
        byte x = 10;
        byte y = 20;
        int z = x + y;
        System.out.println(z);
    }
}
output - 30

class Test {
    public static void main(String[] args){
        byte x = 10;
        // x = x + 1; rror: incompatible types: possible lossy conversion from int to byte
        x = (byte) (x + 1);
        System.out.println(x);
    }
}
output - 11

byte + byte = int
byte + short = int
short + short = int
byte + long = long
long + double = double
float + long = float
char + char = int
char + double = double
'a' + 'b' = 195 (97 + 98)
'a' + 0.89 = 97.89

class Test {
    public static void main(String[] args){
        
      //  System.out.println(10 / 0); java.lang.ArithmeticException: / by zero
      //System.out.println(10 / 0.0);  Infinity
     // System.out.println(10 / 0.0);    Infinity
     // System.out.println(-10.0 / 0);   -Infinity
    // System.out.println(0.0/0);  NaN
    // System.out.println(-0.0/0);  NaN
    System.out.println(0/0); 
     //Exception in thread "main" jav.lang.ArithmeticException: / by zero at Test.main(Test.java:10)N
    }
}

class Test {
    public static void main(String[] args){
        
     // System.out.println(10 < Float.NaN);  false Not a Number
    // System.out.println(10 <= Float.NaN); false
    // System.out.println(10 > Float.NaN);   false
    // System.out.println(10 >= Float.NaN);   false
    // System.out.println(10 == Float.NaN);   false
    // System.out.println(10 != Float.NaN);   true
     System.out.println(Float.NaN != Float.NaN); true
    }
}

Arithmatic Exception is -
    1. It is runtime exception but not compile time error
    2. It is possible only in integral arithmatic but not in floating point arithmatic
    3. The only operators which cause AE are / and %

The only overloaded operartor in java is '+'
10 + 20 = 30
"ab" + "cd" = abcd

class Test {
    public static void main(String[] args){
    String a = "durga";
    int b=10, c=20, d=30;
    a = b+c+d;
    a = a+b+c;
    b = a+c+d;
    b = b+c+d;
   //System.out.println(b+a+c+d); 10durga2030
    }
}

ERROR!
/tmp/nz4ZLZgGwB/Test.java:8: error: incompatible types: int cannot be converted to String
    a = b+c+d;
           ^
ERROR!
/tmp/nz4ZLZgGwB/Test.java:10: error: incompatible types: String cannot be converted to int
    b = a+c+d;
           ^
2 errors

class Test {
    public static void main(String[] args){
    //System.out.println(10 < 20); true
    //System.out.println('a' < 10);  false
    //System.out.println('a' < 976); true
    //System.out.println('a' > 'A'); true
    System.out.println(true > false); 
    //error: bad operand types for binary operator '>'
    }
}

No relationals operators will be applied for object types "vais123" > "vais" not true

class Test {
    public static void main(String[] args){
    System.out.println(10 < 20 < 30); 
    10 < 20 = true < 30
  //  error: bad operand types for binary operator '<'
  //  System.out.println(10 < 20 < 30);                            ^
  // first type:  boolean
  // second type: int
    }
}

class Test {
    public static void main(String[] args){
    //System.out.println(10 == 20); false
    //System.out.println('a' == 'b');  false
    //System.out.println('a' == 97.0); true
    //System.out.println(false > false); true
    }
}
object r1 = object r2 true

class Test {
    public static void main(String[] args){
    Thread t1 = new Thread();
    Thread t2 = new Thread();
    Thread t3 = t1
    // System.out.println(t1 == t2); false
    // System.out.println(t1 == t3);  true
    }
}

class Test {
    public static void main(String[] args){
    Thread t = new Thread();
    Object o = new Object();
    String s = new String("Vais");
    System.out.println(t == o);  //false
    System.out.println(o == s);  //false
    System.out.println(s == t);  // error: incomparable types: String and Thread
    }
}

class Test {
    public static void main(String[] args){
    String s1 = new String("Vais");
    String s2 = new String("Vais");
    System.out.println(s1 == s2); // false
    System.out.println(s1.equals(s2));  // true
    }
}

object r == null // false
class Test {
    public static void main(String[] args){
    String s1 = new String("Vais");
    String s2 = null;
    System.out.println(s1 == null); // false
    System.out.println(s2 == null);  // true
    System.out.println(null == null);  // true
    }
}

class MyJavaClass {
	public static void main(String args[]) {
		Thread t = new Thread();
		System.out.println(t instanceof Runnable);
		System.out.println(t instanceof Object);
	}

}
OUTPUT : tue
    true

class MyJavaClass {
	public static void main(String args[]) throws Exception {
		Thread t = new Thread();
		System.out.println(Class.forName(args[0]).isInstance(t));
	}

}
OUTPUT : C:\Users\VWankhedkar\eclipse-workspace\JavaProject\src>java MyJavaClass java.lang.String
false

C:\Users\VWankhedkar\eclipse-workspace\JavaProject\src>java MyJavaClass java.lang.Runnable
true

