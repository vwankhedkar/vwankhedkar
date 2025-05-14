*** Settings ***
Library           SeleniumLibrary
Test Teardown     Close Browser

*** Variables ***
${BROWSER}        chrome
${URL}            https://demo.nopcommerce.com

*** Test Cases ***
Login Test
    Open Browser    ${URL}    ${BROWSER}
    Login To Application

*** Keywords ***
Login To Application
    Click Link    xpath://a[@class='ico-login']
    Input Text    xpath://input[@class='email']      pavanoltraining@gmail.com
    Input Text    xpath://input[@class='password']   Test@123
    Click Button  xpath://button[@class='button-1 login-button']
**********************************************************************************
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}          https://demo.nopcommerce.com
${email_txt}    xpath://input[@class='email']

*** Test Cases ***
TestingInputBox
    Open Browser    ${url}      ${browser}
    Maximize Browser Window
    Title Should Be    nopCommerce demo store. Home page title
    Click Link    xpath://a[@class='ico-login']
    Wait Until Element Is Visible    ${email_txt}    timeout=10s
    Element Should Be Enabled    ${email_txt}
    Input Text    ${email_txt}    JohnDavid@gmail.com
    Sleep    5
    Clear Element Text    ${email_txt}
    Sleep    3
    Close Browser

