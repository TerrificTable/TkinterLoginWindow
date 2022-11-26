from mysql.connector import MySQLConnection
import customtkinter as ctk
from main import onExit



def loggedInWindow(root, username, connection: MySQLConnection):
    root.withdraw()
    
    loginWindow = ctk.CTkToplevel(root)
    loginWindow.title("Logged in")
    loginWindow.geometry("400x200")
    login_frame = ctk.CTkFrame(loginWindow)
    login_frame.pack(pady=10, padx=30, fill="both", expand=True)
    
    def delete():
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM test WHERE username=%s", (username,))
            confirm = ctk.CTkToplevel(loginWindow)
            confirm.title("Really?")
            confirm.geometry("200x100")
            
            def confirmed():
                connection.commit()
                print(f"Deleted account '{username}'")
                confirm.destroy()
                root.deiconify()
                loginWindow.destroy()

            def notConfirmed():
                confirm.destroy()
            
            ctk.CTkButton(master=confirm, text="Continue", command=confirmed).pack(pady=12, padx=10)
            ctk.CTkButton(master=confirm, text="Cancel", command=notConfirmed).pack(pady=12, padx=10)


    label = ctk.CTkLabel(master=login_frame, text ="You have successfully logged in")
    deleteBtn = ctk.CTkButton(master=login_frame, text="Delete Account", text_color="red", command=delete)
    
    label.pack(pady=12, padx=10)
    deleteBtn.pack(pady=12, padx=10)
    
    loginWindow.protocol('WM_DELETE_WINDOW', onExit)
