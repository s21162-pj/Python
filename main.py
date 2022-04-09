import os
import sys
# from users.users_service import login, register, delete
# from database.database import roomCreate
import getpass
import bcrypt
import uuid
from database.users_model import User
from users.users_service import UserService
from database.room import Room

if __name__ == '__main__':
    # usr1 = User(1, 'test_user', 'test_password')
    # print(f"User{usr1.user_id} --> {usr1})")
    # usr2 = User(2, 'test_user2', 'test_password2')
    # print(f"User{usr2.user_id} --> {usr2})")

    # check users login status
    # print(usr1.check_login_status())
    # print(usr2.check_login_status())
    service = UserService()
    menu = int(input("Wpisz: 1 - LOGOWANIE   2 - REJESTRACJA: "))
    if menu == 1:
        name = input("Podaj login: ")
        password = getpass.getpass("Podaj hasło: ")
        usr1 = User(1, name, password)
        service.login(usr1)
        print(service.check_if_user_login(usr1))

        menu2 = int(input("Wpisz:\n1 - Listowanie użytkowników\n2 - Usuń użytkownika\n3 - Tworzenie pokoju\n4 - Dołączanie do pokoju\n5 - Usuwanie swojego pokoju:"))
        if menu2 == 1:
            service.list_users()
            print(service.sortalph())
        if menu2 == 2:
            nametodelete = input("Podaj swój username ponownie, użytkownik zostanie USUNIĘTY: ")
            service.add_user_access(usr1)
            #User(2, nametodelete, password)
            service.delete_user(User(id, nametodelete, password))
            #service.delete_user(usr2)
        if menu2 == 3:
            room_password = input("Podaj hasło dostępu do pokoju: ")
            room_id = uuid.uuid4()
            r1 = Room(room_id, room_password, usr1.name)
            r1.create()
        if menu2 == 4:
            # TODO: Dodawanie userów do listy
            # TODO: HASLA

            room_id = input("Wklej lub wpisz unikalne id pokoju:")
            room_password = input("Podaj hasło dostępu do pokoju: ")
            r1 = Room(room_id, room_password, usr1.name)
            r1.join(usr1, room_id, room_password)

        if menu2 == 5:
            # TODO: USUWANIE POKOJU
            service.add_user_access(usr1)
            room_id = input("Podaj id pokoju który ma zostać usunięty:")
            room = Room()
            room.delete_room(room_id)






    if menu == 2:
        name = input("Podaj login: ")
        name.casefold()
        password = getpass.getpass("Podaj hasło: ")
        usr1 = User(1, name, bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt()))
        service.register(usr1)

    #users
    #usr1 = User(1, "Rob", "zaq1@WSX")
    #usr2 = User(2, 'test_user2', 'test_password2#')

    #service
    #service = UserService()

    #register
    # service.register(usr1)
    #service.register(usr2)

    # UserService().login(usr1)
    # print(UserService().check_if_user_login(usr1))

    #service.login(usr2)
    #print(service.check_if_user_login(usr2))

    #dodawanie uprawnien do usuniecia uzytkownika
    #service.add_user_access(usr2)
    #service.delete_user(usr2)

    #lista uzytkownikow
    # service.list_users()

    #sorotowanie
    # print(service.sortalph())


    #Tworzenie pokoju
    #r1 = Room(1, 'room_password2#', usr2.name)
    #r1.create()
    #r1.join(usr2, 'room_password2#')

"""
    1. Create User -> UserService.register()
    2. Login User -> UserService.login()
    3. List users -> UserService.show_all_users()
    4. Delete users -> UserService.delete_user()
    5. Create room -> UserService.create_room()
"""
