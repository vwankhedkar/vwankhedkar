class Test {
    int x = 10;
    public static void main(String[] args) {
        System.out.println(x);
    }
}
OUTPUT :    /tmp/3WfqcdA8tw/Test.java:6: error: non-static variable x cannot be referenced from a static context
        System.out.println(x);

class Test {
    int x = 10;
    public static void main(String[] args) {
        Test t = new Test();
        System.out.println(t.x);
    }
    public void m1(){
        System.out.println(x);
    }
}
OUTPUT :    10

class Test {
    int x;
    double d;
    boolean b;
    String s;

    public static void main(String[] args) {
        Test t1 = new Test();
        System.out.println(t1.x);  // Prints the default value of int (0)
        System.out.println(t1.d);  // Prints the default value of double (0.0)
        System.out.println(t1.b);  // Prints the default value of boolean (false)
        System.out.println(t1.s);  // Prints the default value of String (null)
    }
}

class Test {
    static int x = 10;
    public static void main(String[] args) {
        Test t = new Test();
        System.out.println(t.x);
        System.out.println(Test.x);
        System.out.println(x);
    }
}
OUTPUT - 10
10
10

class Test {
    static int x = 10;
    public static void main(String[] args) {
        Test t = new Test();
        System.out.println(x);
    }
    public void m1() {
        System.out.println(x);
    }
}
OUTPUT -    10

class Test {
    static int x;
    static double d;
    static String s;
    public static void main(String[] args) {
        System.out.println(x);
        System.out.println(d);
        System.out.println(s);
    }
}
OUTPUT  -    0
0.0
null

class Test {
    static int x = 10;
    int y = 20;
    public static void main(String[] args) {
        Test t1 = new Test();
        t1.x = 888;
        t1.y = 999;
        Test t2 = new Test();
        System.out.println(t1.x + "--" + t2.y);
    }
}
OUTPUT - 888--20



  
