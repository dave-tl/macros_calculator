from auth import *


def interface():
    """
    todo
    > timestamp data modifications in database
    > implement password / weight / goal / exercise per week modifications
    > add go back button all over the place
    > log out button
    > error handling
    > type enforcement in signup logic
    > exit button
    > ensure that offsite_database.json is ready for data to be saved
    """

    print("---------\nwelcome\n----------")
    from data_creation_check import alldata, main
    main("check integrity")

    print("User: ", alldata.first_name, "", alldata.last_name)
    print("weight:", alldata.weight, "age:", alldata.age, "goal:", alldata.goal, "exercise per week:", alldata.exercise_per_week)
    print("bmi:", alldata.body_mass_index, "tdee:", alldata.tdee, "lean body mass:", alldata.lean_body_mass)
    print("basal metabolic rate:", alldata.basal_metabolic_rate, "min protein requirements:", alldata.min_protein_requirements, )


def main():
    def sign_in_up():
        print("1 ) Sign in\n----------")
        print("2 ) Sign up\n----------")
        print("3 ) Skip\n----------")
        choice = input("enter operation :: ")
        if choice in ["1", "sign in", "signin"]:
            signin_logic()
            interface()
        elif choice in ["2", "sign up", "signup"]:
            signup_logic()
            signin_logic()
            interface()
        elif choice in ["3", "skip"]:
            print("success")
        else:
            print("\n|||please input valid operation|||\n")
            sign_in_up()

    sign_in_up()


if __name__ == "__main__":
    main()
