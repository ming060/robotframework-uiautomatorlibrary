*** Settings ***
Documentation     This demo project is aim to help you start with uiautomatorlibrary.
Library           uiautomatorlibrary

*** Test Cases ***
Check Version
    [Documentation]    This test case is not really a test.
    ...
    ...    It is just a demo for uiautomatorlibrary.
    ...
    ...    This test case will install the F-Droid application and check the version.
    ...
    ...    Then uninstall it.
    # Install F-Droid
    Install    ${CURDIR}${/}FDroid_0.66.apk
    # Open the Application through adb command
    Execute Adb Shell Command    am start -W org.fdroid.fdroid/org.fdroid.fdroid.FDroid
    # Wait loading over
    ${is_loading_over}    Wait Until Gone    30000    text=Please Wait
    Should Be True    ${is_loading_over}    Loading over 10 seconds.
    # Check F-Droid text
    ${is_text_exist}    Wait For Exists    3000    text=F-Droid
    Should Be True    ${is_text_exist}    Text does not exist.
    Click    description=More options
    Click    text=About
    ${is_version_correct}    Wait For Exists    2000    text=0.66
    Should Be True    ${is_version_correct}
    Click    text=OK
    [Teardown]    Run keywords    Run Keyword If Test Failed    Screenshot    AND    Uninstall

*** Keywords ***
Uninstall
    #Uninstall the Application
    uiautomatorlibrary.Uninstall    org.fdroid.fdroid
