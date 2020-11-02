# Install dependancies: pip install -r requirements.txt
# Run the program : python main.py
import pyautogui
import time
import platform

os = platform.system()    
username_pos = pyautogui.locateCenterOnScreen('images/'+os+'/username.png')
sword_pos = pyautogui.locateCenterOnScreen('images/'+os+'/password.png')
connect_pos = pyautogui.locateCenterOnScreen('images/'+os+'/connect.png')

# replace username and password with your credentials
pyautogui.click(username_pos)
pyautogui.typewrite('username', interval=0.05)
pyautogui.click(password_pos)
pyautogui.typewrite('password', interval=0.05)
pyautogui.click(connect_pos)