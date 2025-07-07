package com.tryPrograms;
public class LambdaProgs {
	public static void main(String[] args) {
		Runnable r = () -> System.out.print("Hello Lambda");
		new Thread(r).start();
	}
}    =====>    Hello Lambda
**********************************************************************
package com.tryPrograms;
import java.util.Arrays;
import java.util.List;
public class LambdaProgs {
	public static void main(String[] args) {
		List<String> list = Arrays.asList("Java", "Spring", "Lambda");
		list.forEach(item -> System.out.println(item));
	}
}  
Java
Spring
Lambda
**********************************************************************
package com.tryPrograms;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
public class LambdaProgs {
	public static void main(String[] args) {
		List<String> list = Arrays.asList("Java", "JavaScript", "Python");
		List<String> filteredList = list.stream().filter(s->s.startsWith("J"))
												.collect(Collectors.toList());
		filteredList.forEach(System.out::println);
	}
}
Java
JavaScript
**********************************************************************
package com.tryPrograms;
public class LambdaProgs {
	@FunctionalInterface
	interface Calculator {
		int calculate(int a, int b);
	}
    public static void main(String[] args) {
        Calculator add = (a, b) -> a + b;
        Calculator multiply = (a, b) -> a * b;
        System.out.println("Addition: " + add.calculate(5, 3));
        System.out.println("Multiplication: " + multiply.calculate(5, 3));
    }
}
Addition: 8
Multiplication: 15
**********************************************************************
package com.tryPrograms;
import java.util.Arrays;
import java.util.List;
public class LambdaProgs {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("Java", "Lambda", "Kafka");
        list.sort((s1, s2) -> s1.compareTo(s2)); // Correct lambda syntax
        list.forEach(System.out::println);
    }
}
Java
Kafka
Lambda
**********************************************************************
package com.tryPrograms;
import java.util.HashMap;
import java.util.Map;
public class LambdaProgs {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        map.put("Java", 8);
        map.put("Spring", 5);
        map.put("Lambda", 1);
        map.forEach((key, value) -> System.out.println(key+": "+value));
    }
}
Java: 8
Spring: 5
Lambda: 1
**********************************************************************
package com.tryPrograms;
public class LambdaProgs {
    public static void main(String[] args) {
        new Thread(() -> System.out.println("Thread with Lambda!")).start();
    }
}
Thread with Lambda!
**********************************************************************
package com.tryPrograms;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
public class LambdaProgs {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("Java", "Lambda", "Kafka");
        list.sort(Comparator.comparingInt(String::length));
        list.forEach(System.out::println);
    }
}
Java
Kafka
Lambda
**********************************************************************
package com.tryPrograms;
import java.util.Optional;
public class LambdaProgs {
    public static void main(String[] args) {
        Optional<String> optional = Optional.of("Java");
        optional.ifPresent(s -> System.out.println("Value is present: " + s));
    }
}
Value is present: Java
**********************************************************************
package com.tryPrograms;
import java.util.function.Predicate;
public class LambdaProgs {
    public static void main(String[] args) {
        Predicate<String> isEmpty = s -> s.isEmpty();
        System.out.println(isEmpty.test(""));
        System.out.println(isEmpty.test("Java"));
    }
}
true
false
**********************************************************************
package com.tryPrograms;
import java.util.function.BiFunction;
public class LambdaProgs {
    public static void main(String[] args) {
        BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;
        System.out.println(add.apply(2, 3));
    }
}	====>	5
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
**********************************************************************

**********************************************************************

**********************************************************************
