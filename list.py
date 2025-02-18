# # LISTS
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

techs = ["react", "angular", "python", "nodeJs"]
print(techs)
print(techs[-2:], len(techs))
print("react" not in techs)

techs[0:4] = ["js"]

print(dir(techs))

# EXERCISE 1
expenses = [2200, 2350, 2600, 2130, 2190]


# 1. In Feb, how many dollars you spent extra compare to January?
print("I spend", expenses[1] - expenses[0], "more in Feb than Jan")
# 2. Find out your total expense in first quarter (first three months) of the year.
print("Total expenses in first quarter: ", expenses[0] + expenses[1] + expenses[2])
# 3. Find out if you spent exactly 2000 dollars in any month
print("Spend 2000 $ in: ", 2000 in expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print(expenses)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses[3] = expenses[3] - 200
print(expenses)

# EXERCISE 2

# You have a list of your favorite marvel super heroes.
# heroes=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)


heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]

# 1. Length of the list
print(len(heroes))
# 2. Add 'black panther' at the end of this list
heroes.append("black panther")
print(heroes)
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heroes.pop()
heroes.insert(3, "black panther")
print(heroes)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heroes[1:3] = ["doctor strange"]
print(heroes)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heroes.sort()
print(heroes)
