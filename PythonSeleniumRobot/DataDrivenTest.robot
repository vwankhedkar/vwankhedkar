login_resources.robot

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
                              *******************************************
Login_TC.robot
--------------

*** Settings ***
Library    SeleniumLibrary
Resource   ../Resource/login_resources.robot
Suite Setup    Open My Browser
Suite Teardown    Close Browsers
Test Template    Invalid Login

*** Test Cases ***          username                password
Right user empty pass       admin@youstore.com      ${EMPTY}
Right user wrong pass       admin@youstore.com      xyz
Wrong user right pass       wronguser@youstore.com  admin
Wrong user empty pass       wronguser@youstore.com  ${EMPTY}
Wrong user wrong pass       wronguser@youstore.com  xyz

*** Keywords ***
Invalid Login
    [Arguments]    ${username}    ${password}
    Input Username    ${username}
    Input Pwd         ${password}
    Click Login Button
    Error Message Should Be Visible
