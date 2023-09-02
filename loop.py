def my_name():
    print("My name is Omar")

def my_meal(food = "albaik", drink = "pepsi"):
    print(f"I like eat {food} annd while drinking {drink}")

def cube(number):
    return number*number*number
 
    

def by_three(number):
    if number % 3 == 0:
        cube(number)
    else:
        return "false"
