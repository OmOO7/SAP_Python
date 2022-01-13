# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:00:37 2021

@author: 30048669
"""

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
        path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        subprocess.Popen(path)
        time.sleep(10)

        SapGuiAuto = win32com.client.GetObject('SAPGUI')
        if not type(SapGuiAuto) == win32com.client.CDispatch:
            return

        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
            return
        connection = application.OpenConnection("AEL - Local Production", True)

        if not type(connection) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
            return

        session = connection.Children(0)
        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return

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