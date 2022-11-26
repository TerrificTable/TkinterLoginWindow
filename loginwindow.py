from registerwindow import registerWindow
from loggedinwindow import loggedInWindow
from mysql.connector import connect
from database import Database
import customtkinter as ctk


def loginWindow(root, db: Database):
    with connect(host=db.host, username=db.username, password=db.password, database=db.database) as connection:
        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Login", text_font=("Roboto", 24))
        entry1 = ctk.CTkEntry(master=frame, width=300, placeholder_text="Username")
        entry2 = ctk.CTkEntry(master=frame, width=300, placeholder_text="Password", show="*")

        error = ctk.CTkLabel(master=frame, text="", text_color="red")
        

        def login():
            error.set_text("")
            username = entry1.get()
            password = entry2.get()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM test")
                for data in cursor:
                    if (username != data[1] and password != data[2]):
                        error.set_text("Invalid credentials")
                    else:
                        print("Logged in")
                        loggedInWindow(root, username, connection)
                        error.set_text("")
        def showRegisterWin():
            registerWindow(root, connection)
            error.set_text("")

                        
        error.set_text("")
        button = ctk.CTkButton(master=frame, text="Login", width=250, command=login)
        register = ctk.CTkButton(master=frame, text="Register", width=250, command=showRegisterWin)
        
        label.pack(pady=12, padx=10)
        entry1.pack(pady=12, padx=10)
        entry2.pack(pady=12, padx=10)
        error.pack(pady=0, padx=10)
        button.pack(pady=12, padx=10)
        register.pack(pady=0, padx=10)

        root.mainloop()

