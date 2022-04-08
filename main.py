import os
import sys
from users.users_service import login, register, delete
from database.database import roomCreate

def check_db_exists(path):
    try:
        os.stat(path)
    except FileNotFoundError:
        f = open(path, "w")
        f.close()

def run():
    menu = int(input("Wpisz: 1 - LOGOWANIE   2 - REJESTRACJA: "))

    if menu == 1:
        login.logincheck()
        pass
        after_login_menu = int(input("1 - Wylistowanie nazw użytkowników\n2 - Usuń użytkownika\n3 - Utwórz pokój spotkań\n4 - Dołącz do pokoju spotkań\n: "))
        if after_login_menu == 1:
            login.list()
            login.sortalph()
        elif after_login_menu == 2:
            login.list()
            delete.delete_user()
        elif after_login_menu == 3:
            """ Tworzenie pokoju spotkań """
            roomCreate.create()
        elif after_login_menu == 4:
            """ Dołączanie do pokoju spotkań """
    elif menu == 2:
        register.newuser()
    else:
        print("Błąd, wybrano niewłaściwą opcję, odpal program od nowa")
        pass

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(current_dir)
    print(os.path.join(current_dir, "./database.csv"))
    db_path = os.path.join(current_dir, "./database.csv")
    rooms_path = os.path.join(current_dir, "./rooms.csv")
    check_db_exists(db_path)
    run()