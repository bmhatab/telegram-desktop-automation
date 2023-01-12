import os
import subprocess
import time
import pyautogui
from main.config import Config

accounts = Config.accounts


def add_to_group():
    add_to_group_path = os.path.join(os.getcwd(), "actions", "add_to_group.py")
    if os.path.isfile(add_to_group_path) and os.access(add_to_group_path, os.R_OK):
        with open(add_to_group_path, 'r') as f:
            exec(f.read())
    else:
        print(f"{add_to_group_path} not found or not accessible")

if __name__ == "__main__":
    add_to_group()
