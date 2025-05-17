TC7.robot

*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
MyTestCase
    open browser        https://demowebshop.tricentis.com/register  headlessfirefox
    maximize browser window

    open browser        https://www.softwaretestingmaterial.com/sample-webpage-to-automate/     headlessfirefox
    maximize browser window

    close all browsers

TC8.robot

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
HandlingAlerts
    open browser        https://testautomationpractice.blogspot.com/    headlesschrome
#    click element       id://*[@id="HTML9"]/div[1]/button
#    sleep       3
#    handle alert        accept
    click element       id:promptBtn
    sleep       3
    handle alert        dismiss
#    click element       id:confirmBtn
#    sleep       3
#    handle alert        Leave
    alert should not be present    Press a button!

(.venv) PS C:\Users\vwank\PycharmProjects\PythonProject4\TestCases\Pabot> pabot --processes 2 --outputdir Results *.robot

Robot Framework remote server at 127.0.0.1:8270 started.
2025-05-17 16:13:14.286110 [PID:14852] [0] [ID:1] EXECUTING Suites.TC8
2025-05-17 16:13:14.286398 [PID:21808] [1] [ID:0] EXECUTING Suites.TC7

DevTools listening on ws://127.0.0.1:51753/devtools/browser/b16a7645-8240-41e9-b50c-5bb9341b9665
2025-05-17 16:13:30.012739 [PID:21808] [1] [ID:0] still running Suites.TC7 after 15.0 seconds
2025-05-17 16:13:30.012838 [PID:14852] [0] [ID:1] still running Suites.TC8 after 15.0 seconds
2025-05-17 16:13:42.998493 [PID:14852] [0] [ID:1] PASSED Suites.TC8 in 26.1 seconds
2025-05-17 16:13:52.112310 [PID:21808] [1] [ID:0] still running Suites.TC7 after 35.0 seconds
2025-05-17 16:14:00.656949 [PID:21808] [1] [ID:0] PASSED Suites.TC7 in 43.5 seconds
2 tests, 2 passed, 0 failed, 0 skipped.
===================================================
Output:  C:\Users\vwank\PycharmProjects\PythonProject4\TestCases\Pabot\Results\output.xml
Log:     C:\Users\vwank\PycharmProjects\PythonProject4\TestCases\Pabot\Results\log.html
Report:  C:\Users\vwank\PycharmProjects\PythonProject4\TestCases\Pabot\Results\report.html
Stopping PabotLib process
Robot Framework remote server at 127.0.0.1:8270 stopped.
PabotLib process stopped
Total testing: 1 minute 9.59 seconds
Elapsed time:  47.72 seconds
(.venv) PS C:\Users\vwank\PycharmProjects\PythonProject4\TestCases\Pabot> 
