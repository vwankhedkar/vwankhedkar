package com.test;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testing.annotations.AfterMethod;
import org.testing.annotations.BeforeMethod;
import org.testing.annotations.Test;

public class GoodTest {
	
	WebDriver driver;
	
	//1   //4  //7
	@BeforeMethod
	public void SetUp() {
		System.setProperty("webdriver.chrome.driver", "c:/Downloads/chromedriver");
		driver = new ChromeDriver(); // launch chrome
		driver.manage().window().maximize();
		driver.manage().deleteAllCookies();
		drive.manage().timeouts().pageLoadTimeout(40, TimeUnit.SECONDS);
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		driver.get("https://www.google.com");
	}
	
	// 2
	@Test(priority=1,groups="Title")
	public void googleTitleTest() {
		String title = driver.getTitle();
		System.out.println(title);	
	}
	
	// 8
	@Test(priority=3,groups="Logo")
	public static void googleLogoTest() {
		boolean b = driver.findElement(By.xpath("//*[@id='hplogo']")).isDisplayed();
	}
	
	// 5
	@Test(priority=2,groups="Link Test")
	public void mailLickTest() {
		boolean b = driver.findElement(By.linkText("Mail")).isDisplayed();
	}

	@Test(priority=4,groups="Test")
	public void test1() {
		System.out.println("test1");
	}

	@Test(priority=5,groups="Test")
	public void test2() {
		System.out.println("test2");
	}
	
	@Test(priority=3,groups="Test")
	public void test3() {
		System.out.println("test3");
	}
	
	//3  //6   //9
	@AfterMethod
	public void tearDown()	{
		driver.quit();
	}
}

