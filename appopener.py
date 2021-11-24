def openapp():
    chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    import sys
    import subprocess
    import webbrowser
    print("+=========Hello! I will open the app of your choice!=========+")
    while True:
        opener = input("What app do you want to open? ")
        if opener == "chrome beta":
            subprocess.Popen("C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe")

        elif opener == "word":
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

        elif opener == "notepad":
            subprocess.Popen("C:\\Windows\\notepad.exe")

        elif opener == "wordpad":
            subprocess.Popen("C:\\Windows\\write.exe")

        elif opener == "file explorer":
            subprocess.Popen("C:\\Windows\\explorer.exe")

        elif opener == "brother iprint and scan":
            subprocess.Popen("C:\\Program Files (x86)\\Brother\\iPrint&Scan\\Brother iPrint&Scan.exe")

        elif opener == "onedrive":
            subprocess.Popen("C:\\Program Files (x86)\\Microsoft OneDrive\\OneDrive.exe")

        elif opener == "math input panel":
            subprocess.Popen("C:\\Program Files\\Common Files\\Microsoft Shared\\Ink\\mip.exe")

        elif opener == "zoom":
            subprocess.Popen("C:\\Users\\ybarv\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

        elif opener == "calculator":
            subprocess.Popen("C:\\Windows\\System32\\calc.exe")

        elif opener == "vs code insiders":
            subprocess.Popen("C:\\Users\\ybarv\\AppData\\Local\\Programs\\Microsoft VS Code Insiders\\Code - Insiders.exe")

        elif opener == "teams":
            subprocess.Popen("C:\\Users\\ybarv\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe")

        elif opener == "excel":
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

        elif opener == "access":
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE")

        elif opener == "onenote":
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE")

        elif opener == "skype for business":
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\lync.exe")

        elif opener == "publisher":
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\MSPUB.EXE")

        elif opener == "outlook":
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")

        elif opener == "powerpoint":
            subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

        elif opener == "paint":
            subprocess.Popen("C:\\Windows\\system32\\mspaint.exe")

        elif opener == "system info":
            subprocess.Popen("C:\\Windows\\system32\\msinfo32.exe")

        elif opener == "cmd":
            subprocess.Popen("C:\\Windows\\System32\\cmd.exe")

        elif opener == "powershell":
            subprocess.Popen("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")

        elif opener == "powershell 7":
            subprocess.Popen("C:\\Program Files\\PowerShell\\7\\pwsh.exe")

        elif opener == "acrobat reader":
            subprocess.Popen("C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe")

        elif opener == "chrome":
            subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
        
        elif opener == "exit":
            yesorno = input("Are you sure that you want to exit?")
            if yesorno == "yes":
                sys.exit("Exited")
            
            elif yesorno == "no":
                print("Ok!")
                openapp()

        elif opener == "help":
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open_new_tab("file:///C:/Users/ybarv/source/repos/testfornow/openanapp.html")
        else:
            print("Please enter the name of a supported app. (Type help to see all supported apps.)")

