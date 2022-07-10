import json
import os
import json
from datetime import datetime

current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')


def clone_data(email):
    # clones data on signin from offsite_database.json to Local_data.json
    with open('offsite_database.json', 'r') as fp:
        temp = json.load(fp)
        for array in temp['Users']:
            key = (array.keys())
            key_val = (array.values())
            if list(key) == ["email-" + email]:
                for k in key_val:
                    kv_dict = k

    with open('Local_data.json', 'w') as fp:
        json.dump(kv_dict, fp, indent=4)
    print("data pulled successfully")
    from interface import interface
    interface()


def main(status):
    def create_and_save_initial_data():
        with open('Local_data.json', 'w') as fp:
            units = input("choose system of measurement : 1)imperial  2)metric")
            weight_in = input("weight : ")
            height_in = input("height : ")
            age_in = input("age : ")
            gender_in = input("gender : ")
            while gender_in not in ["male", "female"]:
                gender_in = input("gender : ")
                if gender_in in ["male", "female"]:
                    break
            exercise_per_week_in = input("weekly active days : ")
            while int(exercise_per_week_in) not in range(1, 8):
                exercise_per_week_in = input("weekly active days : ")
                if int(exercise_per_week_in) in range(1, 8):
                    break
            goal_in = input("goal : ")
            while goal_in not in ["gain", "maintain", "lose"]:
                goal_in = input("goal : ")
                if goal_in in ["gain", "maintain", "lose"]:
                    break
            body_fat_pct_in = input("body fat percentage(optional): ")

            local_user = {
                "units": units,
                "weight": weight_in,
                "height": height_in,
                "age": age_in,
                "gender": gender_in,
                "exercise_per_week": exercise_per_week_in,
                "goal": goal_in,
                "body_fat_pct": body_fat_pct_in

            }
            json.dump(local_user, fp, indent=4)

    def body_measurements():

        weight = user.weight * unit.w_multiplier
        height = user.height * unit.h_multiplier
        weight_converter = unit.w_divider
        height_converter = unit.h_divider

        def body_mass_index():
            bmi = (weight / (height * 12) ** 2) * 700
            return round(bmi, 2)

        body_mass_index()

        def estimate_body_fat():
            ebf = 0
            if user.gender == "female":
                ebf += (1.20 * body_mass_index()) + (0.23 * user.age) - 5.4
            if user.gender == "male":
                ebf += (1.20 * body_mass_index()) + (0.34 * user.age) - 16.2
            return ebf

        def lean_body_mass():
            lbm = weight * (1 - estimate_body_fat() / 100) * weight_converter
            return lbm

        def basal_metabolic_rate():
            bmr = 0
            if user.gender == "male":
                bmr += (2 * ((6 + weight) + (12 * height * 12) - (7 * user.age))) + 66
            if user.gender == "female":
                bmr += (2 * ((4 * weight) + (5 * height * 12) - (5 * user.age))) + 660
            return bmr

        def min_protein_requirements():
            mpr = lean_body_mass() / 2.2 * 2.25
            return mpr

        with open('Local_data.json', "r") as rf:
            ex = json.load(rf)
            local_user = {
                "body_mass_index": body_mass_index(),
                "body_fat_pct": estimate_body_fat(),
                "lean_body_mass": lean_body_mass(),
                "basal_metabolic_rate": basal_metabolic_rate(),
                "min_protein_requirements": min_protein_requirements(),
            }
            ex.update(local_user.items())
            with open('Local_data.json', 'w') as fp:
                json.dump(ex, fp, indent=4)

    def set_macros():
        PROTEIN_KCAL = 4
        CARBS_KCAL = 4
        FATS_KCAL = 9

        weight = user.weight * unit.w_multiplier
        height = user.height * unit.h_multiplier
        weight_converter = unit.w_divider
        height_converter = unit.h_divider

        if user.goal == "gain":
            protein = weight * PROTEIN_KCAL
            carbs = weight * 2 * CARBS_KCAL
            fats = weight * 0.45 * FATS_KCAL
        elif user.goal == "lose":
            protein = weight * 1.4 * PROTEIN_KCAL
            carbs = weight * CARBS_KCAL
            fats = weight * 0.25 * FATS_KCAL
        elif user.goal == "maintain":
            protein = weight * PROTEIN_KCAL
            carbs = weight * 1.6 * CARBS_KCAL
            fats = weight * 0.35 * FATS_KCAL

        def total_daily_energy_expenditure():

            if user.exercise_per_week < 2:
                tdee = user_measurements.basal_metabolic_rate * 1.2
            elif user.exercise_per_week in [2, 3]:
                tdee = user_measurements.basal_metabolic_rate * 1.375
            elif user.exercise_per_week in [4, 5]:
                tdee = user_measurements.basal_metabolic_rate * 1.55
            else:
                tdee = user_measurements.basal_metabolic_rate * 1.725
            return tdee

        total_daily_energy_expenditure()
        tdee = total_daily_energy_expenditure()

        def calculate_macros(protein, carbs, fats):
            total_kcal = (protein + carbs + fats)
            clock = 0
            ptn = protein
            if user.goal == "gain":

                while total_kcal > tdee + 500:
                    protein += 1
                    carbs += 1
                    fats += 1
                    total_kcal = (protein + carbs + fats)
            if user.goal == "lose":
                while total_kcal < tdee - 350:
                    protein += 1
                    carbs += 1
                    fats += 1
                    total_kcal = (protein + carbs + fats)

            if user.goal == "maintain":
                while total_kcal < tdee - 100:
                    while total_kcal < tdee + 100:
                        protein += 1
                        carbs += 1
                        fats += 1
                        total_kcal = (protein + carbs + fats)

            with open('Local_data.json', "r") as rf:
                ex = json.load(rf)
                local_user = {
                    "protein": protein,
                    "carbs": carbs,
                    "fats": fats,
                    "total_kcal": total_kcal,
                    "tdee": tdee,
                }
                ex.update(local_user.items())
                with open('Local_data.json', 'w') as fp:
                    json.dump(ex, fp, indent=4)

        (calculate_macros(protein, carbs, fats))

    def check_data():
        status_of = status
        if status_of in ["signup", "skip"]:
            try:
                file_exists = os.path.exists("Local_data.json")
                if file_exists is True:
                    create_and_save_initial_data()

            except IOError or json.JSONDecodeError:
                create_and_save_initial_data()
        elif status_of == "signin":
            try:
                file_exists = os.path.exists("Local_data.json")
                if file_exists is True:
                    try:
                        with open('Local_data.json') as data_file:
                            from_data = json.load(data_file)
                            units = from_data.get("tdee")

                    except json.JSONDecodeError:
                        print("local data missing")
                        create_and_save_initial_data()
            except IOError:
                print("user data corrupted")
                create_and_save_initial_data()

        # if json file containing user data does not exist function below creates json file and saves data on it

    check_data()

    # class below assign's data to class attributes

    class Person:

        def __init__(self, units, weight, height, age, gender, exercise_per_week, goal, body_fat_pct, ):
            self.units = units
            self.weight = float(weight)
            self.height = float(height)
            self.age = int(age)
            self.gender = str(gender)
            self.exercise_per_week = int(exercise_per_week)
            self.goal = goal
            self.body_fat_pct = body_fat_pct

    with open('Local_data.json') as data_file:
        from_data = json.load(data_file)
    units = from_data.get("units")
    weight = from_data.get("weight")
    height = from_data.get("height")
    age = from_data.get("age")
    gender = from_data.get("gender")
    exercise_per_week = from_data.get("exercise_per_week")
    goal = from_data.get("goal")
    body_fat_pct = from_data.get("body_fat_pct")
    user = Person(units, weight, height, age, gender, exercise_per_week, goal, body_fat_pct)

    if user.units in ["imperial", "1"]:
        weight_multiplier = 1
        height_multiplier = 1
        weight_divider = 1
        height_divider = 1
    if user.units in ["metric", "2"]:
        weight_multiplier = 2.204
        height_multiplier = 0.0328
        weight_divider = 0.453
        height_divider = 30.48

    class GetUnit:
        def __init__(self, w_multiplier, h_multiplier, w_divider, h_divider):
            self.w_multiplier = float(w_multiplier)
            self.h_multiplier = float(h_multiplier)
            self.w_divider = float(w_divider)
            self.h_divider = float(h_divider)

    w_m = weight_multiplier
    h_m = height_multiplier
    w_d = weight_divider
    h_d = height_divider

    unit = GetUnit(w_m, h_m, w_d, h_d)

    # after the data assignment, further calculations are performed using before mentioned class attributes
    body_measurements()

    class Measurements:
        def __init__(self, body_mass_index, lean_body_mass, basal_metabolic_rate, min_protein_requirements):
            self.body_mass_index = body_mass_index
            self.lean_body_mass = lean_body_mass
            self.basal_metabolic_rate = basal_metabolic_rate
            self.min_protein_requirements = min_protein_requirements

    with open('Local_data.json') as data_file:
        from_data = json.load(data_file)
    bmi = from_data.get("body_mass_index")
    lbm = from_data.get("lean_body_mass")
    bmr = from_data.get("basal_metabolic_rate")
    mpr = from_data.get("min_protein_requirements")
    user_measurements = Measurements(bmi, lbm, bmr, mpr)

    set_macros()

    class Diet:
        def __init__(self, protein, carbs, fats, tdee, total_kcal):
            self.fats = fats
            self.carbs = carbs
            self.protein = protein
            self.tdee = tdee
            self.total_kcal = total_kcal

    with open('Local_data.json') as data_file:
        from_data = json.load(data_file)
    protein = from_data.get("protein")
    carbs = from_data.get("carbs")
    fats = from_data.get("fats")
    total_kcal = from_data.get("total_kcal")
    tdee = from_data.get("tdee")
    user_macros = Diet(protein, carbs, fats, tdee, total_kcal)

    # print(f"your macros in grams \n"
    #       f"Suggested Protein intake : {protein}grams\n"
    #       f"Suggested Carbohydrate intake : {carbs}grams\n"
    #       f"Suggested fat intake : {fats}grams\n"
    #       f"calculated energy expenditure : {tdee} kcal\n")
    # if user.goal == "lose":
    #     print(f"calorie deficit of : {tdee - total_kcal} kcal per day")
