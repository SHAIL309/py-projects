# Using following list of cities per country,
# india = ["mumbai", "bangalore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
# For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"


india = ["mumbai", "bangalore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# EXERCISE 1.1
city_name = input("Enter name of the city: ")

if city_name in india:
    print(f"{city_name} is in India")
elif city_name in pakistan:
    print(f"{city_name} is in Pakistan")
elif city_name in bangladesh:
    print(f"{city_name} is in Bangladesh")
else:
    print("No data for given city")

# EXERCISE 1.2
city_1 = input("Enter name of city 1: ")
city_2 = input("Enter name of city 2: ")

if city_1 not in india and city_1 not in pakistan and city_1 not in bangladesh:
    print("City 1 is not there")
    exit()


if city_2 not in india and city_2 not in pakistan and city_2 not in bangladesh:
    print("City 2 is not there")
    exit()


if city_1 in india and city_2 in india:
    print("Both city are in India")
elif city_1 in pakistan and city_2 in pakistan:
    print("Both city are in Pakistan")
elif city_1 in bangladesh and city_2 in bangladesh:
    print("Both city are in Bangladesh")
else:
    print("both are in different country")

# EXERCISE 2

sugar_level = float(input("Enter you fasting sugar level: "))

if sugar_level not in range(80, 100):
    if sugar_level < 80:
        print("!!! Sugar level is low")
    elif sugar_level > 100:
        print("Sugar level is high !!!")
else:
    print("Sugar level is in control")
