*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
MultipleBrowsers
    open browser    https://opensource-demo.orangehrmlive.com/     firefox
    maximize browser window
    input text  xpath:/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input   Admin
    input text  name:password   admin123

    capture element screenshot xpath://*[@id="divLogo"]/img   C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase\Screeshot\scr1.png
    capture page screenshot C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase\Screeshot\scr2.png

--------------------------- *************** --------------------------------

*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
MouseActions
    #Right click / open context menu
    open browser    https://swisnl.github.io/jQuery-contextMenu/demo.html   firefox
    maximize browser window
    open context menu   xpath://span[@class='context-menu-one btn btn-neutral']
    sleep   3

    #Double click action
    go to   https://testautomationpractice.blogspot.com/
    #maximize bowser window
    double click element    xpath://button[contains(text(),'Copy Text')]
    sleep   3

    # Drag and Drop
    go to   http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    #maximize browser window
    drag and drop   id:box3     id:box101
    sleep   5
