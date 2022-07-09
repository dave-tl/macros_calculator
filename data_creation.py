import json
import os
from logic import create_and_save_initial_data, body_measurements, set_macros

def check_data(status=True):
    try:
        file_exists = os.path.exists("Local_data.json")
        if file_exists is True:

            return
    except IOError:
        var = False
    # if json file containing user data does not exist function below creates json file and saves data on it
    create_and_save_initial_data()

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

exit(interface())

