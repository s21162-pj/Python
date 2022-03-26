import os
import sys
from usr_mngmnt import login, list, sortalph, register, delete_user

def check_db_exists(path):
    try:
        os.stat(path)
    except FileNotFoundError:
        f = open(path, "w")
        f.close()

def run():
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

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(current_dir)
    print(os.path.join(current_dir, "db.csv"))
    db_path = os.path.join(current_dir, "db.csv")
    check_db_exists(db_path)
    run()