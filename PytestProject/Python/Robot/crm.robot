*** Settings ****
Documentation   This is some basic info about whole suite
Library         SeleniumLibrary

# Run the script
# robot -d results tests/crm1.robot
*** Variables ***

*** Test Cases ***
Should be able to add new customer
    [Documentation]     This is basic info about test
    [Tags]              1006    Smoke   Contacts
    #open the browser
    log                 Starting the test case!
    Open Browser        https://automationplayground.com/crm/   firefox
    # Initialize tests
    Set Selenium Speed      .2s
    Set Selenium Timeout    10s
    # resize browser window for recording
    Set Window Position    x=341    y=169
    Set Window Size    width=1935    height=1090
    Page Should Contain    Customers Are Priority One
    Click Link          id=SignIn
    Page Should Contain    Login

    Input Text    id=email-id    admin@robotframeworktutorial.com
    Input Text    id=password    qwe
    Click Button  Submit
    Page Should Contain    Our Happy Customers
    Click link                id=new-customer
    Page Should Contain         Add Customer
    
    Input Text    id=EmailAddress    janedoe@gmail.com
    Input Text    id=FirstName      Jane
    Input Text    id=LastName       Doe
    Input Text    id=City           Dallas
    Select From List By Value    id=StateOrRegion   TX
    Select Radio Button    gender    female
    Select Checkbox    name=promos-name
    Click Button    Submit
    Wait Until Page Contains    Success! New customer added.

    Sleep    3s
    Close Browser

*** Keywords ***


(.venv) PS C:\Trainings\Robot-Selenium\MyRobot> robot -d results tests/crm1.robot
