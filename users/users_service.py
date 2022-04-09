import csv
import os
import string
import sys
import bcrypt
from database.valid import password_validation
from database.database import DatabasePermission

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
db_path = os.path.join(current_dir, "database/database.csv")


def check_db_exists(path):
    try:
        os.stat(path)
    except FileNotFoundError:
        f = open(path, "w")
        f.close()


class UserService(DatabasePermission):
    logged = False

    @staticmethod
    def login(obj):
        if obj.login_status:
            print('użytkownik jest już zalogowany')

        with open(db_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for usernames, passwords in csv_reader:
                if obj.name.casefold() == usernames.casefold() and bcrypt.checkpw(obj.password.encode('utf-8'), passwords.encode('utf-8')):
                    print("Jesteś zalogowany!")
                    obj.login_status = True
                    logged = True
                    break
        if not logged:
            print("Niepoprawy login lub hasło")

    @staticmethod
    def check_if_user_login(obj):
        return obj.login_status is True

    def register(self, obj):
        valid = password_validation(password=obj.password)

        if len(set(string.punctuation).intersection(obj.name)) < 0:
            print("Login nie może posiadać znaku specjalnego")
            valid = False

        status = True
        if valid:
            with open(db_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                for usernames, passwords in csv_reader:
                    if obj.name.casefold() == usernames.casefold():
                        status = False
            if status:
                with open(db_path, 'a', newline='\n') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([obj.name, obj.password.decode()])
                    print("Utworzono użytkownika, odpal program ponownie aby się zalogować")
                    return False
            else:
                print("Nazwa użytkownika jest już zajęta")

    def delete_user(self, obj):
        lines = []

        if self.user_has_access(obj):
            with open(db_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    lines.append(row)
                    for field in row:
                        if field == obj.name:
                            lines.remove(row)

            with open(db_path, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(lines)
            print("Usunięto użytkownika:", obj, "- program zostanie zamkniety")
        else:
            print("Brak uprawnienie do usuwania użytkownika")

    @staticmethod
    def list_users():
        with open(db_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            print("\nLista użytkowników: ")
            for i, user in enumerate(list(csv_reader)):
                print("Użytkownik", i, ": ", user[0])

    @staticmethod
    def sortalph():
        user_sort_choice = int(input("\nWpisz 1 aby posortować użytkowników alfabetycznie: "))
        with open(db_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            if user_sort_choice == 1:
                print("\nPosortowana lista użytkowników: ")
                usernames = []
                for user, password in csv_reader:
                    usernames.append(user)
                usernames.sort()
                k = 1
                for username in usernames:
                    print("Użytkownik", k, ": ", username)
                    k += 1
