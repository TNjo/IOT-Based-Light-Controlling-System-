import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tkinter as tk

# Fetch the service account key JSON file contents
cred = credentials.Certificate('cred.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://light-control-f9cd1-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/Update')


def update_database(value):
    ref.set(value)
    print(f"Database updated with value: {value}")


def gui():
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Light Control")

    # Create a button to turn on the light
    btn_on = tk.Button(root, text="ON", command=lambda: update_database(1), bg='Green', width=10,
                       font=('Arial', 14, 'bold'))
    btn_on.pack(pady=50)

    # Create a button to turn off the light
    btn_off = tk.Button(root, text="OFF", command=lambda: update_database(0), bg='red', width=10,
                        font=('Arial', 14, 'bold'))
    btn_off.pack(pady=50)

    root.mainloop()


if __name__ == "__main__":
    gui()
