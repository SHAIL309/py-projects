# AREA OF TRIANGLE
# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
def calculate_area(base, height):
    return (1 / 2) * base * height


# AREA OF TRIANGLE OR RECTANGLE
# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area.
# If no shape is supplied then it should take triangle as a default shape


def calculate_area(base, height, shape="triangle"):
    area = 0
    if shape == "rectangle":
        area = base * height
    else:
        area = (1 / 2) * base * height
    return area


# PATTERN
# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
#   *
#   **
#   ***
# if input is 4 then it should print
#   *
#   **
#   ***
#   ****

# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)


def print_pattern(row=3):
    for i in range(row):
        s = ""
        for j in range(i + 1):
            s = s + "*"
        print(s)


print_pattern(4)
