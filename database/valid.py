import string


def password_validation(password):
    if len(password) <= 6:
        print('Password need 6+ characters')
        return False

  #  elif len(set(string.ascii_uppercase).intersection(password)) >= 1:
   #     print("Przynajmniej jedna duża litera")
    #    return False

    elif len(set(string.digits).intersection(password)) > 0:
        print('Haslo musi zawierac cyfre')
        return False

    elif len(set(string.punctuation).intersection(password)) > 0:
        print('Haslo musi zawierac znak specjalny')
        return False
    else:
        return True

