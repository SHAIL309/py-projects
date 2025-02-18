n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))

operation = input("Select any of the operation from '+','-','*','/' : ")

result = 0


def final_result():
    global result  # Use global result to update it outside the function
    match operation:
        case "+":
            result = n1 + n2
        case "-":
            result = n1 - n2
        case "*":
            result = n1 * n2
        case "/":
            if n2 != 0:  # Avoid division by zero
                result = n1 / n2 if n1 > n2 else n2 / n1
            else:
                result = "Error: Division by zero"
        case _:
            result = "Invalid operation"


final_result()

# Check for a valid result
if result == "Invalid operation" or result == "Error: Division by zero":
    print(result)
else:
    print("Result is: ", result)


# AREA OF TRIANGLE
# Write a program that can find area of a triangle. It should take base and height as an input from user and using that it should print an area of a triangle
height = float(input("Enter height of the triangle: "))
base = float(input("Enter base length of the triangle: "))

area = 1 / 2 * base * height

print("Area of triangle is:", area, "sq units")

# FILE NAME WITHOUT EXTENSION
# Write a program that takes file name with extension as an input and prints just the file name without extension (you can assume that file extensions are always 3 character long)
file_name = input("Enter file name: ")

print("File name without extension : ", file_name[: len(file_name) - 3])
