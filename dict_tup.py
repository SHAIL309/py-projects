# FIND COUNTRY POPULATION

# We have following information on countries and their population (population is in crores),

# Country	Population
# China	    143
# India	    136
# USA	    32
# Pakistan	21
# Using above create a dictionary of countries and its population

# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21

# add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
# query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.


population = {"China": 143, "India": 136, "USA": 32, "Pakistan": 21}


def print_data():
    for country, pop in population.items():
        print(f"{country} ==> {pop}")


def query_data():
    user_input = input("Enter country name: ")
    find_country = population.get(user_input.capitalize())
    print(find_country if find_country else "Country dont't exist")


def add_data():
    user_input = input("Enter country name: ")
    find_country = population.get(user_input.capitalize())
    if find_country:
        print("Country exists")
    else:
        user_input_pop = int(input(f"Enter population for {user_input}: "))
        population[user_input] = user_input_pop
        print(population)


def remove_data():
    user_input = input("Enter country name: ")
    find_country = population.get(user_input.capitalize())
    if find_country:
        del population[user_input.capitalize()]
        print(population)
    else:
        print("Country doesn't exists")


print(f"Here is the list of countries ", population.keys())
operation = input("What to perform : query , add, remove, print? : ")

if operation.lower() == "print":
    print_data()
elif operation.lower() == "add":
    add_data()
elif operation.lower() == "remove":
    remove_data()
elif operation.lower() == "query":
    query_data()
else:
    print("Improper input")


# STOCK PRICE

# You are given following list of stocks and their prices in last 3 days,

# Stock	 Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]

# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list.
# Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

stock = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160],
}


def print_all():
    for st, pr in stock.items():
        stock_sum = 0
        for s in pr:
            stock_sum += s
        print(f"{st} ==> {pr} ==> avg: {round(stock_sum/len(pr),2)}")


def add_stock():
    stock_name = input("Enter stock name: ")
    if stock_name in stock:
        print("Stock exist")
    else:
        stock_price = float(input("Enter stock price: "))
        stock[stock_name] = [stock_price]
        print_all()


def main():
    op = input("Enter operation (print, add or amend):")
    if op.lower() == "print":
        print_all()
    elif op.lower() == "add":
        add_stock()
    else:
        print("Unsupported operation:", op)


if __name__ == "__main__":
    main()


# Write circle_calc() function that takes radius of a circle as an input from user and then it calculates
# and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them

import math


def circle_calc(r=1):
    diameter = r * 2
    circumference = 2 * r * math.pi
    area = math.pi * (r**2)
    return round(diameter, 2), round(circumference, 2), round(area, 2)


if __name__ == "__main__":
    r = float(input("Enter radius of circle: "))
    d, c, a = circle_calc(r)
    print(f"Diameter : {d}\nCircumference : {c}\nArea : {a}")
