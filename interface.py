from auth import *



def sign_in_up():
    print("1 ) Sign in\n----------")
    print("2 ) Sign up\n----------")
    print("3 ) Skip\n----------")
    choice = input("enter operation :: ")
    if choice in ["1", "sign in", "signin"]:
        signin_logic()
    elif choice in ["2", "sign up", "signup"]:
        signup_logic()
        signin_logic()
    elif choice in ["3", "skip"]:
        print("success")
    else:
        print("\n|||please input valid operation|||\n")
        sign_in_up()


sign_in_up()
