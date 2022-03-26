import csv
import os
import sys
import getpass
from pw_mngmng import long_enough, has_uppercase, has_numeric, has_special

def check_db_exists(path):
    try:
        os.stat(path)
    except FileNotFoundError:
        f = open(path, "w")
        f.close()

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(current_dir)
    print(os.path.join(current_dir, "db.csv"))
    db_path = os.path.join(current_dir, "db.csv")
    check_db_exists(db_path)

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

def register():
    username = input("Podaj login: ")
    username.casefold()
    with open(db_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for usernames, passwords in csv_reader:
            if username.casefold() == usernames.casefold():
                print("Nazwa użytkownika jest już zajęta")
                register()
    #password = input("Podaj hasło: ")
    #password2 = input("Ponownie podaj hasło: ")
    password = getpass.getpass("Podaj hasło: ")
    password2 = getpass.getpass("Ponownie podaj hasło: ")
    if password == password2 and long_enough(password) and has_uppercase(password) and has_numeric(password) and has_special(password):
        with open(db_path, 'a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([username, password])
            print("Utworzono użytkownika, odpal program ponownie aby się zalogować")
            exit()
    else:
        print("""\n\n-----------------\nPodane hasła sie nie zgadzają lub hasło jest zbyt mało bezpieczne 
        \n wymagania co do bezpiecznego hasła to przynajmniej 6 znaków, 
        przynajmniej jedna duża litera oraz przynajmniej jedna cyfra \n\n Ponowna rejestrajca:""")
        register()

def login():
    username = input("Podaj login: ")
    #password = input("Podaj hasło: ")
    password = getpass.getpass("Podaj hasło: ")
    with open(db_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        #for line in csv_reader:
        for usernames, passwords in csv_reader:
            if username.casefold() == usernames.casefold() and password == passwords:
            #if line == [username, password]:
                print("Jesteś zalogowany!")
                return True
    print("Niepoprawy login lub hasło")
    login()
    return False

def delete_user():
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

menu = int(input("Wpisz: 1 - LOGOWANIE   2 - REJESTRACJA: "))

if menu == 1:
    login()
    pass
    after_login_menu = int(input("1 - Wylistowanie nazw użytkowników    2 - Usuń użytkownika:  "))
    if after_login_menu == 1:
        list()
        sortalph()
    elif after_login_menu == 2:
        list()
        delete_user()
elif menu == 2:
    register()
else:
    print("Błąd, wybrano niewłaściwą opcję, odpal program od nowa")
    pass