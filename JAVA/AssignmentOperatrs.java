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

