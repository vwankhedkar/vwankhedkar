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
        
        System.out.println(0.0 / 0);
    }
}
output - 
    
