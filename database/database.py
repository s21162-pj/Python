import string
import getpass
import os
import sys
import csv
from users.users_service import login

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
rooms_path = os.path.join(current_dir, "./rooms.csv")

class RoomCreate():


    def create(self):
        def long_enough(roomPassword):
            # Przynajmniej 6 znakow
            return len(roomPassword) >= 6

        def has_uppercase(roomPassword):
            # Przynajmniej jedna duża litera
            return len(set(string.ascii_uppercase).intersection(roomPassword)) > 0

        def has_numeric(roomPassword):
            # Musi zawierać cyfrę
            return len(set(string.digits).intersection(roomPassword)) > 0

        def has_special(roomPassword):
            # Musi zawierać znak specjalny
            return len(set(string.punctuation).intersection(roomPassword)) > 0
        roomOwner = login.username
        roomID = 1
        with open(rooms_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for roomsID, roomsPassword, roomsOwner in csv_reader:
                while roomID <= roomsID:
                    roomID += 1

        roomPassword = getpass.getpass("Podaj hasło: ")
        roomPassword2 = getpass.getpass("Ponownie podaj hasło: ")
        if roomPassword == roomPassword2 and long_enough(roomPassword) and has_uppercase(roomPassword) and has_numeric(
                roomPassword) and has_special(roomPassword):
            with open(rooms_path, 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([roomID, roomPassword, roomOwner])
                print("Utworzono pokój o ID:", roomID,"Użytkownika:", roomOwner)


roomCreate = RoomCreate()



