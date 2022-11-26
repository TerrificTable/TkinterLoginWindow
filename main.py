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

db = Database("sql7.freesqldatabase.com", "sql7580994", "3ny5KNafM5", "sql7580994")
if __name__ == "__main__":
    loginWindow(root, db)
