*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
RegTest
    ${speed}=    Get Selenium Speed
    Log To Console    Current Speed: ${speed}
    Open Browser    https://demowebshop.tricentis.com/register    firefox
    Maximize Browser Window
    Set Selenium Speed    2 seconds
    Select Radio Button    Gender   M
    Input Text    name:FirstName    ABC
    Input Text    name:LastName    PQR
    Input Text    name:Email    ABC@gmail.com
    Input Text    name:Password    ABCPQR
    Input Text    name:ConfirmPassword    ABCPQR
    ${speed}=    Get Selenium Speed
    Log To Console    Updated Speed: ${speed}

            ------------------- ************** ---------------------------------

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
RegTest
    Open Browser    https://demowebshop.tricentis.com/register    firefox
    Maximize Browser Window
    wait until page contains    Register    #5 sec
    Select Radio Button    Gender   M
    Input Text    name:FirstName    ABC
    Input Text    name:LastName    PQR
    Input Text    name:Email    ABC@gmail.com
    Input Text    name:Password    ABCPQR
    Input Text    name:ConfirmPassword    ABCPQR
---------------------------*******************-------------------------------

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
RegTest
    Open Browser    https://demowebshop.tricentis.com/register    firefox
    Maximize Browser Window
    ${time} =   get selenium timeout
    log to console      ${time}

    set selenium timeout    10 seconds
    wait until page contains    Registeration    #5 sec
    Select Radio Button    Gender   M
    Input Text    name:FirstName    ABC
    Input Text    name:LastName    PQR
    Input Text    name:Email    ABC@gmail.com
    Input Text    name:Password    ABCPQR
    Input Text    name:ConfirmPassword    ABCPQR
    close browser
---------------------------------------*************************--------------------------

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
RegTest
    Open Browser    https://demowebshop.tricentis.com/register    firefox
    Maximize Browser Window

    ${implicittime}=    get selenium implicit wait
    log to console     ${implicittime}

    set selenium implicit wait  10 seconds

    ${implicittime}=    get selenium implicit wait
    log to console     ${implicittime}

    Select Radio Button    Gender   M
    Input Text    name:FirstName    ABC
    Input Text    name:LastName    PQR
    Input Text    name:Email    ABC@gmail.com
    Input Text    name:Password    ABCPQR
    Input Text    name:ConfirmPassword    ABCPQR
    close browser
------------------------------   Multiple Browsers ------------------------
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
MyTestCase
    Open Browser    https://demowebshop.tricentis.com/register    firefox
    Maximize Browser Window

    Open Browser    https://automationpractice.com/index.php    firefox
    Maximize Browser Window

    Close All Browsers
