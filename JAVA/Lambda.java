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
