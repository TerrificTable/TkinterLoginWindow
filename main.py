from mysql.connector import MySQLConnection
from loginwindow import loginWindow
from database import Database
import customtkinter as ctk
import sys


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("600x350")

def onExit():
    sys.exit()

db = Database("<mysql host>", "<mysql username>", "<mysql password>", "<database name>")
if __name__ == "__main__":
    loginWindow(root, db)
