// corresponding class names for array types
class Test {
    public static void main(String[] args)
    {
        int[] x = new int[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT -    [I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [[I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [B

class Test {
    public static void main(String[] args)
    {
        boolean[] x = new boolean[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [Z

// corresponding class names for array types
class Test {
    public static void main(String[] args)
    {
        int[] x = new int[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT -    [I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [[I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [B

// corresponding class names for array types
class Test {
    public static void main(String[] args)
    {
        int[] x = new int[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT -    [I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [[I

class Test {
    public static void main(String[] args)
    {
        byte[] x = new byte[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [B

class Test {
    public static void main(String[] args)
    {
        short[] x = new short[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [S

class Test {
    public static void main(String[] args)
    {
        double[] x = new double[3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - [D

class Test {
    public static void main(String[] args)
    {
        int[] x = new int[-3];
        System.out.println(x.getClass().getName());
    }
}
OUTPUT - ERROR!
Exception in thread "main" java.lang.NegativeArraySizeException: -3
	at Test.main(Test.java:7)

class Test {
    public static void main(String[] args)
    {
        int[] x = new int[2147483648];
    }
}
OUTPUT - /tmp/532ypyp8YG/Test.java:7: error: integer number too large
        int[] x = new int[2147483648];

class Test {
    public static void main(String[] args)
    {
        int[] x = new int[2147483647];
       // System.out.println(x.getClass().getName());
    }
}
OUTPUT - Exception in thread "main" ERROR!
java.lang.OutOfMemoryError: Requested array size exceeds VM limit
	at Test.main(Test.java:7)

class Test {
    public static void main(String[] args)
    {
        int[][] a = new int[2][];
        System.out.println(a);
        System.out.println(a[0]);
        System.out.println(a[0][0]);
    }
}
OUTPUT - [[I@379619aa
null
ERROR!
Exception in thread "main" java.lang.NullPointerException: Cannot load from int array because "<local1>[0]" is null
	at Test.main(Test.java:10)

class Test {
    public static void main(String[] args)
    {
        int[] a = {10, 20, 30, 40, 50};
        int[] b = {70, 80};
        a = b;
        System.out.println(a);
        b = a;
        System.out.println(b);
    }
}
OUTPUT -[I@379619aa
[I@379619aa

