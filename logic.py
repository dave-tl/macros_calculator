import json
from datetime import datetime

current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')


def create_and_save_initial_data():
    with open('Local_data.json', 'w') as fp:
        units = input("choose system of measurement : 1)imperial  2)metric ")
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
    from data_creation import user, unit
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
    from data_creation import user, unit, user_measurements

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



