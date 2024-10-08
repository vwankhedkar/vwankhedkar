*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
GetAllLinks
    Open Browser    https://swisnl.github.io/jQuery-contextMenu/demo.html    firefox
    Maximize Browser Window
    ${AllLinks}=    Get Element Count    xpath://a
    Log To Console    Total number of links: ${AllLinks}

    @{LinkItems}    Create List

    FOR    ${i}    IN RANGE    1    ${AllLinks + 1}
        ${linkText}=    Get Text    xpath:(//a)[${i}]
        Log To Console    Link ${i}: ${linkText}
    END

**************************************************************************************************

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TableValidation
    Open Browser    https://testautomationpractice.blogspot.com/    firefox
    Maximize Browser Window
    ${rows}=    get element count   xpath://table[@name='BookTable']/tbody/tr
    ${cols}=    get element count   xpath://table[@name='BookTable']/tbody/tr[1]/th

    Log to console  ${rows}
    Log to console  ${cols}

    ${data}=    get text    xpath://*[@name="BookTable"]/tbody/tr
    Log to console  ${data}

****************************************************************************************************

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TableValidation
    Open Browser    https://testautomationpractice.blogspot.com/    firefox
    Maximize Browser Window
    ${rows}=    get element count   xpath://table[@name='BookTable']/tbody/tr
    ${cols}=    get element count   xpath://table[@name='BookTable']/tbody/tr[1]/th

    Log to console  ${rows}
    Log to console  ${cols}

    ${data}=    get text    xpath://table[@name='BookTable']/tbody/tr
    Log to console  ${data}

    table column should contain     xpath://table[@name='BookTable']    2   Author
    table row should contain    xpath://table[@name='BookTable']    4   Learn JS
    table cell should contain   xpath://table[@name='BookTable']    5   2   Mukesh
    table header should contain     xpath://table[@name='BookTable']    BookName

    close browser

