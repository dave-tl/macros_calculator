from data_creation_check import main
import json


def signup_logic():
    item_data = {}

    with open('offsite_database.json', 'r') as fp:
        temp = json.load(fp)
        for i in temp['Users']:
            dct = {}
            dct.update(i)
        email = input("email :: ")
        pw = input("password")

        try:
            temp_dct = (dct["email-" + email])
            if email in temp_dct:
                pass
            print("account already exists")
            signup_logic()

        except KeyError:
            main("signup")
            with open('Local_data.json', "r") as rf:
                ex = json.load(rf)
                local_user = {
                    "email": email,
                    "password": pw,
                }
                ex.update(local_user.items())
                with open('Local_data.json', 'w') as fp:
                    json.dump(ex, fp, indent=4)

            with open('Local_data.json', "r") as rf:
                ex = json.load(rf)
            item_data["email-" + email] = ex
            temp["Users"].append(item_data)
            ex.update()
            with open("offsite_database.json", 'w') as f:
                json.dump(temp, f, indent=4)
            print("----------\nregistered successfully\n|||||||||||||||||||||||||")

def interface():
    def sign_in_up():
        print("1 ) Sign in\n----------")
        print("2 ) Sign up\n----------")
        print("3 ) Skip\n----------")
        choice = input("enter operation :: ")
        if choice in ["1", "sign in", "signin"]:

            print("success")
        elif choice in ["2", "sign up", "signup"]:
            signup_logic()
            interface()
        elif choice in ["3", "skip"]:

            print("success")
        else:
            print("\n|||please input valid operation|||\n")
            sign_in_up()

    sign_in_up()


interface()
