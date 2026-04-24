import workout_classes
import customtkinter

reply = input("Welcome to Exercise Tracker!\nWhat would you like to do?\n 1. Create a workout\n 2. Update biometrics\n")

if reply == "1":
    print("Exercise Creator")
    exercise=input("Exercise Name:\n")
    set = input("Number of Sets:\n")
    rep = input("Number of Reps per Set:\n")
    weight = input("Weight:\n")
    
    new_exercise = workout_classes.Exercise(exercise,set,rep,weight)
    print(new_exercise)

elif reply=="2":
    print("Biometrics Setup")
    weight = input("Weight:\n")
    height = input("Height:\n")
    age = input("Age:\n")
    gender = input("Gender:\n")

    user_data=workout_classes.User(weight,height,age,gender)
    print(user_data)

else:
    print("darn")

