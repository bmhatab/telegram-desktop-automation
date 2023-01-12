import pyautogui

####STATIC

#x, y = pyautogui.position()

#if x == 1 and y == 1:
 #   print("Cursor is at position (1, 1).")
#else:
 #   print("Cursor is not at position (1, 1). Current position is: " + str((x, y)))


#####LOOP

while True:
    x, y = pyautogui.position()
    print("Cursor is at position: " + str((x, y)))
