*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}      https://www.newtours.demoaut.com/
${browser}  firefox

*** Test Cases ***
TC1
    ${PageTitle}=    launchBrowser      ${url}      ${browser}
    log to  ${PageTitle}
    input text      name:username   mercury
    input text      name:password   mercury

*** Keywords ***
launchBrowser
    [Arguments]     ${appurl1}    ${appbrowser}
    open browser    ${appurl1}    ${appbrowser}
    maximize browser window
    ${title}=   get title
    [Return]    ${title}
**********************************************************************************
Seperate resources file 

*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}      https://www.newtours.demoaut.com/
${browser}  firefox

*** Test Cases ***
TC1
    ${PageTitle}=    launchBrowser      ${url}      ${browser}
    log to  ${PageTitle}
    input text      name:username   mercury
    input text      name:password   mercury

Resources.robot
*** Settings ***
Library  SeleniumLibrary
Resources       ../Resources/resources.robot

*** Keywords ***
launchBrowser
    [Arguments]     ${appurl1}    ${appbrowser}
    open browser    ${appurl1}    ${appbrowser}
    maximize browser window
    ${title}=   get title
    [Return]    ${title}
