import os
import sys
import csv
from database.valid import password_validation

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
rooms_path = os.path.join(current_dir, "./rooms.csv")


class Room:
    def __init__(self, room_id, password, user_admin):
        self.room_id = room_id
        self.password = password
        self.user_admin = user_admin
        self.users_list = []

    def __str__(self):
        return f"Room{self.room_id}"

    def create(self):
        valid = password_validation(self.password)
        if valid:
            with open(rooms_path, 'a', newline='\n') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([self.room_id, self.password.decode(), self.user_admin, self.users_list])
                print("Utworzono pokój o ID:", self.room_id, "Użytkownika:", self.user_admin)

    def join(self, obj, room_id, password):
        if room_id == self.room_id and password == self.password:
            if obj.login_status:
                self.users_list.append(obj.name)
                #TODO: Dopisać do CV
                with open(rooms_path, 'w', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(obj,self.users_list)

                print("Użytkownik został dodany do pokoju")
            else:
                print("Ten uzytkownik nie jest zalogowany")
        else:
            print('Złe hasło do pokoju')

    def delete_room(self, obj):

        lines = []
        with open(rooms_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                lines.append(row)
                for field in row:
                    if field == obj.room_id:
                        lines.remove(row)

        with open(rooms_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(lines)
        print("Usunięto pokój:", obj, "- program zostanie zamknięty")

    def del_user_from_room(self, obj):
        self.users_list.remove(obj.name)

    def show_users(self):
        return self.users_list

