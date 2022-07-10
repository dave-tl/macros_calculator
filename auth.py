import json
from data_creation_check import main
from email_validator import validate_email, EmailNotValidError


def signup_logic():
    """
    function checks email in offsite_database.json  if no matches are found then directs to main function
    in data creation da check which creates macros using all the provided user data the all data gets dumped to
    ofcourse the .... offsite_database.json which is definitely offsite
    """
    email = email_validator()
    item_data = {}
    with open('offsite_database.json', 'r') as fp:
        temp = json.load(fp)
        for array in temp['Users']:
            n = (array.keys())
            if list(n) == ["email-" + email]:
                print("exists")
                signup_logic()

    pw = password_validator(email=email)
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


def password_validator(email=None):
    print("\nPassword should contain\n--------------------"
          "\none capital letter \none lower case\none number "
          "\nshould be at least 8 characters\n")
    Password = input("Create password:: ")
    Password1 = input("Repeat password:: ")
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    if Password == email:
        password_validator()
    if len(Password) < 8:
        print("!!!password should contain at least 8 characters!!!")
        password_validator()
    if Password != Password1:
        print("!!!passwords don't match!!!")
        password_validator()
    ck = []
    ck_up = []
    ck_counter = 0
    ck_up_counter = 0
    for char in Password:
        if char in alphabet:
            ck.append(char)
    for char in Password:
        if char in alphabet.upper():
            ck_up.append(char)

    for i in ck:
        ck_counter += 1
    for i in ck_up:
        ck_up_counter += 1
    if ck_counter < 1:
        print("!!!passwords must contain lower-case letters!!!")
        password_validator()
    if ck_up_counter < 1:
        print("!!!passwords must contain capital letters!!!")
        password_validator()
    else:
        return Password


def email_validator():
    email_address = input("Email Address::")
    try:
        validate_email(email_address)
        return email_address
    except:
        print("email adress not valid")
        email_validator()


def signin_logic():
    print(10 * "-" + "\nLogin\n" + 10 * "-")
    email_signin = input("email :: ")
    with open('offsite_database.json', 'r') as fp:
        temp = json.load(fp)
        if True:
            for array in temp['Users']:
                key = (array.keys())
                key_val = (array.values())
                if list(key) == ["email-" + email_signin]:
                    for k in key_val:
                        kv_dict = k
                    password = input("password :: ")
                    password_data = (kv_dict.get('password'))
                    while password != password_data:
                        print('Wrong password')
                        password = input("password :: ")
                    if password == password_data:
                        print(10 * "-" + "\nLogin Successful\n" + 10 * "-")
                        from data_creation_check import clone_data
                        clone_data(email_signin)
                        return
                else:
                    pass
        print("User not found")
        signin_logic()
