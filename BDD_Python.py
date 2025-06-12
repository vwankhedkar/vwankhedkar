features\firstDemo1.feature
Feature: login functionality for newtours application
  Scenario: Valid username and password
    Given Open browser
    When providing valid username and password
    Then Verifying home
------------------------------------------------
.\steps\login_method.py
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('open browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/test/newtours/")

@when('providing valid username and password')
def validUserNameAndPassword(context):
    context.driver.find_element(By.NAME, "userName").send_keys("mercury")
    context.driver.find_element(By.NAME, "password").send_keys("mercury")
    context.driver.find_element(By.NAME, "submit").click()

@then('verifying home')
def verify_home(context):
    assert "Login: Mercury Tours" == context.driver.title

(.venv) PS C:\Users\vwank\PycharmProjects\Python_Cucumber> behave features\firstDemo1.feature
Feature: login functionality for newtours application # features/firstDemo1.feature:1

  Scenario: Valid username and password        # features/firstDemo1.feature:2
    Given Open browser                         # steps/login_method.py:5

DevTools listening on ws://127.0.0.1:56030/devtools/browser/235e1fe0-d328-402a-8036-7010cb9dc666
    When providing valid username and password # steps/login_method.py:10
    Then Verifying home                        # steps/login_method.py:16

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m7.186s
(.venv) PS C:\Users\vwank\PycharmProjects\Python_Cucumber> 
********************************************************************************************************
Feature: login functionality for newtours application
  @smoke
  Scenario: Valid username and password
    Given Opening browser
    When providing valid "{username}" and "{password}"
    Then verify title of the page
    Then Verify Success Message
  @regression
  Scenario Outline:
    Given Opening browser
    When providing valid "{username}" and "{password}"
    Then verify title of the page
    Then Verify Success Message
    Examples:
    | username | password |
    | mercury | mercury |
    | abcdfef | peyrhfb |
----------------------------------------------------
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('Opening browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/test/newtours/")

@when('providing valid "{username}" and "{password}"')
def validUserNameAndPassword(context, username, password):
    context.driver.find_element(By.NAME, "{userName}").send_keys(username)
    context.driver.find_element(By.NAME, "{password}").send_keys(password)
    context.driver.find_element(By.NAME, "submit").click()

@then('verify title of the page')
def verify_home(context):
    assert "Login: Mercury Tours" == context.driver.title

@then('Verify Success Message')
def verify_success(context):
    try:
        text = context.driver.find_element(By.XPATH,"//h3[text()='Login Successfully']").text
    except:
        context.driver.close()
        assert False, "Test Case Failed"

    if text == "Login Successfully":
        context.driver.close()
        assert True, "Test case Passed"
(.venv) PS C:\Users\vwank\PycharmProjects\Python_Cucumber> behave features\firstDemo1.feature --tags=smoke,regression,setupTable
(.venv) PS C:\Users\vwank\PycharmProjects\Python_Cucumber> behave features\firstDemo1.feature  
*****************************************************************************************************
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('Opening browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/test/newtours/")

@when('providing valid <username> and <password>')
def validUserNameAndPassword(context, username, password):
    context.driver.find_element(By.NAME, "{userName}").send_keys(username)
    context.driver.find_element(By.NAME, "{password}").send_keys(password)
    context.driver.find_element(By.NAME, "submit").click()

@then('verify title of the page')
def verify_home(context):
    assert "Login: Mercury Tours" == context.driver.title

@then('Verify Success Message')
def verify_success(context):
    try:
        text = context.driver.find_element(By.XPATH,"//h3[text()='Login Successfully']").text
    except:
        context.driver.close()
        assert False, "Test Case Failed"

    if text == "Login Successfully":
        context.driver.close()
        assert True, "Test case Pass"

@when('verify login by using below query')
def step_imp(context):
    for r in context.table:
        context.driver.find_element(By.NAME, "userName").send_keys(r["username"])
        context.driver.find_element(By.NAME, "password").send_keys(r["password"])
        context.driver.find_element(By.NAME, "submit").click()
