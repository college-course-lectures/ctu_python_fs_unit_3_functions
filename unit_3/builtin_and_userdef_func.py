#Pre-defined functions - built-in functions
# name = input("What's your name?")
# print("Hi ", name)
#
# nums = [1, 2,3]
# squares = list(map(lambda x:x*x, nums))
# print(squares)

#User defined functions

def greet(name):
    return f"Hello, {name}"

def show_info(name="Guest", age=25):
    print(f"{name} is {age} years old.")

def use_lambda_map(nums):
    print(list(map(lambda x: x+10,nums)))

#isinstance() checks if a variable is of a certain type
def check_number_type(number):
    if isinstance(number, int):
        print(f"Number {number} is an Integer.")
    elif isinstance(number, float):
        print(f"Number {number} is a float.")

#Dictionaries - use key-value stores
def use_dictionaries():
    student = {"name": "Tracy","age": 22}
    print(student)

    print(student.get("name"))
    print(student.get("grade"))

    student.update({"grade": "A", "major": "CS"})
    print(student)

    student.setdefault("email", "tracy@gmail.com")
    print(student)

    backup = student.copy()
    print("Back up copy.")
    print(backup)
    student.clear()
    print('Empty student dictionary.')
    print(student)

    #create a dictionary with keys from a list that contain the same value
    #real world - we can return a query with values for id, name and role
    #then update our dictionary

    keys = ["id", "name", "role"]
    default_dict = dict.fromkeys(keys, "unknown")
    print(default_dict)

def use_sets():
       skills = {"Python", "Java"}
       print(skills)
       skills.add("JavaScript")
       print(skills)
       skills.add("Java")
       print(skills)

       #Starting sets
       a = {1,2,3}
       b = {3,4,5}

       #instersection
       #Keeps common elements in both b and a
      # print(a.intersection(b))

       #difference_update
       #Removes shared elements from the first set
       print(a)
      # a.difference_update(b)
       print(a)

       #intersection_update
       # Keep only the common elements in both b and {3, 5} (created new set on fly)
       # Intersection means keep elements common to both:
       # {3, 4, 5} ∩ {3, 5} → {3, 5}
      # b.intersection_update({3,5})
       print(b)

       #symmetric_difference_update
       #keeps items in either set, not both
       # Update 'a' to keep only the elements that are in either set but not both
       #  a = {1,2,3}

       '''
      Symmetric difference means
      Remove common items: 2
      Keep all other unique items:
        From a: 1, 3
        From {2, 5}: 5
      So:
       {1, 2, 3} △ {2, 5} → {1, 3, 5}
      
      
      Now 'a' is updated in place
        Final value of a: {1, 3, 5}

   '''
       a.symmetric_difference_update({2,5})
       print(a)

