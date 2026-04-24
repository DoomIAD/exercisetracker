class Exercise:
    def __init__(self, exercise, sets=1, rep=1, weight=0):
        self.exercise = exercise
        self.sets = sets
        self.rep = rep
        self.weight = weight

    def __str__(self):
        return f"Exercise: {self.exercise}\nSets: {self.sets}\nReps: {self.rep}\nWeight: {self.weight}\n"
        

class Workout:
    def __init__(self,day,exercise_list):
        self.day=day
        self.exercise_list=exercise_list
    def print_workout(self):
        print("Day:",self.day)
        for i in self.exercise_list:
            print ("\n"+self.exercise_list[i])

class User:
    def __init__(self,weight,height,age,gender):
        self.weight=weight
        self.height=height
        self.age=age
        self.gender=gender
    def __str__(self):
        return f"Weight: {self.weight}\nHeight: {self.height}\nAge: {self.age}\nGender: {self.gender}\n"