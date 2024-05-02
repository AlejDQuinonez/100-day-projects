greeting = """
Welcome to the Calorie Tracker, Here you can find how much calories you need to either lose weight
or gain weight, along with keeping track of what you're eating throughout the day while displaying
your macros. Please choose from the menu options.

1. Find calorie intake
2. Track calories
3. Add food to your list
4. See current list
5. Exit
"""
BMR = 0
current_fat     = 0
current_carbs   = 0
current_protein = 0

food = {
    "beef": [100, 10, 5, 50]
}

food_macros = ["Calories: ", "Fat: ", "Carbs: ", "Protein: "]

def calorieIntake(sex, age, height, weight):
    if user_sex == "male":
        global BMR
        BMR = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
        print(f"Your calorie intake is {BMR}")
        print()

while True:
    print(greeting)
    menuOption = int(input("\n"))

    if menuOption == 1:
        user_sex    = input("Are you a male or female?\n")
        user_age    = float(input("How old are you?\n"))
        user_height = float(input("What is your height in cm?\n"))
        user_weight = float(input("what is your weight in kg?\n"))
        print()
        calorieIntake(user_sex, user_age, user_height, user_weight)

    elif menuOption == 2:
        print(f"Current Calories for the day are {BMR}. What have you eaten so far?")
        food_tracker = input()

        if food_tracker in food:
            calorie = food[food_tracker][0]
            fat = food[food_tracker][1]
            carbs = food[food_tracker][2]
            protein = food[food_tracker][3]

            BMR = BMR - calorie
            current_fat += fat
            current_carbs += carbs
            current_protein += protein

            print(f"Current Caloires left: {BMR}")
            print(f"Total fat eaten: {current_fat}")
            print(f"Total carbs eaten: {current_carbs}")
            print(f"Total protein eaten: {current_protein}")
            print()

    elif menuOption == 3:
        food_type    = input("What food do you want to add? (name)\n")
        food_calorie = int(input("Food's calorie content(in grams):\n"))
        food_fat     = int(input("Food's fat content(in grams):\n"))
        food_carb    = int(input("Food's carbs content(in grams):\n"))
        food_protein = int(input("Food's protein content(in grams):\n"))
        food[food_type] = [food_calorie, food_fat, food_carb, food_protein]
        print()
        
        for key, value in food.items():
            print(key)
            for x in range(len(food_macros)):
                print(food_macros[x], value[x])
            print()

    elif menuOption == 4:
        print()
        for key, value in food.items():
            print(key)
            for x in range(len(food_macros)):
                print(food_macros[x], value[x])
            print()

    elif menuOption == 5:
        break

