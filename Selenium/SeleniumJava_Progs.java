package com.PractiseProgs;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.Point;
import org.openqa.selenium.firefox.FirefoxDriver;
public class openHTML {
	public static void main(String[] args) throws InterruptedException {
		FirefoxDriver driver = new FirefoxDriver();
		driver.get("https://www.google.com");
		Thread.sleep(2000);
		Dimension d = new Dimension(200, 200);
		driver.manage().window().setSize(d);
		Thread.sleep(2000);
		Point p = new Point(300,200);
		driver.manage().window().setPosition(p);
		Thread.sleep(2000);
		driver.manage().window().maximize();
		driver.quit();
	}

}
