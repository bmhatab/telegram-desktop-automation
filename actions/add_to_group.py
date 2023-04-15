import os
import pyautogui as pg
import subprocess
import time as t
import pandas as pd
import openpyxl
from main.config import Config

count = Config.count
end_count = Config.end_count
accounts = Config.accounts

excel_path = os.path.join(os.getcwd(),"actions/data.xlsx")



for i in range(1, accounts+1):
        folder_name = "telegram account " + str(i)
        app_dir = os.path.join(os.getcwd(), "actions/Telegram Accounts", folder_name, "Telegram_Portable.exe")
        excel_data = pd.read_excel(excel_path, sheet_name='Sheet1')

        if os.path.exists(app_dir):
            current_window = subprocess.Popen(app_dir)
            # Wait for the window to appear
            t.sleep(4)
        # pyautogui.hotkey('alt', 'tab')
        
            # Get the currently active window
            active_window = pg.getActiveWindow()
            t.sleep(2)
            # Get the current x and y coordinates of the window
            x, y = active_window.left, active_window.top
            #Move the window to the top-left corner of the screen (0, 0)
            pg.moveTo(x, y, duration=0.5)
            t.sleep(1)
            # Drag the object to the top-left corner of the screen (0, 0)
            pg.dragTo(1, 1, button='left', duration=0.5)
            t.sleep(2)
            x, y = active_window.right, active_window.bottom
            pg.moveTo(x, y, duration=0.5)
            t.sleep(2)
            print(x,y)
            pg.dragTo(652, 525, button='left', duration=0.5)
            print(f'{app_dir} launched successfully')

             # Move to menu bar
            t.sleep(2)
            pg.moveTo(25,51,duration=0.5)
            pg.leftClick()
            #Move to saved messages
            t.sleep(2)
            pg.moveTo(73,343,duration=0.5)
            pg.leftClick()
            #Type group name 
            t.sleep(1)
            pg.write(Config.main_group)
            t.sleep(1)
            pg.press("enter")
            #Click view Group
            t.sleep(2)
            pg.moveTo(466,452,duration=0.5)
            pg.leftClick()

            for column in excel_data['Usernames'].tolist():
                #if count >= end_count:
                   # end_count = count + end_count
                   # current_window.terminate()
                   # break

                # Move to TITLE
                t.sleep(2)
                pg.moveTo(363,45,duration=0.5)
                pg.leftClick()

                #Click options
                t.sleep(1)
                pg.moveTo(451,71,duration=0.5)
                pg.leftClick()

                #Select add members
                pg.moveTo(367,103,duration=0.5)
                pg.leftClick()
                t.sleep(3)
                #Write username in search box
                pg.write(str(excel_data['Usernames'][count]))
                t.sleep(2)

                #move to first username
                pg.moveTo(232,158,duration=0.5)
                pg.leftClick()

                #move to add button
                t.sleep(1)
                pg.moveTo(469,486,duration=0.5)
                pg.leftClick()

                t.sleep(2)

                pg.leftClick()

                pg.moveTo(484,102,duration=0.5)
                pg.leftClick()
                t.sleep(3)

               
                count = count+1
                print(count)
            
        else:
            print(f"Application not found at this location:{app_dir}")


   



