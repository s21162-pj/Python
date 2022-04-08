import csv
import os
import string
import sys
import getpass

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
db_path = os.path.join(current_dir, "./database.csv")


def check_db_exists(path):
    try:
        os.stat(path)
    except FileNotFoundError:
        f = open(path, "w")
        f.close()


class Login:

    def logincheck(self):
        username = input("Podaj login: ")
        password = getpass.getpass("Podaj hasło: ")
        with open(db_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for usernames, passwords in csv_reader:
                if username.casefold() == usernames.casefold() and password == passwords:
                    print("Jesteś zalogowany!")
                    return True
        print("Niepoprawy login lub hasło")
        Login().logincheck()


    def list(self):
        with open(db_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            print("\nLista użytkowników: ")
            k = 1
            for user, password in csv_reader:
                print("Użytkownik", k, ": ", user)
                k += 1

    def sortalph(self):
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


login = Login()

class Register:
    def newuser(self):
        def long_enough(password):
            # Przynajmniej 6 znakow
            return len(password) >= 6

        def has_uppercase(password):
            # Przynajmniej jedna duża litera
            return len(set(string.ascii_uppercase).intersection(password)) > 0

        def has_numeric(password):
            # Musi zawierać cyfrę
            return len(set(string.digits).intersection(password)) > 0

        def has_special(password):
            # Musi zawierać znak specjalny
            return len(set(string.punctuation).intersection(password)) > 0

        def has_not_special(username):
            # Login nie może posiadać znaku specjalnego
            return len(set(string.punctuation).intersection(username)) > 0

        username = input("Podaj login: ")
        username.casefold()
        if has_not_special(username):
            print("Twój login ma znak specjalny")
            Register().newuser()
        else:
            pass

        with open(db_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for usernames, passwords in csv_reader:
                if username.casefold() == usernames.casefold():
                    print("Nazwa użytkownika jest już zajęta lub zawiera znak specjalny")
                    Register().newuser()
        # password = input("Podaj hasło: ")
        # password2 = input("Ponownie podaj hasło: ")
        password = getpass.getpass("Podaj hasło: ")
        password2 = getpass.getpass("Ponownie podaj hasło: ")
        if password == password2 and long_enough(password) and has_uppercase(password) and has_numeric(
                password) and has_special(password):
            with open(db_path, 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([username, password])
                print("Utworzono użytkownika, odpal program ponownie aby się zalogować")
                return False
        else:
            print("""\n\n-----------------\nPodane hasła sie nie zgadzają lub hasło jest zbyt mało bezpieczne 
            \n wymagania co do bezpiecznego hasła to przynajmniej 6 znaków, 
            przynajmniej jedna duża litera oraz przynajmniej jedna cyfra \n\n Ponowna rejestrajca:""")
            Register().newuser()


register = Register()

class Deleteuser:
    def delete_user(self):
        lines = []
        user_to_delete = input("Podaj username użytkownika do usunięcia: ")
        with open(db_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                lines.append(row)
                for field in row:
                    if field == user_to_delete:
                        lines.remove(row)
        with open(db_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(lines)
        print("Usunięto użytkownika:", user_to_delete, "- program zostanie zamkniety")


delete = Deleteuser()
"""
def login():
    username = input("Podaj login: ")
    #password = input("Podaj hasło: ")
    password = getpass.getpass("Podaj hasło: ")
    with open(db_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for usernames, passwords in csv_reader:
            if username.casefold() == usernames.casefold() and password == passwords:
                print("Jesteś zalogowany!")
                return True
    print("Niepoprawy login lub hasło")
    login()
    return False



def list():
    with open(db_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        print("\nLista użytkowników: ")
        k = 1
        for user, password in csv_reader:
            print("Użytkownik", k, ": ", user)
            k += 1


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

"""

"""
def register():
    def long_enough(password):
        # Przynajmniej 6 znakow
        return len(password) >= 6

    def has_uppercase(password):
        # Przynajmniej jedna duża litera
        return len(set(string.ascii_uppercase).intersection(password)) > 0

    def has_numeric(password):
        # Musi zawierać cyfrę
        return len(set(string.digits).intersection(password)) > 0

    def has_special(password):
        # Musi zawierać znak specjalny
        return len(set(string.punctuation).intersection(password)) > 0

    def has_not_special(username):
        # Login nie może posiadać znaku specjalnego
        return len(set(string.punctuation).intersection(username)) > 0

    username = input("Podaj login: ")
    username.casefold()
    if has_not_special(username):
        print("Twój login ma znak specjalny")
        register()
    else:
        pass

    with open(db_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for usernames, passwords in csv_reader:
            if username.casefold() == usernames.casefold():
                print("Nazwa użytkownika jest już zajęta lub zawiera znak specjalny")
                register()
    # password = input("Podaj hasło: ")
    # password2 = input("Ponownie podaj hasło: ")
    password = getpass.getpass("Podaj hasło: ")
    password2 = getpass.getpass("Ponownie podaj hasło: ")
    if password == password2 and long_enough(password) and has_uppercase(password) and has_numeric(
            password) and has_special(password):
        with open(db_path, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([username, password])
            print("Utworzono użytkownika, odpal program ponownie aby się zalogować")
            return False
    else:
        print(\n\n-----------------\nPodane hasła sie nie zgadzają lub hasło jest zbyt mało bezpieczne 
        \n wymagania co do bezpiecznego hasła to przynajmniej 6 znaków, 
        przynajmniej jedna duża litera oraz przynajmniej jedna cyfra \n\n Ponowna rejestrajca:)
        register()

"""