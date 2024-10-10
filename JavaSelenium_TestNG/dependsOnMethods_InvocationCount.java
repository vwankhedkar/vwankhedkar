package com.test;
import java.util.concurrent.TimeUnit;
import org.testing.annotations.Test;


public class TestNgFeatures {
	
	@Test
	public void loginTest() {
		System.out.println("Login Test")
		int i = 9 / 0;   // if this fails tests won't proceed
	}
	
	@Test(dependsOnMethods="loginTest")
	public void homePageTest() {
		System.out.println("HomePageTest")	
	}
	
	@Test(dependsOnMethods="loginTest")
	public void searchPageTest() {
		System.out.println("SearchPageTest")	
	}
	
	@Test(dependsOnMethods="loginTest")
	public void RegPageTest() {
		System.out.println("RegistrationPageTest")	
	}
}

*******************************************************************

package com.test;
import java.util.concurrent.TimeUnit;
import org.testing.annotations.Test;


public class InvocationCountTest {
	@Test(invocationCount=10)   // execute this method 10 times
	public void sum() {
		int  a = 10;
		int b = 20;
		int c = a + b ;
		System.out.println("Sum= "+ c);
	}
}
