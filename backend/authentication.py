import pickle as p


def sign_up(user_profiles):
    try:
        with open("user_profiles.dat", "ab") as f:
            p.dump(user_profiles, f)
            f.seek(0)

    except EOFError:
        pass


def log_in(name, password):
    try:
        with open("user_profiles.dat", "rb") as f:
            while True:
                r = p.load(f)

                for i in r:
                    if (i[0] == name and i[1] == password):
                        print("Authenticated")

    except EOFError:
        pass


user_profiles = []

while True:
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    authenticate = input("Sign up or Log in: ")
    user_profiles.append([name, password])

    if (authenticate == "Sign up"):
        sign_up(user_profiles)
    elif (authenticate == "Log in"):
        log_in(name, password)
        break
    else:
        print("Invalid input!")
        continue