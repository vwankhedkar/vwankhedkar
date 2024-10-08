*** Settings ***
Library    SeleniumLibrary
Resource   ../Resource/login_resources.robot
Library     DataDriver  ../TestData/LoginData.xlsx  sheet_name=Sheet1
Suite Setup  Open my Browser
Suite Teardown  Close Browsers
Test Template  Invalid login

*** Test Cases ***
LoginTestwithExcel      using   ${username} and {password}

*** Keywords ***
Invalid Login
    [Arguments]    ${username}    ${password}
    Input username    ${username}
    Input pwd         ${password}
    Click login button
    Error Message Should Be Visible
          ***************************************************************
TC2
*** Settings ***
Library    SeleniumLibrary
Resource   ../Resource/login_resources.robot
Library     DataDriver  ../TestData/LoginData.csv

Suite Setup  Open my Browser
Suite Teardown  Close Browsers
Test Template  Invalid login

*** Test Cases ***
LoginTestwithExcel      using   ${username} and {password}

*** Keywords ***
Invalid Login
    [Arguments]    ${username}    ${password}
    Input username    ${username}
    Input pwd         ${password}
    Click login button
    Error Message Should Be Visible
          ******************************************************************

../Resource/login_resources.robot

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${LOGIN URL}    https://admin-demo.nopcommerce.com/
${BROWSER}      firefox

*** Keywords ***
Open my Browser
    open browser    ${LOGIN URL}    ${BROWSER}
    maximize browser window

Close Browsers
    close all browsers

Open Login Page
    go to   ${LOGIN URL}

Input username
    [Arguments]  ${username}
    input text  id:Email    ${username}

Input pwd
    [Arguments]  ${passowrd}
    input text  id:Password     ${password}

Click login button
    click element   xpath://input[@class='button-1 Login-button']

Click logout link
    click link  logout

Error message should be visible
    page should contain     Login was unsuccessful

Dashboard page should be visible
    page should contain     Dashboard
