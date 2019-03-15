cd /d "C:\Program Files\Autodesk\Maya2018\bin"
mayapy pyside2-uic -o %~dp0duplicate_reference\ui\main_ui.py %~dp0ui\main_ui.ui
cd /d %~dp0