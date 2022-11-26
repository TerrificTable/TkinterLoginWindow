from mysql.connector import MySQLConnection
import customtkinter as ctk


def registerWindow(root, connection: MySQLConnection):
    root.withdraw()

    registerWindow = ctk.CTkToplevel(root)
    registerWindow.title("Register")
    registerWindow.geometry("600x350")
    
    register_frame = ctk.CTkFrame(registerWindow)
    register_frame.pack(pady=20, padx=60, fill="both", expand=True)
    
    label = ctk.CTkLabel(master=register_frame, text="Register", text_font=("Roboto", 24))
    entry1 = ctk.CTkEntry(master=register_frame, width=300, placeholder_text="Username")
    entry2 = ctk.CTkEntry(master=register_frame, width=300, placeholder_text="Password", show="*")

    def register():
        username = entry1.get()
        password = entry2.get()

        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO test (`username`, `password`) VALUES (%s, %s)", (username, password))
            connection.commit()
            registerWindow.destroy()
            root.deiconify()
            
    def openRoot():
        root.deiconify()
        registerWindow.destroy()
    registerWindow.protocol('WM_DELETE_WINDOW', openRoot)

    
    registerBtn = ctk.CTkButton(master=register_frame, text="Register", width=250, command=register)

    label.pack(pady=12, padx=10)
    entry1.pack(pady=12, padx=10)
    entry2.pack(pady=12, padx=10)
    registerBtn.pack(pady=0, padx=10)

