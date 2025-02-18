# EXERCISE 1
result = [
    "heads",
    "tails",
    "tails",
    "heads",
    "tails",
    "heads",
    "heads",
    "tails",
    "tails",
    "tails",
]


count = 0
for i in result:
    if i != "heads":
        continue
    count += 1

print(f"Got {count} times head")


# EXERCISE 2

for i in range(10):
    if i % 2 == 0:
        continue
    print(i**2)

# EXERCISE 3
expense_list = [2340, 2500, 2100, 3100, 2980]

expense = int(input("Enter the expense: "))

for i in range(len(expense_list)):
    if expense == expense_list[i]:
        print(f"{expense} occurred in month {i+1}")
        break

    else:
        print("not there")

# EXERCISE 4
for i in range(5):
    print(f"You ran {i+1} miles")  # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == "yes":
        break

if i == 4:  # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print(
        "You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles"
    )


# EXERCISE 5

for i in range(1, 6):
    s = ""
    for j in range(i):
        s += "*"
    print(s)
