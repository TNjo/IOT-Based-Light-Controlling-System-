import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial

# Fetch the service account key JSON file contents
cred = credentials.Certificate('cred.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://light-control-f9cd1-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/Update')

ser = serial.Serial('COM3', 9600)


def read_database():
    return ref.get()


if __name__ == "__main__":

    previous_value = None

    while True:
        current_value = read_database()

        if current_value != previous_value:
            print(current_value)

            ser.write(str(current_value).encode('utf-8'))

            previous_value = current_value
