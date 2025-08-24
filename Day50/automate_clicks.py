#nao roda no wsl usar powershell

import pyautogui
import time

time.sleep(2)
x, y = 1057, 1067
pyautogui.click(x, y)
print(f"Cliquei na primeira posição {x}, {y}")

time.sleep(5)
x, y = 1894, 142
pyautogui.click(x, y)
print(f"Cliquei na segunda posição {x}, {y}")

#clicar
# x, y = pyautogui.position()
# pyautogui.click(x, y)
# print(f"Cliquei na posição {x}, {y}")
