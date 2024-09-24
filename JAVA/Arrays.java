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
