package com.test;
import java.util.concurrent.TimeUnit;
import org.testing.annotations.Test;


public class InvocationTimeOut {
	@Test(invocationTimeOut=2000)   // execute this infinite loop for 2 seconds
	public void infiniteLoopTest() {
		int  i = 1;
		while (i==1) {
		System.out.println(i);
		}
	}
}
************************************************************************

package com.test;

import org.testng.annotations.Test;

public class ExceptionTimeoutTest() {
	
	@Test(expectedException=NumberFormatException.class)
	public void Test1() {
		String x = "1004";
		Integer.parseInt(x);
	}
}
