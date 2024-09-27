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

class Test {
    public static void main(String[] args) {
        int i = 0;
        for (int j=0; j<3; j++)
        {
            i = i + j;
        }
        System.out.println(i + " -- " + j);
    }
}
OUTPUT - /tmp/ZSZpUy8QQI/Test.java:11: error: cannot find symbol
        System.out.println(i + " -- " +j)                 ^
  symbol:   variable j

class Test {
    public static void main(String[] args) {
        try {
            j = Integer.parseInt("ten");  // This will cause a NumberFormatException
        } 
        catch (NumberFormatException e) {  // Corrected exception name
            j = 10;  // Initialize j with a default value
        }
        System.out.println(j);  // Print the value of j
    }
}

OUTPUT - /tmp/FJgzjRcLLX/Test.java:7: error: cannot find symbol
            j = Integer.parseInt("ten");  // This will cause a NumberFormatException
            ^
  symbol:   variable j
  location: class Test
ERROR!
/tmp/FJgzjRcLLX/Test.java:10: error: cannot find symbol
            j = 10;  // Initialize j with a default value
            ^
  symbol:   variable j
  location: class Test
ERROR!
/tmp/FJgzjRcLLX/Test.java:12: error: cannot find symbol
        System.out.println(j);  // Print the value of j


class Test {
    public static void main(String[] args) {
        int x;
        if (args.length > 0){
            x = 10;
        }
        else {
            x = 20;
        }
        System.out.println(x);
    }
}
OUTPUT -
    java Test.java A B -> 10
    java Test.java -> 20

class Test {
    public static void main(String[] args) {
        public int x = 10;
        protected int x = 10;
        private int x = 10;
        static int x = 10;
        transient int x = 10;
        volatile int x = 10;
        final int x = 10;
    }
}
OUTPUT -
    ERROR!
/tmp/GyR0XAzlca/Test.java:6: error: illegal start of expression
        public int x = 10;
        ^
ERROR!
/tmp/GyR0XAzlca/Test.java:14: error: class, interface, or enum expected
}
^
2 errors
// Instance level
class Test {
    int[] x;
    public static void main(String[] args) {
        Test t = new Test();
        System.out.println(t.x);
        System.out.println(t.x[0]);
    }
}
OUTPUT -
null
ERROR!
Exception in thread "main" java.lang.NullPointerException: Cannot load from int array because "<local1>.x" is null
	at Test.main(Test.java:9)

class Test {
    int[] x = new int[3];
    public static void main(String[] args) {
        Test t = new Test();
        System.out.println(t.x);
        System.out.println(t.x[0]);
    }
}
OUTPUT - [I@379619aa
0
// Static level
class Test {
    static int[] x;
    public static void main(String[] args) {
        Test t = new Test();
        System.out.println(t.x);
        System.out.println(t.x[0]);
    }
}
OUTPUT - null
ERROR!
Exception in thread "main" java.lang.NullPointerException: Cannot load from int array because "Test.x" is null
	at Test.main(Test.java:9)
//local
class Test {
    int[] x = new int[3];
    public static void main(String[] args) {
        Test t = new Test();
        System.out.println(t.x);
        System.out.println(t.x[0]);
    }
}
OUTOUT - [I@379619aa
0
    

  
