# Importing the Libraries

import win32com.client
import sys
import subprocess
import time
import os

# This function will Login to SAP from the SAP Logon window
vTcode = "fbl3n"
vGL = "123"
def saplogin(arg1,arg2):

    try:
        SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine  
        session = SapGui.FindById("ses[0]")  
    
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = "AUTO10002"
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "Sep@2021"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]").maximize
        session.findById("wnd[0]/tbar[0]/okcd").text = arg1
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtSD_SAKNR-LOW").text = arg2
        session.findById("wnd[0]/usr/ctxtSD_SAKNR-LOW").caretPosition = 5

    except:
        os.system("taskkill /F /im SAPLOGON.exe")


    finally:
        session = None
        connection = None
        application = None
        SapGuiAuto = None


saplogin(vTcode,vGL)