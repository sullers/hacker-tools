#截取屏幕
#pip install pyautogui
import pyautogui

img = pyautogui.screenshot()
img.show()
img.save('demo.jpg')